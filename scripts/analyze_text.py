#!/usr/bin/env python3
"""Paragraph-level triage and local-corpus overlap; not an authorship detector."""
from __future__ import annotations
import argparse, datetime as dt, html, json, pathlib, re, statistics
from difflib import SequenceMatcher

VERSION = "1.0.0"
WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿ]+)*|[\u3400-\u9fff]")
SENT_RE = re.compile(r"(?<=[.!?。！？])\s+")
TRANSITIONS = ("furthermore", "moreover", "additionally", "therefore", "consequently",
               "notably", "overall", "in conclusion", "值得注意的是", "此外", "因此", "综上所述")

def words(text): return [w.lower() for w in WORD_RE.findall(text)]
def paras(text): return [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
def shingles(t, n=7): return {tuple(t[i:i+n]) for i in range(max(0, len(t)-n+1))}
def clamp(v): return round(max(0.0, min(100.0, v)), 1)

def signals(text):
    toks = words(text)
    sents = [s for s in SENT_RE.split(text) if words(s)] or [text]
    lengths = [len(words(s)) for s in sents]
    mean = statistics.mean(lengths) if lengths else 0
    cv = statistics.pstdev(lengths)/mean if len(lengths) > 1 and mean else 0
    diversity = len(set(toks))/len(toks) if toks else 0
    bigrams = list(zip(toks, toks[1:]))
    repeat = 1-len(set(bigrams))/len(bigrams) if bigrams else 0
    hits = sum(text.lower().count(x) for x in TRANSITIONS)
    return {"sentence_count": len(sents), "mean_sentence_words": round(mean, 2),
            "sentence_length_cv": round(cv, 3), "lexical_diversity": round(diversity, 3),
            "repeated_bigram_rate": round(repeat, 3), "transition_hits": hits,
            "regularity": clamp((0.42-cv)*135) if len(sents) >= 3 else 0,
            "predictability_proxy": clamp((0.58-diversity)*120 + repeat*80),
            "templating": clamp(hits/max(1, len(sents))*55)}

def matches(text, corpus):
    toks, sh = words(text), shingles(words(text))
    if not sh: return []
    found = []
    for name, source in corpus:
        st, ssh = words(source), shingles(words(source))
        common = sh & ssh
        containment = len(common)/len(sh)
        seq = SequenceMatcher(None, " ".join(toks), " ".join(st), autojunk=True).ratio()
        score = max(containment*100, seq*70)
        if common or score >= 20:
            found.append({"source": name, "score": round(score, 1),
                          "shingle_containment": round(containment, 3),
                          "evidence": " ".join(next(iter(common))) if common else "near-sequence resemblance"})
    return sorted(found, key=lambda x: x["score"], reverse=True)[:5]

def band(score, count, families):
    if count < 40: return "insufficient evidence"
    if score >= 60 and families >= 2: return "elevated"
    if score >= 30 or families >= 1: return "moderate"
    return "low"

def analyze(text, corpus):
    items = []
    for i, p in enumerate(paras(text), 1):
        toks, sig, mt = words(p), signals(p), matches(p, corpus)
        vals = [sig["regularity"], sig["predictability_proxy"], sig["templating"]]
        active, score = sum(v >= 35 for v in vals), clamp(sum(vals)/3)
        sev = band(score, len(toks), active)
        reasons = []
        if sig["regularity"] >= 35: reasons.append("unusually even sentence-length pattern")
        if sig["predictability_proxy"] >= 35: reasons.append("low-diversity/repetition proxy")
        if sig["templating"] >= 35: reasons.append("high transition/template density")
        if mt: reasons.append("candidate overlap in supplied corpus")
        items.append({"id": f"P{i:04d}", "anchor": f"paragraph {i}", "excerpt": p[:280],
            "word_count": len(toks), "ai_style_triage_score": score, "ai_style_severity": sev,
            "confidence": "low" if len(toks) < 80 else "moderate", "signal_families_active": active,
            "signals": sig, "similarity_matches": mt, "reasons": reasons,
            "recommendation": "Review context; revise from verified sources and author reasoning, not to evade detection." if reasons else "No action from local triage."})
    analyzed = [p for p in items if p["ai_style_severity"] != "insufficient evidence"]
    total = sum(p["word_count"] for p in items)
    matched = sum(p["word_count"] for p in items if p["similarity_matches"])
    summary = "elevated" if any(p["ai_style_severity"] == "elevated" for p in analyzed) else ("moderate" if any(p["ai_style_severity"] == "moderate" for p in analyzed) else "low")
    return {"metadata": {"generated_at": dt.datetime.now(dt.timezone.utc).isoformat(), "tool": "analyze_text.py", "version": VERSION},
        "coverage": {"total_paragraphs": len(items), "analyzed_paragraphs": len(analyzed), "total_words": total, "corpus_files": [n for n,_ in corpus]},
        "similarity": {"scope": "supplied local corpus only", "paragraph_word_coverage_percent": round(matched/total*100,1) if total else 0, "note": "Coverage is not a universal plagiarism rate."},
        "ai_style_review": {"summary": summary, "confidence": "low-to-moderate", "note": "Heuristic triage, not an authorship probability."},
        "paragraphs": items, "limitations": ["No proprietary detector or private publisher corpus was queried.", "Heuristics have substantial false-positive risk across genres and languages.", "Human review is required."],
        "human_review_queue": [p["id"] for p in items if p["ai_style_severity"] == "elevated" or p["similarity_matches"]]}

def render(data):
    rows=[]
    for p in data["paragraphs"]:
        cls={"elevated":"high","moderate":"mid","low":"low","insufficient evidence":"none"}[p["ai_style_severity"]]
        why="; ".join(p["reasons"]) or "No material local signal"
        src=", ".join(m["source"] for m in p["similarity_matches"]) or "—"
        rows.append(f'<tr class="{cls}"><td>{p["id"]}</td><td>{html.escape(p["ai_style_severity"])}</td><td>{p["ai_style_triage_score"]}</td><td>{html.escape(p["excerpt"])}</td><td>{html.escape(why)}</td><td>{html.escape(src)}</td></tr>')
    c,a,s=data["coverage"],data["ai_style_review"],data["similarity"]
    return f'''<!doctype html><html lang="en"><meta charset="utf-8"><title>Academic Integrity Risk Audit</title><style>body{{font:15px/1.5 system-ui;margin:0;background:#f4f6f8;color:#17202a}}main{{max-width:1180px;margin:auto;padding:32px}}.notice{{background:#fff4d6;border-left:5px solid #b7791f;padding:14px;margin:20px 0}}.cards{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.card{{background:white;padding:18px;border-radius:10px;box-shadow:0 2px 10px #0001}}.big{{font-size:28px;font-weight:700}}table{{width:100%;border-collapse:collapse;background:white;margin-top:20px}}th,td{{padding:10px;border-bottom:1px solid #dde3e8;text-align:left;vertical-align:top}}th{{background:#22313f;color:white}}tr.high{{border-left:6px solid #c0392b}}tr.mid{{border-left:6px solid #d68910}}tr.low{{border-left:6px solid #27864b}}tr.none{{border-left:6px solid #87929d}}small{{color:#566573}}@media(max-width:800px){{.cards{{grid-template-columns:1fr}}table{{font-size:12px}}}}</style><main><h1>Academic Integrity Risk Audit</h1><small>Generated {html.escape(data['metadata']['generated_at'])}</small><div class="notice"><b>Screening only.</b> This report does not determine authorship or academic misconduct; qualified human review is required.</div><section class="cards"><div class="card"><div>AI-style review</div><div class="big">{html.escape(a['summary'])}</div><small>{html.escape(a['note'])}</small></div><div class="card"><div>Corpus-scoped overlap coverage</div><div class="big">{s['paragraph_word_coverage_percent']}%</div><small>{html.escape(s['note'])}</small></div><div class="card"><div>Analyzed coverage</div><div class="big">{c['analyzed_paragraphs']}/{c['total_paragraphs']}</div><small>{c['total_words']} words; {len(c['corpus_files'])} corpus files</small></div></section><h2>Paragraph evidence map</h2><table><thead><tr><th>ID</th><th>Review band</th><th>Triage score</th><th>Excerpt</th><th>Reasons</th><th>Corpus sources</th></tr></thead><tbody>{''.join(rows)}</tbody></table><h2>Limitations</h2><ul>{''.join(f'<li>{html.escape(x)}</li>' for x in data['limitations'])}</ul></main></html>'''

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("input",type=pathlib.Path)
    ap.add_argument("--corpus",type=pathlib.Path,action="append",default=[])
    ap.add_argument("--json",type=pathlib.Path,default=pathlib.Path("audit-data.json"))
    ap.add_argument("--html",type=pathlib.Path,default=pathlib.Path("audit-report.html")); args=ap.parse_args()
    corpus=[(p.name,p.read_text(encoding="utf-8")) for p in args.corpus]
    data=analyze(args.input.read_text(encoding="utf-8"),corpus)
    args.json.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
    args.html.write_text(render(data),encoding="utf-8")
    print(json.dumps({"json":str(args.json),"html":str(args.html),"review_queue":data["human_review_queue"]},ensure_ascii=False))
if __name__ == "__main__": main()
