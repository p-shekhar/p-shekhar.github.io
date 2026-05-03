# EconML Tutorials

This folder is for hands-on tutorial notebooks focused on EconML, a widely used Python library for estimating heterogeneous treatment effects with modern machine-learning methods.

The goal is to make these notebooks educational rather than tied to one applied portfolio project. Each notebook should explain the causal question, the data-generating setup or dataset, the treatment and outcome definitions, the nuisance models, the target estimand, the EconML estimator being used, and the diagnostics that make the result more credible.

EconML is especially useful when the causal question is clear and the next challenge is estimation:

- estimating conditional average treatment effects;
- using flexible models for outcome and treatment nuisance functions;
- comparing DML, DR, forest, and meta-learner approaches;
- ranking units by expected treatment benefit;
- building treatment-targeting or policy-learning workflows.

Notebook sequence:

- `00_environment_and_econml_tour.ipynb`  
  Check the environment, imports, package versions, and the main EconML estimator families used across the tutorial series.

- `01_cate_foundations_potential_outcomes.ipynb`  
  Introduce ATE, CATE, potential outcomes, treatment heterogeneity, and why personalization changes the analysis target.

- `02_double_machine_learning_basics.ipynb`  
  Explain orthogonalization, residualization, nuisance models, and cross-fitting with a simple DML workflow.

- `03_lineardml_and_sparselineardml.ipynb`  
  Estimate interpretable heterogeneous effects with LinearDML and SparseLinearDML.

- `04_causalforestdml.ipynb`  
  Use CausalForestDML for nonlinear CATE estimation, intervals, feature importance, and segment summaries.

- `05_drlearner_and_doubly_robust_estimation.ipynb`  
  Use DRLearner for binary treatment settings and explain why doubly robust nuisance modeling is useful.

- `06_metalearners_s_t_x_learners.ipynb`  
  Compare S-Learner, T-Learner, X-Learner, and related meta-learner ideas.

- `07_policy_learning_and_treatment_targeting.ipynb`  
  Turn CATE estimates into treatment ranking, targeting rules, and policy-value comparisons.

- `08_interpretability_shap_and_segments.ipynb`  
  Explain CATE drivers with feature importance, SHAP-style explanations, and segment-level summaries.

- `09_inference_intervals_and_uncertainty.ipynb`  
  Cover confidence intervals, uncertainty-aware decisions, and how to avoid overreacting to noisy CATE estimates.

- `10_multiple_treatments_and_continuous_treatments.ipynb`  
  Extend from binary treatments to multi-arm and continuous-treatment examples.

- `11_iv_estimators_deepiv_and_dmliv.ipynb`  
  Introduce instrumental-variable treatment-effect estimation with EconML's IV-oriented estimators.

- `12_panel_or_longitudinal_extensions.ipynb`  
  Discuss repeated observations, time-varying settings, and when a simple cross-sectional CATE design is not enough.

- `13_estimator_comparison_benchmark.ipynb`  
  Compare LinearDML, CausalForestDML, DRLearner, and meta-learners on the same simulated ground truth.

- `14_end_to_end_case_study.ipynb`  
  Combine data preparation, nuisance modeling, CATE estimation, policy targeting, diagnostics, and reporting.

- `15_common_pitfalls_debugging_reporting.ipynb`  
  Cover overlap failures, leakage, bad nuisance models, overinterpreting CATE, and transparent reporting habits.

Style notes:

- Keep code visible by default.
- Add explanatory markdown before every code cell.
- Add a short natural discussion after result-producing cells so the analysis flows from one step to the next.
- Keep the tutorials company-neutral and focused on reusable causal inference skills.
- Prefer small synthetic teaching datasets until a notebook explicitly needs a real dataset.
