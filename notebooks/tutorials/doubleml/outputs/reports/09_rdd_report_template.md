# Regression Discontinuity DoubleML Report Template

## Question

Estimate the local treatment effect at a cutoff in the running variable.

## Sharp RDD Result

The preferred sharp estimate uses `RDFlex` with gradient boosting nuisance adjustment and the robust interval.

- Estimate: 1.3002
- 95 percent CI: [1.0932, 1.5071]
- Synthetic true cutoff effect: 1.2000

## Fuzzy RDD Result

The preferred fuzzy estimate uses `RDFlex` with outcome and treatment nuisance adjustment.

- Estimate: 1.0301
- 95 percent CI: [0.7515, 1.3087]
- Synthetic true local effect: 1.0000

## Identification Assumptions

The design requires potential outcomes to be smooth through the cutoff in the absence of treatment. It also requires no precise manipulation of the running variable around the cutoff. For fuzzy RDD, crossing the cutoff must create a meaningful first-stage change in treatment probability.

## Diagnostics To Include

- Running-variable density around the cutoff.
- Binned outcome plot with the cutoff marked.
- Local support counts by bandwidth.
- Covariate continuity checks.
- Bandwidth sensitivity.
- First-stage plot for fuzzy RDD.

## Scope

This is a local estimate at the cutoff. It should not be generalized to units far from the cutoff without an additional argument.