# 04 AI for Causal Inference

This course studies how LLMs and AI systems can support causal-inference workflows without replacing the analyst. The emphasis is on structured drafts, critique, retrieval, diagnostics, report generation, agents, and evaluation harnesses that keep causal claims auditable.

## Data and Model Realism Standard

The notebooks use a mix of deterministic examples, synthetic causal datasets, small retrieval corpora, and optional live local LLM calls. This is intentional. Synthetic causal data lets the course expose potential outcomes, hidden confounders, bad controls, oracle estimates, and ground-truth failure modes that real business data would not reveal.

Every synthetic example should state what is visible only for teaching and what would be unknown in production. Every LLM example should treat model output as an empirical artifact that can vary across model family, scale, prompt, decoding settings, package versions, and reruns. A good notebook should include deterministic checks, structured schemas, repair logic, model comparison where useful, and human review gates.

The standard is not to make AI look smooth. The standard is to make AI-assisted causal work inspectable.
