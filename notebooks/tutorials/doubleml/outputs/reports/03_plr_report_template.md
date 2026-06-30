# PLR Effect Estimate Report Template

## Causal Question
Estimate the constant-slope effect of `exposure_intensity` on `weekly_value`, adjusting for pre-treatment controls.

## Estimator
The main estimator is `DoubleMLPLR` with the partialling-out score, five-fold cross-fitting, and histogram gradient-boosting nuisance learners for `ml_l` and `ml_m`.

## Main Estimate
- Estimated effect: 1.8036
- Standard error: 0.0206
- 95 percent confidence interval: [1.7633, 1.8439]

## Diagnostics Included
- Baseline comparisons against naive and linearly adjusted OLS.
- Manual cross-fitted residualization.
- Nuisance learner RMSE checks.
- Residual distribution checks.
- Orthogonal score contribution checks.
- Repeated sample-splitting stability.
- Bootstrap confidence interval.
- Small illustrative sensitivity analysis.

## Required Assumptions
The PLR estimate relies on observed-control identification: after adjusting for the selected pre-treatment controls, residual treatment variation is as-good-as-random for the outcome. The model does not solve omitted confounding or bad-control problems by itself.