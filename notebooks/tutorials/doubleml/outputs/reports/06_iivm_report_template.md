# IIVM Local Effect Estimate Report Template

## Causal Question
Estimate the local effect of `feature_exposure` on `weekly_value` for units whose treatment status is shifted by `encouragement`.

## Target
The target is LATE, not the full-population ATE. The estimate applies to the instrument-responsive margin under the IV assumptions.

## Main Estimate
- Estimated local effect: 1.1618
- Standard error: 0.0836
- 95 percent confidence interval: [0.9979, 1.3257]

## First Stage
- Mean estimated first stage: 0.5122

## Estimator
The main estimator is `DoubleMLIIVM` with five-fold cross-fitting, histogram gradient-boosted outcome nuisance models, and histogram gradient-boosted classifiers for instrument and treatment take-up nuisance models.

## Diagnostics Included
- Direct treatment comparisons, raw Wald, residualized Wald, oracle ratio, manual cross-fitted IIVM, and DoubleML IIVM comparisons.
- Compliance-type summary for the synthetic example data.
- Instrument overlap diagnostics.
- First-stage distribution diagnostics.
- Nuisance learner losses and prediction checks.
- Orthogonal score contribution checks.
- Bootstrap confidence interval.
- Repeated sample-splitting stability.
- Subgroup assumption variants.
- Weak first-stage and exclusion-violation stress tests.

## Required Assumptions
The local effect is causal only if the instrument is relevant, has no direct effect on the outcome, is conditionally independent after controls, satisfies monotonicity, and has adequate overlap. DoubleML estimates the score under these assumptions; it does not establish them.