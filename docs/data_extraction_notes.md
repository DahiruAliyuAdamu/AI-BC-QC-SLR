# Data Extraction Notes

This folder contains repository-ready files extracted from the current AI-BC-QC-SLR folder.

## Extracted source files

- `data/included_studies_metadata.csv` was created from the 77-study QA Excel file.
- `data/bibliometric_dataset.csv` was created as a paper-level bibliometric template using the available title, author, and year fields.
- `data/coded_dataset.csv` was created as a partially filled coding file. Metadata and quality scores are included, while coding fields should be completed using the manuscript coding framework.
- `screening/quality_assessment_scores.csv` contains the QA1–QA5 scores and total quality score.
- `search_strategy/first_collection.ris` is the available RIS file for search/screening evidence.
- `scripts/rigorous_screening.py` is the available screening script and should be kept in the `scripts/` folder.

## Important note

The `coded_dataset.csv` is not yet fully complete. Columns such as integration pattern, application domain, maturity level, validation strategy, and reproducibility status still need to be coded based on the paper content, abstracts, or existing coding matrix.
