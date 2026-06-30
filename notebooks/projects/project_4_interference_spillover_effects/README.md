# Interference and Spillovers in Recommendation Slates

This project studies interference in recommendation and content discovery systems. Promoting one item can change the exposure and outcomes of nearby items, so the relevant decision often has to be made at the slate, cluster, or market level.

## What You Will Build

You will build a spillover-aware causal workflow. The project constructs recommendation slates from MovieLens preference data, simulates promotion assignment, maps direct and neighbor exposure, estimates direct and indirect effects, and studies when item-level conclusions differ from slate-level conclusions.

## How To Use This Project

Notebook `01` builds the slate setting and explains why interference matters. Notebook `02` defines exposure mappings. The next notebooks estimate cluster-randomized effects, decompose direct, indirect, and total effects, and add advanced spillover models. The sequence is designed to show how a recommendation change can create gains, displacement, or both.

The final notebook is an artifact and sensitivity notebook. Use the first five notebooks as the public analytic path.

## Data Source And Scope

The project uses MovieLens ratings as a real preference source, then constructs simulated recommendation slates and promotion assignments. The simulation is intentional. MovieLens does not contain randomized promotion experiments, so the project uses the real item-user preference structure to create a controlled interference setting where exposure mappings and effect definitions can be studied transparently.

## Notebook Sequence

- [01 MovieLens interference setup and EDA](01_movielens_interference_setup_eda.ipynb)
- [02 Spillover exposure mapping](02_spillover_exposure_mapping.ipynb)
- [03 Cluster-randomized estimators](03_cluster_randomized_estimators.ipynb)
- [04 Direct, indirect, and total effects](04_direct_indirect_total_effects.ipynb)
- [05 Advanced spillover models](05_advanced_spillover_models.ipynb)

## Artifact Notebook

- [06 Sensitivity and final report](06_sensitivity_and_final_report.ipynb)

This notebook assembles sensitivity checks and final artifacts. The main public project should focus on notebooks `01` through `05`.

## Key Interpretation

Item-level lift can be misleading when units compete for limited attention. The project shows how exposure mappings, cluster assignment, and spillover decomposition help separate gains for promoted items from displacement of neighboring items.

## Verified References And Data Links

- Harper, F. M., & Konstan, J. A. (2015). The MovieLens datasets: History and context. *ACM Transactions on Interactive Intelligent Systems*, 5(4), Article 19. [https://doi.org/10.1145/2827872](https://doi.org/10.1145/2827872) and [GroupLens MovieLens data page](https://grouplens.org/datasets/movielens/).
