# Off-Policy Evaluation of Recommendation Systems

This folder contains the off-policy evaluation notebooks based on `CausalAI_projects.pdf`.

The project goal is to evaluate a new recommendation policy using logged data from an existing behavior policy. The core causal question is:

> How would an alternative recommendation policy have performed if it had been deployed?

Planned methods:

- Inverse Propensity Scoring
- Self-Normalized IPS
- Doubly Robust policy value estimation

Candidate datasets:

- Open Bandit Dataset
- KuaiRec

Suggested notebook sequence:

- `01_open_bandit_eda.ipynb`
- `02_behavior_policy_and_propensities.ipynb`
- `03_ips_and_snips.ipynb`
- `04_doubly_robust_ope.ipynb`
- `05_policy_comparison_and_sensitivity.ipynb`
- `06_contextual_policy_learning.ipynb`
- `07_final_report_and_artifacts.ipynb`
