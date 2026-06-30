# Discovery Quality and Mediation

This project studies causal metrics for discovery quality in recommendation and content discovery systems using KuaiRec. The workflow asks whether broad discovery exposure creates longer-term user value directly, indirectly through satisfaction depth, or both.

## What You Will Build

You will build a mediation analysis workflow for discovery quality. The project constructs exposure, mediator, and outcome metrics from logged viewing behavior, validates the metrics, states mediation assumptions, estimates direct and indirect effects, and compares classical, SEM-style, and machine-learning mediation approaches.

## How To Use This Project

Start with notebook `01` for the discovery-quality problem setup and data construction. Notebook `02` builds and validates the metrics. Notebook `03` states the mediation estimands and assumptions. The later notebooks estimate direct, indirect, and total effects, run robustness checks, and add advanced mediation models.

The final notebook builds report figures, tables, and writeup files. It is useful for artifacts, while notebooks `01` through `06` provide the public analysis sequence.

## Data Source And Scope

The project uses KuaiRec watch behavior and user-video interaction logs. The data are reorganized into user-day records with discovery-breadth exposure, satisfaction-depth mediators, quality-adjusted discovery metrics, shallow-click-pressure checks, and future engagement outcomes. The design is observational, so the project emphasizes metric validity, mediator assumptions, overlap, robustness, and sensitivity.

## Notebook Sequence

- [01 Discovery quality problem setup and EDA](01_discovery_quality_problem_setup_eda.ipynb)
- [02 Metric construction and validation](02_metric_construction_and_validation.ipynb)
- [03 Mediation estimands and assumptions](03_mediation_estimands_and_assumptions.ipynb)
- [04 Direct, indirect, and total effects](04_direct_indirect_total_effects.ipynb)
- [05 Robustness and sensitivity](05_robustness_and_sensitivity.ipynb)
- [06 Advanced SEM and ML mediation](06_advanced_sem_and_ml_mediation.ipynb)

## Artifact Notebook

- [07 Final report and figures](07_final_report_and_figures.ipynb)

This notebook assembles final figures, tables, and writeup artifacts:

- [final project summary](writeup/final_project_summary.md)
- [artifact index](writeup/artifact_index.csv)
- [tables](writeup/tables/)
- [figures](writeup/figures/)

## Key Interpretation

Short-term clicks can miss the quality of discovery. This project separates the total effect of broader discovery exposure into direct and mediated pathways, so the resulting metric story can distinguish immediate response from satisfaction-linked future value.

## Verified References And Data Links

- Gao, C., Li, S., Lei, W., Chen, J., Li, B., Jiang, P., He, X., Mao, J., & Chua, T.-S. (2022). KuaiRec: A fully-observed dataset and insights for evaluating recommender systems. *CIKM 2022*. [https://doi.org/10.1145/3511808.3557220](https://doi.org/10.1145/3511808.3557220), [arXiv:2202.10842](https://arxiv.org/abs/2202.10842), and [dataset site](https://kuairec.com/).
