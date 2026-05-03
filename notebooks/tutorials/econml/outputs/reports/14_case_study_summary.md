# End-To-End EconML Case Study Summary

## Decision

Estimate which users should receive a proactive onboarding bundle when treatment cost is `0.18` outcome units per treated user.

## Main Result

The strongest held-out policy by true net value is **LinearDML: effect > cost**.

- Treatment rate: `53.9%`
- True net value per user: `0.1709`
- Precision among treated users: `82.9%`

The estimator with the lowest held-out CATE RMSE is **LinearDML** with RMSE `0.2719`.

## Evidence Used

The recommendation uses covariate balance checks, overlap diagnostics, nuisance-model diagnostics, held-out CATE recovery, segment bias checks, policy value comparisons, budget curves, and bootstrap policy intervals.

## Caveats

This is a teaching dataset with known ground truth. In real observational work, hidden true CATE would not be available, so the workflow would need domain review of confounders, sensitivity analysis, temporal validation, and ideally an experiment for policy confirmation.