# 02 Interpretable ML and XAI

This course will focus on explanation, transparency, and model understanding for high-stakes analytics. It should connect technical explanation methods to governance, trust, and stakeholder-facing communication.

## Data Realism Standard

Interpretability examples should be rich enough that explanations have real work to do. A useful simulated dataset should include correlated drivers, interactions, thresholds, segment heterogeneity, noisy labels, and governance-relevant constraints. The model should be plausible enough that coefficients, rules, SHAP values, LIME explanations, partial dependence, recourse, and stability checks reveal genuine tradeoffs.

Whenever synthetic truth is visible, the notebook should clearly separate teaching knowledge from production knowledge. In production, analysts would not know the true response surface, true treatment effect, or hidden segment label. Those quantities are shown only to evaluate whether the explanation workflow behaves sensibly.

## Planned Notebook Sequence

1. Why interpretability matters in decision systems
2. Transparent models as first-class baselines
3. Reading models: coefficients, odds ratios, and response surfaces
4. Shape constraints, monotonicity, and business logic
5. Tree models, path logic, and segment rules
6. Global explanations: partial dependence, ICE, and ALE
7. Permutation importance and model reliance
8. SHAP values: intuition, computation, and failure modes
9. LIME, local surrogates, and neighborhood sensitivity
10. Interactions, heterogeneity, and nonlinear structure
11. Counterfactual explanations and actionable recourse
12. Explaining ranking, prioritization, and policy scores
13. Explanation stability across resamples and retrains
14. When explanations conflict with causal reasoning
15. Fairness, governance, and auditability of explanations
16. Communicating explanations to stakeholders
17. Capstone: an interpretable decision pipeline
