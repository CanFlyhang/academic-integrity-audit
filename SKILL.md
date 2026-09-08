---
name: academic-integrity-audit
description: Audit an uploaded scientific or academic manuscript for evidence-backed text-similarity, citation/source, and AI-writing risk signals; generate a paragraph-level visual report with revision advice. Use for integrity screening and editorial diagnosis, not for proving authorship or evading detectors.
---

# Academic Integrity Audit

Produce a reproducible risk audit, not a verdict. Separate three questions throughout:

1. **Text similarity:** overlap with the comparison corpus actually searched.
2. **Source integrity:** quotations, citations, unverifiable references, and uncited borrowing.
3. **AI-writing signals:** stylistic/statistical indicators that may justify human review.

Never claim to reproduce “all market detectors,” report a universal plagiarism rate, or determine whether AI wrote a passage. Commercial systems use private corpora and changing models. Label AI results as screening signals with uncertainty and plausible non-AI explanations.

## Intake and routing

- Accept PDF, DOCX, Markdown, plain text, LaTeX, or pasted content.
- Preserve headings, paragraphs, quotations, references, tables, captions, equations, and page/section anchors where extraction permits.
- For PDF/DOCX extraction and rendering, use the available PDF/document capabilities. OCR scanned pages before analysis and disclose OCR uncertainty.
- Ask for discipline, language, document type, and comparison corpus only if missing information would materially change interpretation; otherwise infer and state assumptions.
- If external searching is requested, browse scholarly/web sources and cite exact matches. Without external search or a supplied corpus, call the result **limited-corpus similarity**, never “plagiarism rate.”

Before scoring, read [references/methodology.md](references/methodology.md). For report fields and severity rules, read [references/report-schema.md](references/report-schema.md).

## Workflow

1. **Normalize without erasing evidence.** Create a paragraph inventory with stable IDs and anchors. Exclude bibliography, boilerplate, formula-only blocks, code, and correctly marked quotations from AI-style scoring; retain them for source checks.
2. **Build evidence.** Run `scripts/analyze_text.py` on extracted UTF-8 text. If a corpus is available, pass its files with `--corpus`; record names, access dates, and coverage. Search exact distinctive phrases externally only when authorized or requested.
3. **Triangulate.** Treat no single signal as dispositive. An elevated AI-review flag requires at least two materially independent signal families and adequate analyzable text. Downweight formulaic methods/results, translated prose, templates, and heavily copy-edited text.
4. **Review flagged passages manually.** Test legitimate quotation, standard terminology, methods boilerplate, self-reuse, and genre effects before escalating.
5. **Recommend integrity-preserving revisions.** Suggest citation, quotation, synthesis from primary evidence, factual verification, clearer author reasoning, or disclosure where policy requires it. Do not provide detector evasion, synonym spinning, or guaranteed score reduction.
6. **Generate deliverables.** Produce `audit-report.html`, `audit-data.json`, and optionally a visually verified PDF when requested.

## Reporting requirements

- Put corpus coverage beside every similarity percentage.
- Distinguish exact/near-exact overlap from semantic resemblance.
- Show paragraph-level evidence and source links; never highlight a passage without an explanation.
- Express AI-writing results as `low`, `moderate`, `elevated`, or `insufficient evidence`, plus confidence.
- Include false-positive factors and a human-review queue.
- Use neutral language: “risk signal,” “candidate overlap,” and “requires verification.”
- If evidence is inadequate, say so prominently rather than fabricating precision.

## Completion check

Confirm inputs are unchanged, every headline number names its coverage, each severe flag has inspectable evidence, citations resolve where possible, recommendations protect scholarly meaning, and the report states that authorship and misconduct decisions require qualified human review.
