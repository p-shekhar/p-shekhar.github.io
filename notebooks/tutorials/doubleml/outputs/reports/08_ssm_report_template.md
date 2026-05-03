# Sample Selection DoubleML Report Template

## Question

Estimate the treatment effect for the full target population when the outcome is observed only for selected rows.

## Preferred Missing-At-Random Result

The preferred MAR estimate uses `DoubleMLSSM` with gradient boosting nuisance learners.

- Estimate: 1.0028
- Standard error: 0.0363
- 95 percent CI: [0.9316, 1.0739]
- Synthetic true ATE: 1.0323

## Nonignorable Selection Demonstration

When selection depends on a hidden response factor, a MAR score is not conceptually sufficient. The nonignorable score uses a selection encouragement variable as an exclusion variable.

- Nonignorable estimate: 1.0701
- Standard error: 0.0443
- 95 percent CI: [0.9832, 1.1570]
- Synthetic true ATE: 1.0389

## Assumptions To State

- Treatment assignment is unconfounded after conditioning on observed covariates.
- Outcome observation is missing at random after conditioning on treatment and covariates, unless using the nonignorable score.
- Treatment and selection probabilities have adequate overlap.
- For nonignorable selection, the selection encouragement affects outcome observation and has no direct outcome effect.

## Diagnostics To Include

- Selected versus unselected covariate balance.
- Treatment and selection probability overlap.
- Selected-row baseline estimates versus selection-adjusted estimates.
- Nuisance learner diagnostics.
- Stress test showing how lower outcome visibility affects uncertainty.