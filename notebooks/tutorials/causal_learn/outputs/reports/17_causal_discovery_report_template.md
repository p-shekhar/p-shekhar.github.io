# Causal Discovery Report Template

## 1. Discovery Question

State the graph question in one or two sentences. Name the decision, mechanism, or scientific question the graph is meant to inform.

## 2. Data Scope

- Row unit:
- Time period:
- Inclusion and exclusion rules:
- Known selection mechanisms:
- Missingness handling:

## 3. Variable Dictionary

For each variable, include definition, measurement window, allowed causal timing tier, and whether it is an input, mechanism, outcome, or post-outcome measure.

## 4. Assumptions

State which assumptions are required by the chosen methods. Include causal sufficiency, faithfulness, stationarity, linearity, non-Gaussianity, or functional-form assumptions where relevant.

## 5. Algorithms And Settings

List algorithms, independence tests or scores, alpha values, thresholds, background knowledge, package versions, and random seeds.

## 6. Main Candidate Graph

Show the graph and separate:

- stable adjacencies;
- directions supported by timing or method assumptions;
- ambiguous or equivalence-class edges;
- edges with plausible hidden-confounding risk.

## 7. Sensitivity Checks

Summarize sample-size, alpha, threshold, seed, bootstrap, method-comparison, and hidden-confounding checks.

## 8. Edge Review Table

For each important edge, report support level, caveats, plausible omitted causes, and recommended validation.

## 9. What The Graph Does Not Prove

State limits plainly. Graph discovery alone usually does not estimate intervention effects or prove that changing a variable will change the outcome.

## 10. Next Validation Step

Recommend the next experiment, quasi-experiment, effect-estimation design, or data collection step.
