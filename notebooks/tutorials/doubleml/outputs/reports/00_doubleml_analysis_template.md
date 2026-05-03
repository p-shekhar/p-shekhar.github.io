# DoubleML Analysis Template

## 1. Causal Question

State the treatment, outcome, target population, and intended estimand.

## 2. Identification Strategy

State the design: unconfoundedness, IV, DID, RDD, sample selection, or another setup. List the assumptions needed for the estimate to be causal.

## 3. Data Roles

List outcome columns, treatment columns, controls, instruments, time variables, cluster variables, sample-selection variables, and excluded variables.

## 4. Nuisance Learners

Document each nuisance learner, its role, preprocessing, tuning approach, and whether tuning was nested safely.

## 5. Cross-Fitting And Resampling

Report folds, repeated splits, random seed, external split logic, and any clustered or temporal split decisions.

## 6. Main Estimate

Report coefficient or effect estimate, standard error, confidence interval, p-value, and estimand meaning.

## 7. Diagnostics

Include nuisance losses, overlap or propensity diagnostics where relevant, sensitivity checks, and split robustness.

## 8. Caveats And Next Steps

State what the estimate does not prove, what assumptions are hardest to defend, and what validation or follow-up design should come next.
