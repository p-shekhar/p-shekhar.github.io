# End-To-End DoubleML Case Study Report

## Causal Question
Estimate the average effect of receiving a guided onboarding nudge on next-period user value.

## Estimand
The target estimand is the average treatment effect:

$$
\theta_0 = \mathbb{E}[Y(1) - Y(0)].
$$

## Identification Assumptions
The analysis assumes conditional exchangeability given the documented pre-treatment controls, overlap between treated and untreated users, stable treatment definition, and no interference across users.

## Main DoubleML Specification
- Estimator: `DoubleMLIRM`
- Score: ATE
- Outcome learner: random forest regressor
- Propensity learner: random forest classifier
- Cross-fitting: 5 folds
- Propensity clipping threshold: 0.02

## Main Estimate
- Estimated ATE: 0.4615
- Standard error: 0.0379
- 95% confidence interval: [0.3871, 0.5359]
- Known true ATE in this teaching simulation: 0.4257

## Diagnostics
- Estimated propensity p05 / p95: 0.2088 / 0.7317
- Outcome RMSE under control model: 0.9807
- Outcome RMSE under treated model: 0.9810
- Propensity log loss: 0.4725
- Sample-split estimate SD: 0.0066

## Heterogeneity
The doubly robust signal suggests larger effects for higher-intent users. Treat this as subgroup evidence, not as a fully validated targeting policy.

## Sensitivity
Sensitivity bounds are saved for mild, moderate, and strong hidden-confounding scenarios. These stress tests do not remove hidden-confounding risk; they describe how the estimate would move under specified scenarios.

## Limitations
The analysis remains observational. It can be threatened by missing confounders, bad measurement, outcome leakage, violations of overlap, interference, or changes in the treatment definition.

## Artifact Paths
- Data: `/home/apex/Documents/ranking_sys/notebooks/tutorials/doubleml/outputs/datasets/18_end_to_end_case_study_data.csv`
- Main estimate: `/home/apex/Documents/ranking_sys/notebooks/tutorials/doubleml/outputs/tables/18_main_irm_estimate.csv`
- Learner comparison: `/home/apex/Documents/ranking_sys/notebooks/tutorials/doubleml/outputs/tables/18_learner_family_comparison.csv`
- Segment summary: `/home/apex/Documents/ranking_sys/notebooks/tutorials/doubleml/outputs/tables/18_segment_dr_signal_summary.csv`
- Sensitivity summary: `/home/apex/Documents/ranking_sys/notebooks/tutorials/doubleml/outputs/tables/18_sensitivity_summary.csv`
- Evidence scorecard: `/home/apex/Documents/ranking_sys/notebooks/tutorials/doubleml/outputs/tables/18_evidence_scorecard.csv`
