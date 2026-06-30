# 03 AI and Machine Learning

Path: `03_ai_machine_learning/`

This track complements the causal sequence with a decision-science-oriented machine-learning module. The emphasis is not generic model building for its own sake, but predictive systems that can be trusted, interpreted, monitored, and used responsibly in operational settings.

## Data Realism Standard

Most notebooks in this module use controlled simulations because they let the course expose hidden states, delayed labels, intervention effects, anomaly truth, and operational costs that real public datasets rarely provide. The simulations should still feel like decision-science data, with realistic structure and operational stakes.

When a notebook uses simulated data, the data story should name the unit of analysis, decision horizon, action that depends on the model, observed features, hidden drivers, label limitations, and production caveats. Good examples should include realistic complications such as heterogeneous regimes, correlated features, nonlinear thresholds, class imbalance, measurement noise, delayed labels, drift, capacity constraints, guardrails, or human review. Low-dimensional geometric examples are acceptable only as short algorithmic warm-ups and should be followed by an operational tabular or workflow example.

## Course Structure

- `01_machine_learning_basics_for_decision_science/`
- `02_interpretable_ml_and_xai/`
- `03_anomaly_detection_for_decision_systems/`
- `04_ai_for_causal_inference/`

## 01 Machine Learning Basics for Decision Science

This course should teach machine learning as a disciplined workflow for decision support. The framing should be practical: what prediction, grouping, ranking, or structure-discovery task is being used; what action depends on it; what error costs matter; and what evidence is needed before deployment. It should explicitly cover both supervised and unsupervised learning, but keep the anomaly-detection depth for the dedicated third course.

Recommended notebook sequence:

1. Statistical learning for decision systems
2. Framing business questions as supervised and unsupervised learning tasks
3. Data-generating processes, labels, features, and representative data
4. Train, validation, and test splits without leakage
5. Linear and logistic models as predictive baselines
6. Regularization, bias-variance tradeoffs, and feature selection
7. Tree-based methods: CART, random forests, and gradient boosting
8. Regression metrics, residuals, and operational error costs
9. Classification metrics, thresholds, and confusion matrices
10. Probability calibration and risk scoring
11. Unsupervised learning for segmentation and structure discovery
12. Clustering methods: k-means, hierarchical clustering, and density ideas
13. Dimensionality reduction: PCA, embeddings, and visualization
14. Feature engineering for operational machine learning
15. Hyperparameter tuning, model comparison, and pipelines
16. Error analysis by segment and use case
17. Monitoring drift, degradation, and feedback loops
18. From scores, segments, and model outputs to operational recommendations

## 02 Interpretable ML and XAI

This course should move from transparent models to post-hoc explanation methods, while being honest about what explanations can and cannot support. The key theme is explanation quality in high-stakes settings.

Recommended notebook sequence:

1. Why interpretability matters in decision science
2. Inherently interpretable models: linear, sparse, rule-based, monotone
3. Coefficients, odds ratios, margins, and response surfaces
4. Partial dependence, ICE, and ALE plots
5. Permutation importance and model reliance
6. Global surrogate models and approximation caveats
7. SHAP values: intuition, computation, and failure modes
8. Local explanations with LIME and neighborhood sensitivity
9. Interaction effects and explanation of nonlinear structure
10. Counterfactual explanations and actionable recourse
11. Explaining ranking, prioritization, and policy scores
12. Stability of explanations across resamples and retrains
13. Interpretable reporting for stakeholders and auditors
14. Fairness, transparency, and governance of explanations
15. When explanation conflicts with causal reasoning
16. Building an explanation review template for deployment

## 03 Anomaly Detection for Decision Systems

This course should treat anomaly detection as part of operational intelligence: identifying unusual cases, system failures, fraud, rare events, or safety-relevant deviations while managing false alarms and alert fatigue.

Recommended notebook sequence:

1. What counts as an anomaly in operational data
2. Point, contextual, collective, and temporal anomalies
3. Baseline rules, z-scores, robust statistics, and control limits
4. Distance-based methods and nearest-neighbor anomaly scores
5. Density-based methods: LOF and related approaches
6. Isolation Forest and tree-based anomaly detection
7. One-class classification and support estimation
8. Reconstruction-based methods and autoencoder intuition
9. Time-series anomaly detection and change-point ideas
10. Anomaly detection in transactional and event-log data
11. Segment-aware anomaly thresholds and heterogeneity
12. Precision, recall, ranking quality, and alert calibration
13. Root-cause triage with interpretable anomaly summaries
14. Monitoring pipelines, retraining triggers, and drift
15. Human-in-the-loop review and escalation policies
16. Case study: anomaly detection for a decision operations team

## 04 AI for Causal Inference

This course treats LLMs, retrieval, agents, structured outputs, and evaluation workflows as supervised assistants for causal analysis. The emphasis is not replacing identification discipline, but using AI systems to draft, critique, document, test, and communicate causal workflows more effectively.

Recommended notebook sequence:

1. Getting a local LLM running
2. AI-assisted causal workflow
3. LLM basics for causal analysts
4. Turning business questions into causal questions
5. Estimand cards and causal design documents
6. AI-assisted DAG brainstorming
7. DAG critique, variable roles, and backdoor paths
8. RAG for causal domain knowledge
9. Literature synthesis for causal assumptions
10. Dataset profiling with AI
11. Detecting bad controls, post-treatment variables, and leakage
12. Synthetic data generation for causal teaching
13. Simulation labs for assumption stress testing
14. AI-assisted method selection
15. AI-assisted causal code generation
16. Automating balance, overlap, and diagnostic reports
17. AI for sensitivity analysis
18. AI for experiment design and power planning
19. AI for quasi-experiment design
20. Causal report generation with LLMs
21. Causal analysis agent
22. Multi-agent causal review workflow
23. Evaluating AI outputs in causal workflows
24. Hallucination and failure modes in AI causal analysis
25. Capstone AI-assisted causal project
