# QC-AI-BC SLR Repository Scripts

This package contains simplified Python scripts for reproducing the main analytical outputs of the AI–Blockchain–Quantum Computing SLR repository.

## Recommended use

Place the `scripts/` folder in the root of your GitHub repository, then install dependencies:

```bash
pip install -r requirements.txt
```

Run all scripts at once:

```bash
python scripts/generate_figures.py
```

Or run individual scripts:

```bash
python scripts/preprocess_metadata.py
python scripts/publication_trend_analysis.py
python scripts/integration_pattern_analysis.py
python scripts/maturity_analysis.py
python scripts/validation_analysis.py
python scripts/reproducibility_analysis.py
```

## Expected input files

The scripts are designed to work with these repository files when available:

```text
data/included_studies_metadata.csv
data/bibliometric_dataset.csv
data/coded_dataset.csv
```

If some columns are missing, the scripts will skip the affected figure and print a clear message instead of stopping the whole workflow.

## Main output folder

Generated figures are saved to:

```text
outputs/figures/
```
