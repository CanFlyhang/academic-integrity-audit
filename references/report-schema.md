# Report schema

## Machine-readable JSON

- `metadata`: title, language, discipline, document type, timestamp, tool/version.
- `coverage`: total/analyzed paragraphs and words, exclusions, OCR status, corpora and searches.
- `similarity`: corpus-scoped aggregate plus match records; never a universal plagiarism percentage.
- `ai_style_review`: category, confidence, signal distribution, false-positive factors.
- `paragraphs`: stable ID, anchor, excerpt, word count, similarity findings, signals, severity, confidence, reasons, recommendations.
- `reference_checks`: reference, resolved identifier/link, status, and claim-support notes.
- `limitations`: plain-language constraints.
- `human_review_queue`: ordered paragraph/reference IDs with reasons.

## Visual HTML

Use a restrained scholarly design with accessible contrast. Include scope and limitations; separate summary cards; coverage/provenance; a paragraph heatmap; evidence table; revision plan grouped by integrity action; and methodology appendix.

Use gray for insufficient evidence, amber for moderate, and red for elevated, but do not encode conclusions only by color. End with: “This screening report does not determine authorship or academic misconduct; qualified human review is required.”

## Severity language

- Low: no material signal in available evidence.
- Moderate: one meaningful signal family or limited corroboration; inspect in context.
- Elevated: multiple independent signal families or strong candidate overlap; prioritize human review.
- Insufficient evidence: too little text, poor extraction, or inadequate corpus/model coverage.
