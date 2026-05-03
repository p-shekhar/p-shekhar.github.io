# Long-Term Causal Effects

This folder contains the long-term causal effects notebooks based on `CausalAI_projects.pdf`.

The project goal is to estimate whether short-term recommendation exposure affects longer-term user outcomes such as retention, repeat engagement, or sustained watch behavior.

Core causal question:

> How do sequential recommendation exposures affect future engagement or retention?

Planned methods:

- Marginal Structural Models
- Time-dependent inverse probability weighting
- G-computation
- Doubly robust / AIPW estimation

Candidate datasets:

- KuaiRec
- Sequential logs from MIND

Suggested notebook sequence:

- `01_kuairec_sequence_eda.ipynb`
- `02_long_term_outcome_definition.ipynb`
- `03_time_varying_confounding_and_propensity.ipynb`
- `04_marginal_structural_model.ipynb`
- `05_g_computation.ipynb`
- `06_doubly_robust_heterogeneous_effects.ipynb`
- `07_sensitivity_and_final_report.ipynb`
