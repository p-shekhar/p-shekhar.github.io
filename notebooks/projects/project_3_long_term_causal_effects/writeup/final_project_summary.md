# Final Summary: Long-Term Causal Effects in Recommendation Systems

## Question

This project estimates whether a high-watch-exposure day in KuaiRec changes a user's future 7-day engagement. The target outcome is future 7-day interaction volume.

## Why This Matters

Short-term recommendation metrics such as watch ratio or completion can look attractive while failing to improve longer-term engagement. This project treats the problem as a sequential causal inference task, where prior user behavior affects today's exposure and future behavior.

## Methods

The project uses three complementary causal strategies:

- Marginal structural model with stabilized inverse probability weights.
- G-computation with linear and LightGBM outcome models.
- Doubly robust AIPW estimation with segment-level heterogeneity diagnostics.

## Main Result

The average effect is small and uncertain across estimators:

- MSM estimate: -2.69 future interactions, 95% CI [-12.27, 5.73].
- LightGBM g-computation estimate: 0.04, 95% CI [-0.64, 1.87].
- Doubly robust AIPW estimate: 1.09, 95% CI [-7.34, 12.02].

The evidence does not support claiming a clear positive average effect of high-watch-exposure days on future 7-day interaction volume.

## Sensitivity and Heterogeneity

Weighting improved observed covariate balance, but overlap was imperfect and effective sample size dropped after weighting. Secondary outcomes suggest the treatment may relate differently to watch-hours metrics than to interaction volume. Heterogeneity diagnostics point to recent engagement and recent watch-quality history as useful stratification variables for future experiments.

## Product Takeaway

High-watch exposure should not be treated as automatically beneficial for longer-term interaction volume. It may still be a useful short-term satisfaction signal, but it should be validated against long-term metrics and tested online with stratification by recent user history.

## Limitations

This is an observational analysis. The estimates rely on sequential ignorability, observed history adjustment, and constructed treatment definitions. The results are best used to prioritize and design online experiments, not to replace them.
