# Triadic Convergence of AI, Blockchain, and Quantum Technologies: A Systematic Literature Review

This repository contains the supporting materials for the systematic literature review (SLR) on the convergence of Artificial Intelligence (AI), Blockchain (BC), and Quantum Computing (QC). It supports transparency, reproducibility, and reuse of the search strategy, screening workflow, coded dataset, analysis scripts, figures, and supplementary materials.

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

## Screening Workflow

The SLR used a PRISMA-style multi-stage screening process. Bibliographic records exported in `.ris` format were first categorized according to the presence of the three core technology pillars: AI, blockchain, and quantum computing. Records with strong triadic relevance were retained, two-pillar records were refined, and irrelevant or noisy records were excluded.

The screening workflow consisted of:

1. **Stage 1: Categorical screening**  
   Records were classified as `include`, `maybe`, or `exclude` based on whether they contained three, two, or fewer relevant technology pillars.

2. **Stage 2: Maybe-set refinement**  
   Two-pillar records were rechecked for meaningful inter-pillar synergy, especially AI–QC and AI–BC relationships.

3. **Stage 3: Rigorous SLR screening**  
   Candidate records were screened using inclusion/exclusion rules, date limits, literature-type filters, and domain-specific noise filters.

4. **Full-text eligibility and quality assessment**  
   Final candidate papers were manually reviewed and scored using a structured quality assessment rubric before inclusion in the final synthesis.

<p align="center">
  <img src="outputs/figures/PRISMA%20flowchart%20of%20the%20systematic%20literature%20process.png" width="760"/>
</p>

---

## Screening Criteria

The screening process applied formal exclusion and inclusion checks, including:

- publication period eligibility
- exclusion of editorials, letters, newsletters, and non-research records
- exclusion of secondary studies where required by the review protocol
- exclusion of unrelated quantum physics/materials papers without computational relevance
- exclusion of cryptocurrency price speculation or market forecasting papers
- confirmation of AI, blockchain, and quantum relevance
- full-text review for vague abstracts or unclear AI methodology

The main screening outputs include:

```text
final_screened_papers.csv
final_include.ris
final_maybe.ris
final_exclude.ris
quality_assessment_scores.csv
quality_assessment_rubric.md
```

The file `screening/quality_assessment_scores.csv` contains the study-level quality assessment scores used to support final inclusion decisions. It records the paper identifier, authors, year, title, individual QA criterion scores, and total quality score. This file is included to improve transparency and traceability of the screening process. It should be interpreted as quality assessment evidence, not as the full analytical coding dataset. The full coding matrix is provided separately as `data/coded_dataset.csv`.


---

## Quality Assessment

The final included studies were assessed using a structured quality assessment process. The scoring considered relevance to AI–BC–QC convergence, methodological clarity, technical depth, validation evidence, and contribution to the review objectives.

<p align="center">
  <img src="outputs/figures/Quality%20score%20distribution%20of%20the%20publications.png" width="760"/>
</p>

---

## Maturity and Research Trajectory

The review examines how AI–BC–QC research is progressing from conceptual and simulation-based studies toward more mature, interoperable, and deployment-oriented systems.

<p align="center">
  <img src="outputs/figures/Evolution%20toward%20scalable%20and%20interoperable%20triadic%20systems.png" width="760"/>
</p>

<p align="center">
  <img src="outputs/figures/Maturity%20gap%20between%20prototype%20validation%20and%20real-world%20deployment.png" width="760"/>
</p>

---

## Repository Structure

```text
AI-BC-QC-SLR/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
│
├── search_strategy/
│   ├── database_search_strings.xlsx
│   ├── prisma_identification_summary.csv
│   ├── search_log.xlsx
│   └── first_collection.ris
│
├── screening/
│   ├── final_screened_papers.csv
│   ├── final_include.ris
│   ├── final_maybe.ris
│   ├── final_exclude.ris
│   ├── quality_assessment_scores.csv
│   └── quality_assessment_rubric.md
│
├── data/
│   ├── included_studies_metadata.csv
│   ├── bibliometric_dataset.csv
│   ├── coded_dataset.csv
│   ├── coded_dataset_template.csv
│   └── keyword_normalization_dictionary.csv
│
├── coding_framework/
│   ├── integration_taxonomy.md
│   ├── coding_examples.xlsx
│   └── variable_dictionary.xlsx
│
├── scripts/
│   ├── screening_script.py
│   ├── refine_maybe.py
│   ├── rigorous_screening.py
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

The repository includes cleaned metadata, coded review data, bibliometric data, keyword normalization records, screening records, and supplementary coding materials. These files support replication of descriptive, bibliometric, maturity, validation, and reproducibility analyses.

Copyrighted full-text articles are not included. Only metadata, review-derived coding outputs, screening records, and supplementary materials are provided.

---

## Reproducibility

Install the required packages and run the analysis scripts:

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

To run the screening pipeline:

```bash
python scripts/screening_script.py
python scripts/refine_maybe.py
python scripts/rigorous_screening.py
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
- search strategy and RIS screening files
- quality assessment rubric and study-level QA scores
- AI–BC–QC integration taxonomy
- coded dataset of included studies
- publication trend analysis
- integration pattern distribution
- application domain mapping
- technological maturity assessment
- validation and reproducibility assessment
- supplementary coding and quality assessment materials

---


## Authors

- Yahaya Saidu  
- Shuhaida Mohamed Shuhidan  
- Shehu Lukman Ayinla  
- Isiaka Shuaibu  
- Dahiru Adamu Aliyu  

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

**Corresponding Contact Person:**  
Saidu Yahaya  
Email: yahayasaidu17@gmail.com

For questions regarding the dataset, screening workflow, coding framework, or reproducibility materials, please contact the repository maintainer.

