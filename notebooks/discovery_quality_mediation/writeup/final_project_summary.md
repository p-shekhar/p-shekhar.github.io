# Discovery Quality Mediation: Final Summary

## Problem

Recommendation systems can increase short-term activity without necessarily improving user satisfaction or durable value. This analysis studies whether high discovery exposure is associated with future user value, and whether that relationship is mediated by same-day satisfaction depth.

## Data and Unit of Analysis

- Dataset: KuaiRec interaction logs and metadata.
- Analysis unit: active user-day.
- Final analysis panel: 8,199 active user-days from 133 users.
- Treatment: high discovery-breadth day.
- Mediator: same-day satisfaction-depth score.
- Primary outcome: future seven-day interactions.

## Metrics

- `discovery_breadth_score`: exposure-like metric combining long-tail content, new category exposure, and category breadth.
- `satisfaction_depth_score`: mediator-like score combining watch quality, valid play, completion, and abandonment proxies.
- `quality_adjusted_discovery_score`: product monitoring metric that requires both discovery and satisfaction to be high.
- `shallow_click_pressure_score`: guardrail for high-volume, low-satisfaction engagement.

## Main Results

- Total effect on future seven-day interactions: **+37.3** with 95% bootstrap interval **[32.2, 42.8]**.
- Natural direct effect: **+38.6**.
- Natural indirect effect through satisfaction depth: **-1.3**.
- Estimated shift in satisfaction depth from high discovery exposure: **+0.023**.
- Future play-hours total effect: **+0.078** hours.

The primary future-interaction gain is mostly direct in this specification. The satisfaction-depth mediated pathway is small relative to the total effect.

## Robustness

- Discovery-threshold sensitivity kept the total future-interaction effect positive across 4 tested thresholds.
- Mediator sensitivity kept the total effect positive across 5 satisfaction proxy definitions.
- Model sensitivity kept the total effect positive across weighted/unweighted, interaction/no-interaction, and simple/rich control choices.
- Placebo-style checks show meaningful pre-period imbalance, which reinforces the need for adjustment and caution.

## Advanced Models

- SEM-style path model aligns closely with the linear g-computation result.
- Cross-fitted LightGBM and XGBoost keep the effect direction positive but shrink the estimated future-interaction effect to **+3.2** and **+2.7**.
- The advanced model comparison supports a conservative conclusion: direction is stable, magnitude is model-sensitive.

## Limitations

- The data are observational recommendation logs, not randomized experiments.
- Satisfaction is measured through watch-behavior proxies.
- Unobserved user intent and ranking-system state may confound treatment, mediator, and outcome relationships.
- The analysis conditions on active user-days and may not generalize to dormant users.

## Bottom Line

High discovery exposure appears positively associated with future user value, especially future interaction volume and play time. The evidence for a large satisfaction-mediated pathway is weak in the primary interaction-count analysis. A careful product takeaway is to track discovery quality separately from satisfaction depth and to validate discovery policies with future-value metrics, not short-term clicks alone.
