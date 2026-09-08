# Methodology and interpretation

## Evidence model

This audit is a screening workflow inspired by public detector families, not an imitation of proprietary products. Use multiple independent families.

### Text similarity

- Exact and normalized phrase overlap using word n-grams.
- Near-duplicate overlap using shingles/Jaccard or sequence matching.
- Semantic resemblance only when embeddings or scholarly search are available; never equate it with copying.
- Citation alignment: whether overlapping claims or wording are quoted and attributed.

Report the searched corpus explicitly. A local corpus score answers only “how much overlaps this corpus?” Web search samples are incomplete and should be described as such.

### AI-writing review signals

- Distributional regularity: unusually even sentence lengths, low variation, repeated cadence.
- Predictability proxies: low lexical diversity, repeated transitions, templated openings/endings, phrase reuse.
- Discourse signals: generic claims, symmetrical lists, excessive signposting, low source-specific detail.
- Citation/factual signals: citations that do not support claims, invented or unresolvable references, mismatched metadata.
- Document inconsistency: abrupt shifts in terminology, voice, spelling convention, or technical depth.

These signals are non-unique. Careful human writing, translated prose, language-learning backgrounds, standardized methods, professional editing, and disciplinary conventions can produce the same patterns. Perplexity/burstiness values are model-, tokenizer-, language-, and genre-dependent; do not invent them without an actual named model and calibration set.

## Scoring rules

- Score paragraphs only when they contain at least 40 analyzable words; otherwise use `insufficient evidence`.
- Local heuristic scores are triage values from 0–100, not probabilities.
- `elevated` requires at least two independent signal families.
- Confidence reflects evidence quality and coverage, not severity.
- Similarity and AI-style scores must never be averaged into a single “integrity score.”

Suggested triage bands: 0–29 low, 30–59 moderate, 60–100 elevated. Override downward when false-positive factors dominate, and explain the override.

## Similarity classification

- **Attributed quotation:** quoted and cited; exclude from misconduct risk while checking accuracy.
- **Standard expression:** unavoidable terminology or methods boilerplate; usually low concern.
- **Possible self-overlap:** same author/work; assess journal policy and disclosure.
- **Candidate unattributed overlap:** distinctive wording or structured paraphrase without adequate attribution; prioritize for review.
- **Unresolved:** source unavailable or match too weak.

## Ethical boundary

Refuse requests to conceal AI use, defeat a detector, fabricate sources, or mechanically alter wording solely to lower a score. Offer legitimate alternatives: verify claims, cite sources, disclose tool use under venue policy, restore author reasoning, and rewrite from evidence rather than from the flagged sentence.
