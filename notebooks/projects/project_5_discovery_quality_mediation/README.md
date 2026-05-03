# Discovery Quality Mediation

This folder contains notebooks for studying causal metrics for discovery quality in recommendation and content discovery systems. The analysis uses KuaiRec behavior logs to ask whether broad discovery exposure creates longer-term user value directly, indirectly through satisfaction depth, or both.

The central causal issue is that short-term click-through rate does not necessarily measure user satisfaction or longer-term value. A recommendation can increase clicks while failing to improve satisfaction, repeat engagement, or retention. This workflow studies the pathway:

> Discovery exposure -> Satisfaction depth -> Future user value

Core causal question:

> How much of the effect of broader discovery exposure on longer-term user value flows through same-day satisfaction depth?

Why this matters:

- CTR can reward curiosity, miscalibration, or low-quality engagement.
- Satisfaction-like signals may mediate the relationship between exposure and retention.
- Product metrics should distinguish direct effects from indirect effects through clicks or satisfaction.
- A good discovery metric should predict durable user value, not only immediate response.

Planned methods:

- Discovery metric construction from logged viewing behavior
- Mediation analysis with direct, indirect, and total effect decomposition
- Confounding diagnostics and overlap checks
- Robustness checks across treatment thresholds, mediator definitions, and model specifications
- Structural equation modeling style path analysis
- Cross-fitted machine-learning mediation models
- Final report tables, figures, resume bullets, and artifact index

Dataset:

- KuaiRec, using watch behavior, completion/watch-ratio style satisfaction signals, discovery-breadth exposure, and future engagement outcomes

Notebook sequence:

- `01_discovery_quality_problem_setup_eda.ipynb`
- `02_metric_construction_and_validation.ipynb`
- `03_mediation_estimands_and_assumptions.ipynb`
- `04_direct_indirect_total_effects.ipynb`
- `05_robustness_and_sensitivity.ipynb`
- `06_advanced_sem_and_ml_mediation.ipynb`
- `07_final_report_and_figures.ipynb`

Final writeup artifacts:

- `writeup/final_project_summary.md`
- `writeup/resume_bullets.md`
- `writeup/artifact_index.csv`
- `writeup/tables/`
- `writeup/figures/`
