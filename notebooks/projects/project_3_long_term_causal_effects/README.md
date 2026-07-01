# Long-Term Effects in Recommendation Systems

This project studies long-term causal effects in recommendation logs using KuaiRec. The goal is to estimate whether short-term recommendation exposure affects later user outcomes such as retention, repeat engagement, or sustained watch behavior.

## What You Will Build

You will build a sequential causal workflow for recommendation exposure. The project defines user-day outcomes, explains time-varying confounding, estimates treatment histories with propensity models, then compares marginal structural models, g-computation, and doubly robust approaches.

## How To Use This Project

Read notebook `01` for the KuaiRec sequence structure and panel construction. Notebook `02` defines the long-term estimand. The middle notebooks cover time-varying confounding, stabilized weights, marginal structural models, and g-computation. Notebook `06` adds doubly robust and heterogeneous-effect analysis.

Use notebooks `01` through `06` as the public analytic sequence, ending with doubly robust estimation and heterogeneity analysis.

## Data Source And Scope

The project uses KuaiRec interaction logs. KuaiRec is valuable for recommendation research because it contains dense user-video observations and supports more complete evaluation than sparse observational logs. Here it is reorganized into active user-day records so the analysis can study short-term exposure and later engagement. The design remains observational, so the project emphasizes assumptions, weighting diagnostics, and sensitivity checks.

## Notebook Sequence

- [01 KuaiRec sequence EDA](01_kuairec_sequence_eda.ipynb)
- [02 Long-term outcome definition](02_long_term_outcome_definition.ipynb)
- [03 Time-varying confounding and propensity weights](03_time_varying_confounding_and_propensity.ipynb)
- [04 Marginal structural model](04_marginal_structural_model.ipynb)
- [05 G-computation](05_g_computation.ipynb)
- [06 Doubly robust heterogeneous effects](06_doubly_robust_heterogeneous_effects.ipynb)


## Key Interpretation

Recommendation effects can evolve over time because exposure today changes tomorrow's behavior, and tomorrow's behavior changes later exposure. The project makes that feedback structure explicit so long-term engagement claims are tied to treatment histories and same-session response is only one part of the evidence.

## Verified References And Data Links

- Gao, C., Li, S., Lei, W., Chen, J., Li, B., Jiang, P., He, X., Mao, J., & Chua, T.-S. (2022). KuaiRec: A fully-observed dataset and insights for evaluating recommender systems. *CIKM 2022*. [https://doi.org/10.1145/3511808.3557220](https://doi.org/10.1145/3511808.3557220), [arXiv:2202.10842](https://arxiv.org/abs/2202.10842), and [dataset site](https://kuairec.com/).
