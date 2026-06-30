# Custom Score And Advanced DoubleML API Report Template

## Causal Estimand
State the target parameter and the model assumptions. Explain why a built-in DoubleML score is or is not sufficient.

## Score Definition
Write the score as $\psi(W; \theta, \eta) = \psi_a(W; \eta)\theta + \psi_b(W; \eta)$. Include the callable function signature and all nuisance inputs.

## Orthogonality Argument
Explain why the score is Neyman-orthogonal. If the score is not orthogonal, do not present it as a DoubleML-style robust estimator.

## Reproducibility Checks
Document sample splitting, random seeds, learner settings, and whether external nuisance predictions were supplied.

## Validation Results
Report known-score recreation, score reconstruction, final score mean, nuisance diagnostics, and any simulation checks with known truth.

## Unsupported Or Limited Features
Document any DoubleML features that are unavailable for callable scores in the installed version.

## Decision Boundary
State what the custom score supports and what still needs theory, robustness checks, or experimental validation.

Key estimate from this lesson:
- Built-in PLR estimate: 1.2852
- Callable equivalent estimate: 1.2852
- Priority-weighted callable estimate: 1.2890
- True $\theta_0$ in simulation: 1.2500
