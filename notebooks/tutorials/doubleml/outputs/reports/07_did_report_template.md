# Difference-In-Differences DoubleML Report Template

## Question

Estimate the post-period effect for units in the treated group using DID designs with flexible nuisance adjustment.

## Panel DID Result

The preferred panel estimate is the observational `DoubleMLDID` model with gradient boosting nuisance learners.

- Estimate: 1.1713
- Standard error: 0.0186
- 95 percent CI: [1.1349, 1.2077]
- Synthetic true ATT: 1.1606

## Repeated Cross-Section DID Result

The preferred repeated cross-section estimate is the observational `DoubleMLDIDCS` model with gradient boosting nuisance learners.

- Estimate: 1.0958
- Standard error: 0.0415
- 95 percent CI: [1.0143, 1.1772]
- Synthetic true ATT: 1.1592

## Identification Assumptions

The estimates rely on conditional parallel trends: after conditioning on observed pre-treatment covariates, treated and control groups would have had comparable untreated trends. The estimates also require overlap, stable measurement, and no hidden group-specific shocks aligned with treatment timing.

## Diagnostics To Include

- Covariate balance by treated group.
- Propensity overlap plots.
- Raw DID versus adjusted DID comparison.
- Placebo pre-period check when historical outcomes are available.
- Stress test or sensitivity discussion for hidden trend violations.
- Clear statement of the target population.