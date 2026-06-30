# Technical Summary Bullets: Interference and Spillover Effects

- Built an end-to-end causal inference workflow for recommendation slate interference using MovieLens 32M, simulated randomized promotions, and slate-level outcome construction.
- Estimated direct, spillover, and total effects under item competition; found a +171.6 focal-click gain but a -307.8 net slate-click change per 1,000 promoted slates after competitor displacement.
- Implemented slate-clustered estimators, bootstrap checks, direct/indirect/total decomposition, and sensitivity analyses across same-cluster, displaced-item, and all-non-focal spillover definitions.
- Trained LightGBM and XGBoost outcome models for conditional net-effect prediction, compared model-assisted AIPW against randomized estimates, and evaluated targeted promotion policies.
