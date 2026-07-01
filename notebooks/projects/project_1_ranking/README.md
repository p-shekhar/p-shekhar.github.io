# Ranking Position and Incremental Click Lift

This project studies how ranking position relates to click outcomes in MIND news recommendation impression logs. The treatment is top-3 exposure, the outcome is click-through, and the adjustment set uses observed user history, item metadata, slate size, time, and exposure features.

## What You Will Build

You will build an end-to-end causal ranking audit. The workflow starts with logged recommendation data, turns top-rank exposure into a causal treatment, checks whether the treated and comparison impressions are comparable, estimates adjusted effects, studies segment-level variation, and converts the evidence into experiment-prioritization guidance.

## How To Use This Project

Read the notebooks in sequence. The first notebook explains the MIND impression data and defines the ranking treatment. The next notebooks add propensity modeling, IPW, doubly robust estimation, heterogeneous effects, policy simulation, and sensitivity analysis. The LightGBM and EconML notebooks show how modern nuisance modeling changes the evidence.

Use notebooks `01` through `08` as the public analytic sequence. Generated figures, tables, and snippets live in the project writeup folder when they are needed for summaries.

## Data Source And Scope

The analysis uses MIND news recommendation impression logs. MIND was released for news recommendation research and contains user histories, impression slates, clicked labels, and news metadata. In this project, the logs are used to study whether top-3 placement is associated with incremental click lift after adjustment for observed features. The data are observational, so the estimates should be read as design evidence for future online validation.

## Notebook Sequence

- [01 EDA and treatment definition](01_eda_mind.ipynb)
- [02 Propensity modeling and IPW](02_propensity_ipw.ipynb)
- [03 Doubly robust estimation](03_doubly_robust.ipynb)
- [04 Heterogeneous effects](04_heterogeneous_effects.ipynb)
- [05 Policy simulation](05_policy_simulation.ipynb)
- [06 Sensitivity and limitations](06_sensitivity_and_limitations.ipynb)
- [07 ML nuisance models](07_ml_nuisance_models.ipynb)
- [08 EconML causal ML estimators](08_econml_causal_ml.ipynb)


## Key Interpretation

The large naive top-3 click lift fades after adjustment. The final LightGBM AIPW estimate is slightly negative and statistically uncertain. Segment and policy simulations are therefore best used to prioritize experiments and identify where ranking-position interventions deserve more careful testing.

## Verified References And Data Links

- Wu, F., Qiao, Y., Chen, J. H., Wu, C., Qi, T., Lian, J., Liu, D., Xie, X., Gao, J., Wu, W., & Zhou, M. (2020). MIND: A large-scale dataset for news recommendation. *ACL 2020*. [ACL Anthology](https://aclanthology.org/2020.acl-main.331/) and [dataset site](https://msnews.github.io/).
