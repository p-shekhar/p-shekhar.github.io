# Heterogeneous Treatment Effects Report Template

## Causal Question
State the treatment, outcome, population, and time horizon. Explain why an average effect is not enough for the decision.

## Identification Design
Describe the assumptions behind the base DoubleML model: observed confounding adjustment, overlap, and no interference. Note that GATE and CATE summaries inherit these assumptions.

## Base ATE
- Estimated ATE: 0.5297
- Standard error: 0.0499
- 95% confidence interval: [0.4318, 0.6276]

## Pre-Specified GATEs
Report group definitions, group sizes, treatment rates, estimated effects, and confidence intervals. Avoid ranking groups without uncertainty.

## CATE/BLP Summary
List the basis features used for the BLP. Explain that coefficients summarize a projection of the heterogeneous effect signal, not a full structural model of individual treatment effects.

## Subgroup Cautions
Document any exploratory groupings separately from pre-specified groupings. Treat exploratory findings as hypotheses for validation.

## Decision Guidance
Translate the heterogeneity pattern into follow-up experiments, monitoring plans, or product design changes. Avoid direct targeting decisions unless the design and validation are strong enough.
