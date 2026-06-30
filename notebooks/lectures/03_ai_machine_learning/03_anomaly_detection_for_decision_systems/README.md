# 03 Anomaly Detection for Decision Systems

This course will focus on detecting unusual events, risky cases, rare failures, and operational deviations in data systems. It should balance algorithmic methods with threshold design, review workflows, and deployment realism.

## Data Realism Standard

Anomaly-detection notebooks often need simulated labels because real deployments rarely have clean truth for every monitored case. That is acceptable, but the simulated systems should resemble production monitoring problems: multiple normal regimes, benign rare behavior, true incidents, delayed review labels, alert budgets, false-alarm costs, drift, and human investigation.

Each notebook should make clear which labels are available only because the case is simulated. Production analogues would come from incident tickets, expert review, customer reports, chargebacks, staged audits, or post-incident analysis. The goal is to teach detector behavior and decision design without pretending that synthetic labels are available in real time.

## Notebook Sequence

1. `01_anomaly_detection_for_decision_science.ipynb` - Anomaly Detection for Decision Science
2. `02_statistical_foundations_of_anomaly_detection.ipynb` - Statistical Foundations of Anomaly Detection
3. `03_thresholds_alerts_and_decision_costs.ipynb` - Thresholds, Alerts, and Decision Costs
4. `04_univariate_and_multivariate_statistical_detectors.ipynb` - Univariate and Multivariate Statistical Detectors
5. `05_distance_based_methods_knn_and_local_outlier_factor.ipynb` - Distance-Based Methods: kNN and Local Outlier Factor
6. `06_density_based_anomaly_detection.ipynb` - Density-Based Anomaly Detection
7. `07_tree_based_anomaly_detection_isolation_forest.ipynb` - Tree-Based Anomaly Detection: Isolation Forest
8. `08_one_class_classification_and_support_vector_methods.ipynb` - One-Class Classification and Support Vector Methods
9. `09_reconstruction_based_detection_pca_autoencoders.ipynb` - Reconstruction-Based Detection: PCA and Autoencoders
10. `10_time_series_anomaly_detection.ipynb` - Time-Series Anomaly Detection
11. `11_change_point_detection_and_distribution_shift.ipynb` - Change-Point Detection and Distribution Shift
12. `12_anomaly_detection_for_logs_events_and_sequences.ipynb` - Anomaly Detection for Logs, Events, and Sequences
13. `13_evaluating_anomaly_detection_without_clean_labels.ipynb` - Evaluating Anomaly Detection Without Clean Labels
14. `14_explaining_anomaly_scores.ipynb` - Explaining Anomaly Scores
15. `15_from_alerts_to_root_cause_analysis.ipynb` - From Alerts to Root Cause Analysis
16. `16_governance_fairness_privacy_and_human_review.ipynb` - Governance, Fairness, Privacy, and Human Review
17. `17_capstone_anomaly_detection_decision_pipeline.ipynb` - Capstone: Anomaly Detection Decision Pipeline
