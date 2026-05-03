# DoubleML Backend Design Report

## 1. Causal Question

State the treatment, outcome, target population, and estimand.

## 2. Backend Class

Name the DoubleML backend class used and explain why it matches the design.

## 3. Column Roles

- Outcome column:
- Treatment column(s):
- Control columns:
- Instrument column(s):
- Cluster column(s):
- Unit/time columns:
- Running score column:
- Selection column:

## 4. Excluded Columns

List columns intentionally excluded from controls, especially identifiers, instruments, post-treatment variables, colliders, mediators, and target leakage columns.

## 5. Data Audit

Summarize missingness, finite-value checks, data types, treatment variation, binary-treatment support, instrument support, cluster counts, panel balance, RDD cutoff support, or selection support as relevant.

## 6. Assumption Notes

State the identification assumptions that must be defended outside the backend object.

## 7. Ready For Model Fitting?

State what remains to check before fitting: nuisance learner choice, sample splitting, tuning, inference, and sensitivity.
