# Resume Bullets

- Built an off-policy evaluation framework for recommendation systems using Open Bandit logs, estimating counterfactual policy value with IPS, self-normalized IPS, direct method, and doubly robust estimators from logged propensities.
- Trained LightGBM reward models to learn context-aware recommendation policies, then evaluated greedy, epsilon-greedy, softmax, and conservative mixed policies with ESS, clipping sensitivity, and residual-correction diagnostics.
- Produced an A/B-test recommendation framework that balanced estimated click lift with support risk, identifying `lgbm_conservative_mix` as a contextual candidate and `fixed_ctr_weighted` as a stable fallback policy.
