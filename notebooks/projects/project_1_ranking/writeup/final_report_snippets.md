# Final Report Snippets

## Executive Summary

This project estimates the causal effect of ranking position on user clicks using MIND impression logs. The treatment is top-3 exposure, the outcome is click-through, and the adjustment set includes user-history, item metadata, slate-size, time, and exposure features.

The naive top-3 lift in the final modeling sample is 0.0630. After cross-fitted LightGBM AIPW adjustment, the estimated lift is -0.0049 with an approximate 95% interval [-0.0113, 0.0014].

## Methodology

The analysis starts with descriptive CTR-by-rank curves, then estimates adjusted treatment effects using propensity modeling, IPW, doubly robust AIPW, ML nuisance models, EconML causal ML estimators, heterogeneous treatment effect summaries, policy simulation, and sensitivity checks.

## Key Finding

Top-3 ranking exposure is associated with higher click probability after adjustment for observed confounders. Segment-level analysis suggests that the incremental value of top placement is not uniform across content and context segments.

## Policy Implication

The best offline policy simulation allocates a limited promotion budget by `subcategory` using `aipw_lift` and estimates 112.43 incremental clicks in the modeling sample. This should be interpreted as prioritization for experimentation, not a guaranteed production effect.

## Limitations

The estimates are observational and depend on no unobserved confounding, reasonable overlap, and appropriate nuisance models. MIND contains clicks, not long-term satisfaction or retention. A production system should validate ranking-policy changes through online experiments or randomized exploration traffic.

## Next Steps

1. Validate candidate policy changes with online experiments.
2. Replace public-data proxies with production ranker scores, item freshness, and richer user features.
3. Extend the outcome from clicks to downstream satisfaction or retention.
4. Use slate-aware methods to account for displacement and interference among items.
