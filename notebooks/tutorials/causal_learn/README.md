# causal-learn Tutorials

This folder is for hands-on tutorial notebooks focused on `causal-learn`, a Python library for causal discovery.

The goal is to make these notebooks educational and reusable. Each notebook should explain the discovery question, the data-generating setup or dataset, the graph assumptions, the algorithm family, the output graph type, and the diagnostics that make the result easier to trust.

`causal-learn` is especially useful for tabular and small-to-medium graph discovery workflows:

- constraint-based methods such as PC, FCI, and CD-NOD;
- score-based methods such as GES and exact search;
- functional causal models such as LiNGAM, additive-noise models, and post-nonlinear models;
- permutation-based methods such as GRaSP and BOSS;
- independence tests, score functions, graph operations, and evaluation utilities.

Notebook sequence:

- `00_environment_and_library_tour.ipynb`  
  Check the environment, imports, package versions, graph utilities, and the main causal-learn algorithm families used across the tutorial series.

- `01_graphs_dags_cpdag_pag_and_evaluation.ipynb`  
  Introduce graph objects, edge marks, equivalence classes, and graph-comparison metrics before running discovery algorithms.

- `02_synthetic_data_for_causal_discovery.ipynb`  
  Build reusable teaching datasets with known graphs so later discovery outputs can be evaluated honestly.

- `03_independence_tests.ipynb`  
  Study the conditional independence tests that power constraint-based discovery methods.

- `04_pc_algorithm_continuous_data.ipynb`  
  Use PC on continuous data and study alpha sensitivity, skeleton discovery, and edge orientation.

- `05_pc_with_prior_knowledge_missing_and_discrete_data.ipynb`  
  Extend PC-style discovery with background knowledge, missing-value handling, and discrete-data tests.

- `06_fci_for_latent_confounders.ipynb`  
  Use FCI when hidden common causes may exist and learn how to read PAG outputs.

- `07_cdnod_for_nonstationary_data.ipynb`  
  Introduce causal discovery under changing environments and distribution shifts.

- `08_score_based_discovery_ges.ipynb`  
  Use GES and score functions to learn graph structure through search rather than conditional-independence pruning.

- `09_exact_search_and_score_functions.ipynb`  
  Study exact search and score choices on small graphs where exhaustive or dynamic programming strategies are feasible.

- `10_lingam_linear_nongaussian_models.ipynb`  
  Use LiNGAM-style methods when linearity and non-Gaussian noise can identify directions beyond Markov equivalence.

- `11_functional_causal_models_anm_pnl.ipynb`  
  Explore pairwise and functional causal discovery based on additive-noise and post-nonlinear assumptions.

- `12_permutation_based_methods_grasp_boss.ipynb`  
  Introduce permutation-search methods and compare them with PC and GES on synthetic graphs.

- `13_time_series_causal_discovery.ipynb`  
  Cover causal-learn time-series tools and frame when a separate Tigramite tutorial may be better for large time-series workflows.

- `14_hidden_representation_learning_gin.ipynb`  
  Introduce GIN-style ideas for hidden causal representation and latent structure.

- `15_benchmarking_stability_and_sensitivity.ipynb`  
  Compare discovery algorithms across noise, sample size, hidden confounding, nonlinearity, and tuning settings.

- `16_end_to_end_causal_discovery_case_study.ipynb`  
  Combine data audit, domain constraints, algorithm choice, graph estimation, stability checks, and final graph reporting.

- `17_common_pitfalls_reporting_and_limitations.ipynb`  
  Close the series with failure modes: hidden confounding, weak tests, over-orientation, leakage, selection bias, and overclaiming graph direction.

Style notes:

- Keep code visible by default.
- Add explanatory markdown before every code cell.
- Add a short natural discussion after result-producing cells so the analysis flows from one step to the next.
- Keep tutorials company-neutral and focused on reusable causal discovery skills.
- Prefer small synthetic teaching datasets until a notebook explicitly needs a real dataset.
- Treat discovered graphs as candidate structures unless assumptions, stability checks, and domain knowledge support stronger claims.

## Figure Style Note

DAG-style figures in this tutorial should follow the visual style used in `notebooks/tutorials/dowhy/outputs/figures/00_teaching_dag.png`: a wide white canvas, rounded pastel text boxes, bold variable labels, dark annotation arrows, clear arrowhead spacing, and enough horizontal room for long causal paths. This keeps the tutorial notebooks visually consistent across libraries.
