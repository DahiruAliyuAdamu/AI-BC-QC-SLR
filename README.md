# Triadic Convergence of AI, Blockchain, and Quantum Technologies: A Systematic Literature Review

This repository provides the supporting materials for the systematic literature review (SLR) on the convergence of Artificial Intelligence (AI), Blockchain (BC), and Quantum Computing (QC). It is designed to improve transparency, reproducibility, and accessibility of the review process, including search strategy, screening records, coding framework, datasets, analysis scripts, figures, and supplementary materials.

---

## Paper Overview

The study investigates how AI, blockchain, and quantum technologies are being integrated across emerging digital systems. It examines integration patterns, application domains, technological maturity, validation practices, and reproducibility evidence in the AI–BC–QC literature.

The review is structured around three integration patterns:

- **T1:** Quantum-enhanced AI for blockchain optimization  
- **T2:** Blockchain-enabled governance for AI–quantum systems  
- **T3:** AI-supported quantum-safe blockchain and post-quantum resilience  

---

## Research Questions

The review addresses the following research questions:

1. What integration patterns characterize AI–Blockchain–Quantum convergence?
2. What application domains and problem classes are most represented?
3. What functional roles do AI, blockchain, and quantum technologies play in integrated systems?
4. What is the technological maturity level of existing AI–BC–QC studies?
5. How rigorous are the validation strategies and reproducibility practices?

---

## Methodological Workflow

The review followed a PRISMA-style process covering database searching, deduplication, title and abstract screening, full-text eligibility assessment, quality assessment, coding, and synthesis.

<p align="center">
  <img src="outputs/figures/prisma_flow_diagram.png" width="750"/>
</p>

---

## Integration Taxonomy

The review classifies studies into three main AI–BC–QC integration patterns. This taxonomy supports consistent comparison across technical objectives, architectural roles, and maturity levels.

<p align="center">
  <img src="outputs/figures/integration_taxonomy_framework.png" width="750"/>
</p>

---

## Publication Trend

The publication trend highlights the growth of AI–BC–QC research over the review period.

<p align="center">
  <img src="outputs/figures/publication_trend.png" width="750"/>
</p>

---

## Repository Structure

```text
QC-AI-BC-SLR/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
│
├── search_strategy/
│   ├── database_search_strings.xlsx
│   ├── prisma_identification_summary.csv
│   └── search_log.xlsx
│
├── screening/
│   ├── title_abstract_screening.xlsx
│   ├── full_text_screening.xlsx
│   ├── exclusion_reasons.xlsx
│   ├── eligibility_quality_assessment.xlsx
│   └── quality_assessment_rubric.md
│
├── data/
│   ├── included_studies_metadata.csv
│   ├── coded_dataset.csv
│   ├── bibliometric_dataset.csv
│   └── keyword_normalization_dictionary.csv
│
├── coding_framework/
│   ├── integration_taxonomy.md
│   ├── coding_examples.xlsx
│   └── variable_dictionary.xlsx
│
├── scripts/
│   ├── preprocess_metadata.py
│   ├── publication_trend_analysis.py
│   ├── integration_pattern_analysis.py
│   ├── maturity_analysis.py
│   ├── validation_analysis.py
│   ├── reproducibility_analysis.py
│   └── generate_figures.py
│
├── outputs/
│   ├── figures/
│   └── tables/
│
├── supplementary_materials/
│   ├── appendix_full_included_studies.xlsx
│   ├── appendix_coding_matrix.xlsx
│   └── supplementary_methods.pdf
│
└── docs/
    ├── reproducibility_guide.md
    └── how_to_run_analysis.md
```

---

## Data Description

The repository includes cleaned metadata, coded review data, bibliometric data, keyword normalization records, and supplementary coding materials. The datasets support replication of the descriptive, bibliometric, maturity, validation, and reproducibility analyses.

Copyrighted full-text articles are not included. Only metadata, coding outputs, and review-derived materials are provided.

---

## Reproducibility

To reproduce the analysis:

```bash
pip install -r requirements.txt
python scripts/preprocess_metadata.py
python scripts/publication_trend_analysis.py
python scripts/integration_pattern_analysis.py
python scripts/maturity_analysis.py
python scripts/validation_analysis.py
python scripts/reproducibility_analysis.py
python scripts/generate_figures.py
```

Detailed instructions are available in:

```text
docs/how_to_run_analysis.md
docs/reproducibility_guide.md
```

---

## Key Outputs

The main outputs include:

- PRISMA screening diagram
- AI–BC–QC integration taxonomy
- publication trend analysis
- integration pattern distribution
- domain mapping results
- technological maturity assessment
- validation strategy analysis
- reproducibility assessment

---

## Citation

If you use this repository, please cite the associated paper and repository.

```bibtex
@article{AI_BC_QC_SLR,
  title   = {Triadic Convergence of Artificial Intelligence, Blockchain, and Quantum Technologies: A Systematic Literature Review and Research Agenda},
  author  = {Author Names},
  journal = {Journal Name},
  year    = {2026},
  note    = {Repository supporting systematic review materials}
}
```

---

## License

This repository is released for academic and research use. Please see the `LICENSE` file for details.

---

## Contact

For questions about the dataset, coding framework, or reproducibility materials, please contact the corresponding author of the associated paper.
