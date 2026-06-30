# Final Summary: Off-Policy Evaluation Of Recommendation Systems

## Problem
This project evaluates recommendation policies offline using logged bandit data. The business question asks which recommendation policy is most credible to advance to an online A/B test.

## Dataset
The analysis uses the Open Bandit Dataset, focusing on the `random/men` campaign because it contains logged actions, click rewards, context features, and known behavior-policy propensities. The random behavior policy provides broad support, which is important for reliable off-policy evaluation.

## Methods
The project implements IPS, self-normalized IPS, direct method, doubly robust OPE, weight diagnostics, reward-model diagnostics, clipping sensitivity, reward-model sensitivity, split sensitivity, and contextual policy learning with LightGBM reward scores.

## Final Recommendation
The primary offline A/B-test candidate is `lgbm_conservative_mix`. Its estimated DR click rate is 0.5324%, with estimated lift of 0.034 percentage points versus the observed random-policy baseline. Because this policy is still marked `clip sensitive`, the safer fallback is `fixed_ctr_weighted`, which has stronger support diagnostics and estimated lift of 0.030 percentage points.

## Interpretation
The project recommends a prioritized online experiment based on offline OPE evidence. Test a conservative contextual policy or stable fixed policy against the current/random baseline while tracking click quality, longer-term engagement, and user experience guardrails.
