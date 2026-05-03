# DoubleML Diagnostics And Reporting Template

## 1. Causal Question
State the treatment, outcome, population, and target estimand. For PLR, write whether the target is a constant marginal effect like $	heta_0$.

## 2. Identification Assumptions
Describe the adjustment set, timing of all controls, unconfoundedness assumptions, overlap or residual treatment variation, and any reasons these assumptions may fail.

## 3. Data And Feature Timing
List every feature group and classify it as pre-treatment, treatment, mediator, outcome, post-treatment, or future information. Exclude post-treatment controls from the main design.

## 4. DoubleML Specification
Report the DoubleML class, score, learners for each nuisance function, fold count, repeated-split count, random seeds, and whether sample splitting was supplied externally.

## 5. Main Estimate
Report estimate, standard error, confidence interval, and sample size. Explain the units of treatment and outcome.

## 6. Diagnostics
Include nuisance RMSE, residualized-treatment variation, score denominator, sample-split stability, and any learner-comparison results.

## 7. Robustness And Sensitivity
Discuss omitted-confounder risk, alternative adjustment sets, weak-overlap checks, and whether the estimate changes under defensible specifications.

## 8. Limitations
State what the analysis cannot prove. DoubleML does not repair missing confounders, bad controls, interference, measurement error, or target mismatch.

## 9. Artifact Paths From This Notebook
- Pitfall map: /home/apex/Documents/ranking_sys/notebooks/tutorials/doubleml/outputs/tables/17_pitfall_map.csv
- Control-set scenarios: /home/apex/Documents/ranking_sys/notebooks/tutorials/doubleml/outputs/tables/17_control_set_scenarios.csv
- Residual treatment variation: /home/apex/Documents/ranking_sys/notebooks/tutorials/doubleml/outputs/tables/17_residual_treatment_variation.csv
- Nuisance learner comparison: /home/apex/Documents/ranking_sys/notebooks/tutorials/doubleml/outputs/tables/17_nuisance_learner_comparison.csv
- Sample-split summary: /home/apex/Documents/ranking_sys/notebooks/tutorials/doubleml/outputs/tables/17_sample_split_summary.csv
- Diagnostic scorecard: /home/apex/Documents/ranking_sys/notebooks/tutorials/doubleml/outputs/tables/17_diagnostic_scorecard.csv
