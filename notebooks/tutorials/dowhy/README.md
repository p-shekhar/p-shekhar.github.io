# DoWhy Tutorials

This folder is for hands-on tutorial notebooks focused on DoWhy, a widely used Python library for causal inference workflows built around explicit causal graphs, estimand identification, effect estimation, and refutation.

The goal is to make these notebooks educational rather than tied to one applied portfolio project. Each notebook should explain the causal question, the data-generating setup or dataset, the graph assumptions, the identified estimand, the estimator being used, and the diagnostic/refutation checks that make the result more credible.

Notebook sequence:

- `00_environment_and_library_tour.ipynb`  
  Check the environment, imports, package versions, and the main DoWhy API areas used across the tutorial series.

- `01_core_workflow_model_identify_estimate_refute.ipynb`  
  Introduce the standard DoWhy workflow: model, identify, estimate, and refute.

- `02_causal_graphs_dags_and_assumptions.ipynb`  
  Focus on DAGs, causes, effects, mediators, colliders, confounders, and assumption documentation.

- `03_backdoor_adjustment_and_confounding.ipynb`  
  Study backdoor paths, observed confounding, and adjusted versus unadjusted effect estimates.

- `04_regression_matching_and_propensity_estimators.ipynb`  
  Compare regression, matching, stratification, and propensity-score estimators for the same estimand.

- `05_weighting_overlap_and_common_support.ipynb`  
  Diagnose propensity overlap, common support, extreme weights, and trimmed versus untrimmed estimates.

- `06_frontdoor_iv_and_natural_experiments.ipynb`  
  Introduce frontdoor identification, instrumental variables, and natural-experiment logic.

- `07_cate_and_heterogeneous_effects.ipynb`  
  Move from average treatment effects to conditional and segment-level treatment effects.

- `08_refuters_placebos_negative_controls_sensitivity.ipynb`  
  Use placebo treatments, negative controls, random common causes, subset refuters, and sensitivity checks.

- `09_graph_discovery_and_graph_refutation.ipynb`  
  Explore causal discovery integrations and graph-level assumption checks.

- `10_gcm_structural_causal_models.ipynb`  
  Introduce graphical causal models, causal mechanisms, mechanism assignment, and model evaluation.

- `11_interventions_and_counterfactuals_with_gcm.ipynb`  
  Use GCMs to simulate interventions and answer counterfactual what-if questions.

- `12_mediation_direct_and_indirect_effects.ipynb`  
  Decompose effects into total, direct, and indirect pathways.

- `13_root_cause_anomaly_and_distribution_change.ipynb`  
  Use GCM tools for anomaly attribution, root-cause analysis, and distribution-shift attribution.

- `14_end_to_end_observational_case_study.ipynb`  
  Combine the earlier ideas into a compact applied workflow from data through final causal summary.

- `15_common_pitfalls_debugging_and_reporting.ipynb`  
  Cover bad controls, colliders, leakage, weak overlap, estimator instability, and transparent reporting.

Style notes:

- Keep code visible by default.
- Add explanatory markdown before every code cell.
- Add a short natural discussion after result-producing cells so the analysis flows from one step to the next.
- Avoid company-specific framing; make the tutorials useful for causal inference roles in general.
