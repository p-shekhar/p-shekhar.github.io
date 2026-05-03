# Learner And Tuning Report Template

## Estimand
- Treatment:
- Outcome:
- Control set:
- Target population:
- Identification assumptions:

## Nuisance Learners
- Primary `ml_l` learner:
- Primary `ml_m` learner:
- Reason for primary learner choice:
- Alternative learners checked:

## Preprocessing
- Numeric controls:
- Encoded categorical controls:
- Excluded columns:
- Pipeline steps:

## Cross-Fitting And Tuning
- Number of folds:
- Repeated sample splitting:
- Tuning method:
- Tuning score:
- Search budget:
- Search space summary:

## Diagnostics
- Outcome nuisance RMSE:
- Treatment nuisance RMSE:
- Estimate stability across learners:
- Runtime considerations:

## Final Estimate
- Point estimate:
- Standard error:
- Confidence interval:
- Main caveats: