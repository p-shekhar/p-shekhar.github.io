# Interference and Spillover Effects

This folder contains notebooks for studying interference in recommendation and content discovery systems.

The central causal issue is that promoting one item can affect the exposure and outcomes of other items. This violates the standard no-interference assumption behind many causal estimators, because an item's outcome may depend not only on its own treatment but also on how other competing items were promoted.

Core causal question:

> How does promoting one item affect both that item and nearby competing items in the recommendation surface?

Why this matters:

- A promoted item may gain clicks or watch time by taking attention away from substitutes.
- Standard item-level ATE estimates can overstate product value if they ignore displacement.
- A ranking or recommendation change should be evaluated at the slate, cluster, or market level when units compete for limited attention.

Planned methods:

- Multi-item exposure simulation
- Cluster-level treatment assignment
- Spillover feature construction
- Direct, indirect, and total effect decomposition
- Exposure models for partial interference

Candidate dataset:

- MovieLens with simulated recommendation slates and promotion assignments

Suggested notebook sequence:

- `01_movielens_interference_setup_eda.ipynb`
- `02_spillover_exposure_mapping.ipynb`
- `03_cluster_randomized_estimators.ipynb`
- `04_direct_indirect_total_effects.ipynb`
- `05_advanced_spillover_models.ipynb`
- `06_sensitivity_and_final_report.ipynb`
