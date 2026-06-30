# Off-Policy Evaluation for Recommendation Policies

This project evaluates alternative recommendation policies offline with logged bandit data from the Open Bandit Dataset. The core question is how a candidate policy might have performed if it had been deployed under the same user-context distribution.

## What You Will Build

You will build a complete off-policy evaluation workflow. The project moves from behavior-policy diagnostics to IPS, SNIPS, direct method, doubly robust estimation, clipping sensitivity, and contextual policy learning. The output is a launch-readiness view of candidate policies, not a single score detached from support and uncertainty.

## How To Use This Project

Start with the data audit in notebook `01`, then move through behavior-policy propensities, importance-weighted estimators, doubly robust estimation, and sensitivity analysis. Notebook `06` adds policy learning with reward models and compares candidate recommendation policies under the OPE diagnostics developed earlier.

The final notebook is an artifact builder for figures, tables, and summary files.

## Data Source And Scope

The project uses the Open Bandit Dataset, with emphasis on the `random/men` campaign. This setting is useful for OPE because the data include logged actions, rewards, context features, and known behavior-policy propensities from a real fashion e-commerce recommendation setting. The analysis uses click reward as the short-term outcome, so the interpretation is about immediate response under logged recommendation policies.

## Notebook Sequence

- [01 Open Bandit EDA](01_open_bandit_eda.ipynb)
- [02 Behavior policy and propensity diagnostics](02_behavior_policy_and_propensities.ipynb)
- [03 IPS and SNIPS policy evaluation](03_ips_and_snips.ipynb)
- [04 Doubly robust OPE](04_doubly_robust_ope.ipynb)
- [05 Policy comparison and sensitivity](05_policy_comparison_and_sensitivity.ipynb)
- [06 Contextual policy learning](06_contextual_policy_learning.ipynb)

## Artifact Notebook

- [07 Final report and artifacts](07_final_report_and_artifacts.ipynb)

This notebook generates final figures, tables, and project artifacts. The public teaching sequence should point readers first to notebooks `01` through `06`.

## Key Interpretation

Offline policy value estimates are meaningful only when support, propensity quality, reward-model diagnostics, and sensitivity checks agree. The project shows how a policy with appealing estimated reward can still require caution when effective sample size is low or estimates depend heavily on clipped high-weight observations.

## Verified References And Data Links

- Saito, Y., Aihara, S., Matsutani, M., & Narita, Y. (2021). Open Bandit Dataset and Pipeline: Towards realistic and reproducible off-policy evaluation. [arXiv:2008.07146](https://arxiv.org/abs/2008.07146) and [OBP GitHub repository](https://github.com/st-tech/zr-obp).
