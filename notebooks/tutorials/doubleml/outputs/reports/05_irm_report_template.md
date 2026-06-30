# IRM Effect Estimate Report Template

## Causal Question
Estimate the effect of `feature_exposure` on `weekly_value` using observed pre-treatment controls.

## Estimands
Two targets are reported:
- ATE: average effect over the full analysis population.
- ATTE: effect for the treated units under the DoubleML treated-target score.

## Main Estimates
ATE estimate:
- Estimated effect: 0.9843
- Standard error: 0.0537
- 95 percent confidence interval: [0.8790, 1.0897]

ATTE estimate:
- Estimated effect: 1.1023
- Standard error: 0.0571
- 95 percent confidence interval: [0.9905, 1.2141]

## Estimator
The main estimator is `DoubleMLIRM` with five-fold cross-fitting, histogram gradient-boosted outcome models, and a histogram gradient-boosted propensity classifier.

## Diagnostics Included
- Difference-in-means, OLS adjustment, manual IPW, manual AIPW, and DoubleML comparisons.
- Propensity overlap and inverse-propensity weight diagnostics.
- Effective sample size from IPW weights: 2251.7.
- Outcome nuisance and propensity nuisance quality checks.
- Orthogonal score contribution checks.
- Bootstrap confidence intervals.
- Repeated sample-splitting stability.
- Propensity clipping sensitivity.
- Overlap stress test.

## Required Assumptions
The estimates rely on consistency, conditional unconfoundedness given the selected controls, overlap, and no interference. DoubleML improves estimation under these assumptions but does not establish them.