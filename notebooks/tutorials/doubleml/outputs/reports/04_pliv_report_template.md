# PLIV Effect Estimate Report Template

## Causal Question
Estimate the effect of `exposure_intensity` on `weekly_value` using `encouragement_score` as an instrument.

## Design Logic
The concern is that unobserved factors may affect both treatment and outcome. The instrument is intended to shift treatment while affecting the outcome only through treatment after adjusting for observed controls.

## Estimator
The main estimator is `DoubleMLPLIV` with the partialling-out score, five-fold cross-fitting, and histogram gradient-boosting nuisance learners.

## Main Estimate
- Estimated effect: 1.9293
- Standard error: 0.0475
- 95 percent confidence interval: [1.8363, 2.0224]

## First Stage
- Residualized first-stage slope: 0.7581
- Residualized first-stage F statistic: 575.44
- Residual instrument-treatment correlation: 0.4327

## Diagnostics Included
- OLS, naive IV, residualized IV, oracle IV, and DoubleML PLIV comparisons.
- First-stage relevance screen.
- Manual cross-fitted PLIV calculation.
- Nuisance learner RMSE checks.
- Residual distribution and score contribution checks.
- Score variant comparison.
- Bootstrap confidence interval.
- Repeated sample-splitting stability.
- Weak-instrument and exclusion-violation stress tests.

## Required Assumptions
The estimate relies on instrument relevance, exclusion, and conditional independence after controls. Relevance is screened in the data. Exclusion and conditional independence require design evidence and cannot be established by DoubleML alone.