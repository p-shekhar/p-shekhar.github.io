# IRM Effect Estimate Report Template

## Causal Question
Estimate the effect of `feature_exposure` on `weekly_value` using observed pre-treatment controls.

## Estimands
Two targets are reported:
- ATE: average effect over the full analysis population.
- ATTE: effect for the treated units under the DoubleML treated-target score.

## Main Estimates
ATE estimate:
- Estimated effect: 0.9853
- Standard error: 0.0539
- 95 percent confidence interval: [0.8797, 1.0909]

ATTE estimate:
- Estimated effect: 1.0483
- Standard error: 0.0699
- 95 percent confidence interval: [0.9113, 1.1852]

## Estimator
The main estimator is `DoubleMLIRM` with five-fold cross-fitting, histogram gradient-boosted outcome models, and a histogram gradient-boosted propensity classifier.

## Diagnostics Included
- Difference-in-means, OLS adjustment, manual IPW, manual AIPW, and DoubleML comparisons.
- Propensity overlap and inverse-propensity weight diagnostics.
- Effective sample size from IPW weights: 2225.4.
- Outcome nuisance and propensity nuisance quality checks.
- Orthogonal score contribution checks.
- Bootstrap confidence intervals.
- Repeated sample-splitting stability.
- Propensity clipping sensitivity.
- Overlap stress test.

## Required Assumptions
The estimates rely on consistency, conditional unconfoundedness given the selected controls, overlap, and no interference. DoubleML improves estimation under these assumptions but does not establish them.