# Final Summary: Interference and Spillover Effects in Recommendation Slates

## Question

This analysis studies what happens when a lower-ranked item is promoted inside a recommendation slate. The causal issue is interference: promoting one item can affect other items because slate attention is limited.

## Data and Design

MovieLens 32M was used as a realistic user-item preference dataset. Since MovieLens does not contain real impression logs or promotion assignments, the workflow constructed simulated recommendation slates, selected focal items, randomized focal promotion at the slate level, and generated outcomes from an explicit competition model.

## Main Finding

The promoted focal item gained engagement, but the full slate lost value after competitor displacement was included.

- Direct focal item effect: 0.172 simulated click-rate lift.
- Same-cluster competitor spillover: -0.058.
- All non-focal spillover: -0.044.
- Total slate effect: -0.308 simulated clicks per slate.

In product units, the focal item gained 171.6 simulated clicks per 1,000 promoted slates, while same-cluster competitors changed by -145.4 and other competitors changed by -334.0. The net total slate effect was -307.8 simulated clicks per 1,000 promoted slates.

## Advanced Modeling

Flexible outcome models were used to predict slate-level outcomes and estimate conditional net promotion effects. XGBoost had the best held-out RMSE at 1.405 clicks per slate. A cross-fitted LightGBM AIPW estimate was -0.304, close to the randomized total-effect estimate of -0.308. The best evaluated targeting rule was `Promote only predicted-positive slates`, with -3.7 oracle lift per 1,000 eligible slates.

## Recommendation

Do not evaluate promotion policies using promoted-item gains alone. When items compete for visibility, report slate-level total effects and monitor substitute or displaced-item spillovers. Advanced models can help target safer promotions, but they should be validated against randomized or valid off-policy benchmarks.

## Limitations

The numerical results are from a simulation built on MovieLens ratings, not a real production experiment. Genres are coarse substitute clusters, and the outcome mechanism is assumed. The value of the work is the transferable causal workflow: define interference, randomize at the right level, decompose direct and indirect effects, and evaluate policies by net slate value.
