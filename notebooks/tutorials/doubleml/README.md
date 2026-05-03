# DoubleML Tutorials

This folder is for hands-on tutorial notebooks focused on `DoubleML`, the Python package for double / debiased machine learning effect estimation.

Unlike causal discovery libraries, DoubleML is mainly used after a causal design has been specified. The central workflow is: define the estimand, structure the data, choose nuisance learners, use orthogonal scores with cross-fitting, estimate effects, quantify uncertainty, and report assumptions clearly.

Install the core package with:

```bash
uv add doubleml
```

For the RDD notebook, the optional RDD dependency may be needed depending on the local package version and workflow:

```bash
uv add "doubleml[rdd]"
```

Notebook sequence:

- `00_environment_and_library_tour.ipynb`  
  Install check, package versions, core objects, built-in datasets, and where DoubleML fits in causal ML.

- `01_dml_theory_orthogonalization_and_cross_fitting.ipynb`  
  Regularization bias, Neyman orthogonality, nuisance functions, sample splitting, cross-fitting, DML1, and DML2.

- `02_data_backend_doublemldata_and_design_setup.ipynb`  
  Outcome, treatment, covariate, instrument, time, cluster, and sample-selection roles in the DoubleML data backend.

- `03_partially_linear_regression_plr.ipynb`  
  Core PLR workflow for continuous treatment effects with flexible nuisance learners.

- `04_partially_linear_iv_pliv.ipynb`  
  Instrumental-variable DML for continuous treatments with endogenous treatment assignment.

- `05_interactive_regression_model_irm.ipynb`  
  Binary-treatment ATE and ATT estimation with propensity scores and outcome nuisance models.

- `06_interactive_iv_model_iivm.ipynb`  
  Binary treatment with instruments, compliance logic, and local effect meaning.

- `07_difference_in_differences_did.ipynb`  
  DID models, treatment timing, repeated cross sections, panels, and nuisance learning.

- `08_sample_selection_models.ipynb`  
  Selection correction workflows for outcomes observed only in selected samples.

- `09_regression_discontinuity_design_rdd.ipynb`  
  RDD workflow, running variables, cutoffs, bandwidths, and optional DoubleML RDD dependencies.

- `10_learners_hyperparameters_and_tuning.ipynb`  
  Learner choices, preprocessing pipelines, LightGBM/XGBoost/sklearn examples, and tuning without leakage.

- `11_sample_splitting_cross_fitting_and_repeated_cross_fitting.ipynb`  
  K-fold choices, repeated cross-fitting, external sample splits, and no-cross-fitting comparisons.

- `12_inference_bootstrap_and_confidence_bands.ipynb`  
  Standard errors, confidence intervals, multiplier bootstrap, simultaneous inference, and reporting uncertainty.

- `13_sensitivity_analysis_for_unobserved_confounding.ipynb`  
  DoubleML sensitivity tools, robustness values, omitted-variable concerns, and cautious reporting.

- `14_heterogeneous_treatment_effects_gate_cate_blp.ipynb`  
  Group average treatment effects, conditional effects, best linear predictors, and subgroup reporting.

- `15_policy_learning_weighted_ates_quantiles_and_cvar.ipynb`  
  Policy learning, weighted average treatment effects, quantiles, and tail-risk causal targets.

- `16_custom_scores_and_advanced_api.ipynb`  
  Custom Neyman-orthogonal scores, advanced model configuration, and extension patterns.

- `17_common_pitfalls_diagnostics_and_reporting.ipynb`  
  Overlap, bad controls, leakage, weak instruments, unstable nuisance models, wrong estimands, and report writing.

- `18_end_to_end_doubleml_case_study.ipynb`  
  A complete applied workflow from causal question to final effect estimate, sensitivity analysis, and reporting.

Style notes:

- Keep code visible by default.
- Add explanatory markdown before every code cell.
- Add a short natural discussion after result-producing cells so the analysis flows smoothly.
- Keep tutorials company-neutral and focused on reusable causal effect-estimation skills.
- Treat DoubleML estimates as design-based causal estimates: the model helps with nuisance adjustment, but the identification assumptions come from the causal design.