# Technical Summary Bullets

- Built an end-to-end causal mediation analysis on KuaiRec recommendation logs to study how discovery exposure, satisfaction depth, and future user value relate at the active user-day level.
- Engineered discovery-quality metrics separating exposure, mediator, composite product score, and guardrail roles; validated metrics against future engagement while avoiding future-label leakage.
- Estimated total, natural direct, natural indirect, and controlled direct effects with g-computation and user-level bootstrap uncertainty across 8,199 active user-days.
- Stress-tested mediation findings across treatment thresholds, mediator definitions, outcome definitions, weighting choices, interaction terms, control sets, and placebo-style pre-period checks.
- Compared linear mediation, SEM-style path modeling, and cross-fitted LightGBM/XGBoost nuisance models; found stable positive direction but model-sensitive effect magnitude.
- Produced report-ready report artifacts, figures, limitations, and artifact index for a recommendation-system causal measurement workflow.
