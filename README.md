# Triadic Convergence of AI, Blockchain, and Quantum Technologies: A Systematic Literature Review

This repository contains the supporting materials for the systematic literature review (SLR) on the convergence of Artificial Intelligence (AI), Blockchain (BC), and Quantum Computing (QC). It is intended to support transparency, reproducibility, and reuse of the review workflow, coded dataset, analysis scripts, figures, and supplementary materials.

---

## Paper Overview

The study examines how AI, blockchain, and quantum technologies are integrated in emerging digital systems. It focuses on integration patterns, application domains, functional technology roles, maturity levels, validation rigor, and reproducibility evidence.

<p align="center">
  <img src="outputs/figures/Triadic%20Synergy%20of%20AI-BC-QC.png" width="760"/>
</p>

---

## Research Questions

1. What integration patterns characterize AI–Blockchain–Quantum convergence?
2. What application domains and problem classes are most represented?
3. What functional roles do AI, blockchain, and quantum technologies play in integrated systems?
4. What is the technological maturity level of existing AI–BC–QC studies?
5. How rigorous are the validation strategies and reproducibility practices?

---

## Integration Taxonomy

The review classifies studies into three main integration patterns:

- **T1:** Quantum-enhanced AI for blockchain optimization  
- **T2:** Blockchain-enabled governance for AI–quantum systems  
- **T3:** AI-supported quantum-safe blockchain and post-quantum resilience  

---

## Methodological Workflow

The review followed a PRISMA-style workflow covering database searching, deduplication, title and abstract screening, full-text eligibility assessment, quality assessment, coding, and synthesis.

<p align="center">
  <img src="outputs/figures/PRISMA%20flowchart%20of%20the%20systematic%20literature%20process.png" width="760"/>
</p>

---

## Maturity and Research Trajectory

The review also examines how AI–BC–QC research is progressing from conceptual and simulation-based studies toward more mature, interoperable, and deployment-oriented systems.

<p align="center">
  <img src="outputs/figures/Evolution%20toward%20scalable%20and%20interoperable%20triadic%20systems.png" width="760"/>
</p>

<p align="center">
  <img src="outputs/figures/Maturity%20gap%20between%20prototype%20validation%20and%20real-world%20deployment.png" width="760"/>
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

The repository includes cleaned metadata, coded review data, bibliometric data, keyword normalization records, and supplementary coding materials. These files support replication of descriptive, bibliometric, maturity, validation, and reproducibility analyses.

Copyrighted full-text articles are not included. Only metadata, review-derived coding outputs, and supplementary materials are provided.

---

## Reproducibility

To reproduce the analysis, install the required packages and run the analysis scripts:

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

Further instructions are provided in:

```text
docs/how_to_run_analysis.md
docs/reproducibility_guide.md
```

---

## Key Outputs

The repository provides:

- PRISMA screening record
- AI–BC–QC integration taxonomy
- coded dataset of included studies
- publication trend analysis
- integration pattern distribution
- application domain mapping
- technological maturity assessment
- validation and reproducibility assessment
- supplementary coding and quality assessment materials

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
