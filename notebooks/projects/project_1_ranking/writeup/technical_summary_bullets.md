# Technical Summary Bullets

- Estimated the causal effect of ranking position on user clicks using MIND impression logs; built an impression-level analysis table with rank, click, user-history, item metadata, slate-size, time, and exposure features.
- Implemented IPW, doubly robust AIPW, LightGBM/XGBoost nuisance models, EconML DRLearner/CausalForestDML, heterogeneous treatment effect analysis, policy simulation, and sensitivity checks for a recommendation ranking use case.
- Translated causal estimates into product recommendations by identifying high-lift content/context segments and simulating budgeted top-3 promotion policies under uncertainty-aware decision rules.
