# EconML Debugging And Reporting Summary

## Recommended Valid Workflow

The strongest valid reference workflow in this teaching run is **Clean DRLearner**.

- Held-out CATE RMSE: `0.2532`
- Held-out CATE correlation: `0.8484`
- Net policy value per user: `0.2813`
- Treatment rate under cost threshold: `63.7%`

## Main Lessons

1. Strong-looking metrics do not fix invalid feature timing.
2. Weak overlap reduces the effective information available for causal estimation.
3. Bad nuisance models can distort both average and heterogeneous effects.
4. Post-treatment controls can change the estimand by blocking part of the treatment pathway.
5. CATE estimates should be reported with calibration, segment checks, policy value, and uncertainty.

## Required Caveats

We use synthetic data with known truth. In real observational analysis, the report must include domain justification for confounders, evidence of overlap, sensitivity to modeling choices, and validation plans before a policy recommendation is treated as decision-ready.