# Applied Causal Decision Projects

This folder contains notebook-backed projects in causal inference, off-policy evaluation, sequential effects, interference, and mediation. Each project is designed as a hands-on decision workflow, with data explanation, mathematical setup, executable analysis, diagnostics, and interpretation.

These projects are meant to support public project pages on the website. The website should introduce the decision problem first, then link to the analytic notebooks as the reproducible sequence behind that project.

## Project Map

| Project | Public framing | Public notebook sequence | Artifact notebook |
|---|---|---|---|
| [`project_1_ranking`](project_1_ranking/) | Ranking Position and Incremental Click Lift | `01` through `08` | `09_final_report_figures.ipynb` |
| [`project_2_off_policy_evaluation`](project_2_off_policy_evaluation/) | Off-Policy Evaluation for Recommendation Policies | `01` through `06` | `07_final_report_and_artifacts.ipynb` |
| [`project_3_long_term_causal_effects`](project_3_long_term_causal_effects/) | Long-Term Effects in Recommendation Systems | `01` through `06` | `07_sensitivity_and_final_report.ipynb` |
| [`project_4_interference_spillover_effects`](project_4_interference_spillover_effects/) | Interference and Spillovers in Recommendation Slates | `01` through `05` | `06_sensitivity_and_final_report.ipynb` |
| [`project_5_discovery_quality_mediation`](project_5_discovery_quality_mediation/) | Discovery Quality and Mediation | `01` through `06` | `07_final_report_and_figures.ipynb` |

## How To Use These Projects

Start with the project README, then work through the public notebook sequence in order. The early notebooks define the data, estimand, and design problem. The middle notebooks estimate effects or policy values. The later notebooks add diagnostics, sensitivity analysis, and decision interpretation.

Artifact notebooks create final figures, tables, snippets, and writeup files. They are useful for building project pages and reports, while the public sequence gives readers the cleaner analytic path.

## Data Sources

- MIND news recommendation impression logs for ranking-position analysis.
- Open Bandit Dataset logs for off-policy evaluation with known behavior-policy propensities.
- KuaiRec interaction logs for sequential recommendation effects and discovery-quality mediation.
- MovieLens ratings data for simulated recommendation slates and interference analysis.

## Verified References And Data Links

- Wu, F., Qiao, Y., Chen, J. H., Wu, C., Qi, T., Lian, J., Liu, D., Xie, X., Gao, J., Wu, W., & Zhou, M. (2020). MIND: A large-scale dataset for news recommendation. *ACL 2020*. [ACL Anthology](https://aclanthology.org/2020.acl-main.331/) and [dataset site](https://msnews.github.io/).
- Saito, Y., Aihara, S., Matsutani, M., & Narita, Y. (2021). Open Bandit Dataset and Pipeline: Towards realistic and reproducible off-policy evaluation. [arXiv:2008.07146](https://arxiv.org/abs/2008.07146) and [OBP GitHub repository](https://github.com/st-tech/zr-obp).
- Gao, C., Li, S., Lei, W., Chen, J., Li, B., Jiang, P., He, X., Mao, J., & Chua, T.-S. (2022). KuaiRec: A fully-observed dataset and insights for evaluating recommender systems. *CIKM 2022*. [https://doi.org/10.1145/3511808.3557220](https://doi.org/10.1145/3511808.3557220), [arXiv:2202.10842](https://arxiv.org/abs/2202.10842), and [dataset site](https://kuairec.com/).
- Harper, F. M., & Konstan, J. A. (2015). The MovieLens datasets: History and context. *ACM Transactions on Interactive Intelligent Systems*, 5(4), Article 19. [https://doi.org/10.1145/2827872](https://doi.org/10.1145/2827872) and [GroupLens MovieLens data page](https://grouplens.org/datasets/movielens/).
