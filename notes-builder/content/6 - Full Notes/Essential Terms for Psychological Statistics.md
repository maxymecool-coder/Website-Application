---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2025-12-02T16:47
created: 2024-09-26T21:42
---
Status: #adult 
Tags: [[statistics]] [[psychology]] [[3 - Tags/reading]]
# Essential Terms for Psychological Statistics
**Details**
## Core basics

- Sample vs population: The people actually studied (sample) vs everyone we care about (population).
- N (or n): How many people/observations. Bigger N = more precise.
- Variable types:
    - Continuous (height, score),
    - Categorical (male/female; yes/no),
    - Ordinal (Likert 1–5).

## Describing data

- Mean: Usual “average.”
- Median: Middle value; ignores extreme outliers.
- Standard deviation (SD): Typical spread around the mean. If M=70, SD=10, most scores are ~60–80.
- Range/IQR: Range = max–min. IQR = middle 50%; both describe spread.
- z-score: How many SDs a value is from the mean (z=1 = one SD above average).

## Significance and uncertainty

- Null hypothesis (H0): “No real effect/difference.”
- p-value: If H0 were true, how surprising are these data? Smaller p = more surprising. p<.05 is the common “significant” cutoff, not a magic truth machine.
- Alpha (α): Your chosen cutoff for “significant” (often .05).
- Type I error: False alarm (saying there’s an effect when there isn’t).
- Type II error: Miss (failing to spot a real effect).
- Power (1−β): Chance to detect a real effect (aim ~80%). Bigger samples = more power.
- Standard error (SE): How wobbly an estimate is. Smaller SE = more precise.
- Confidence interval (CI): Estimate ± wiggle room. A 95% CI is a plausible range for the true value. Narrow = precise. If a 95% CI for a difference doesn’t include 0, that’s typically “significant.”

## Effect size (how big is it, in practical terms?)

- Cohen’s d: Difference between two group means in SD units.
    - ~0.2 small, ~0.5 medium, ~0.8 large (rough guides).
- Correlation (r): Strength of a relationship (−1 to +1).
    - ~.10 small, ~.30 medium, ~.50 large.
- R-squared (R²): Percent of outcome variation a model explains (e.g., R²=.25 → 25%).
- Eta-squared (η²): Percent of variation explained by a factor (ANOVA version of R²).
- Odds ratio (OR): For yes/no outcomes. OR=1 no difference; OR=2 = double the odds; OR=0.5 = half the odds.
- Beta (β): Regression slope. Standardized β says “how many SDs Y changes per 1 SD change in X.”

## Common tests you’ll see

- t-test: Compare two means.
    - Independent: two different groups.
    - Paired: same people twice (pre/post).
- ANOVA (F-test): Compare 3+ means or multiple factors.
    - One-way, two-way, repeated-measures, or mixed.
    - ANCOVA = ANOVA while adjusting for a covariate.
- Chi-square (χ²): Are categorical variables related? (e.g., treatment vs improved yes/no)
- Correlation:
    - Pearson’s r: linear relation between continuous variables.
    - Spearman’s ρ: rank-based (for skewed/ordinal data).
- Regression:
    - Linear: predicts a continuous outcome (test score).
    - Logistic: predicts a yes/no outcome (quit vs not).
- Nonparametric stand-ins (when assumptions fail):
    - Mann–Whitney/Wilcoxon, Kruskal–Wallis, etc.

## Assumptions (quiet rules the tests rely on)

- Normality: Data roughly bell-shaped (mostly matters for small samples).
- Equal variances: Groups have similar spread (you’ll see “Levene’s test”).
- Independence: One person’s score doesn’t depend on another’s (watch for clustered data like students in classes).
- Sphericity (repeated-measures ANOVA thing): Variances of differences are similar (“Mauchly’s test”). If broken, papers use corrections like Greenhouse–Geisser.

If assumptions are shaky, researchers might transform data, use robust/nonparametric tests, or switch models.

## Multiple tests problem

Running many tests inflates false positives (p-hacking risk). Fixes:

- Bonferroni, Holm, FDR: Adjust p-values or the cutoff.
- Pre-registration: Promises the analysis plan ahead of time.

## Measurement (super important in psychology)

- Reliability = consistency.
    - Cronbach’s alpha (α): Internal consistency for a questionnaire; ~.70+ is often acceptable; >.95 can mean items are redundant.
    - Test–retest: Stable over time.
    - Inter-rater (e.g., Cohen’s κ, ICC): Raters agree with each other.
- Validity = are we measuring what we think?
    - Construct validity (overall), convergent (agrees with similar measures), discriminant (not the same as different constructs), criterion (predicts outcomes).
- Factor analysis:
    - EFA: Explore how items group into factors.
    - CFA: Confirm a factor structure; common fit indices: CFI/TLI (~~>.90–.95 good), RMSEA (~~<.06–.08 lower is better), SRMR (~<.08 lower is better).
- Latent variables: Unseen traits (like “anxiety”) estimated from items.
- Mediation and moderation:
    - Mediation: X affects Y through M (indirect effect; often tested with bootstrapped CIs).
    - Moderation: The effect of X on Y depends on Z (an interaction).

## Designs you’ll read about

- Between-subjects: Different people in each condition.
- Within-subjects: Same people in all conditions (more power; watch order effects).
- Mixed design: Both together.
- Random assignment vs random sampling: Assignment = who goes to which condition; sampling = who gets into the study in the first place.
- Covariates/confounds: Extra variables adjusted for (ANCOVA, regression).
- Clustered data: People nested in groups (classes, clinics). Use multilevel/mixed models with random effects.

## Bayesian terms (when you see them)

- Prior: What you believed before the data.
- Posterior: Updated belief after seeing data.
- Bayes Factor (BF): How much data favor one model over another (e.g., BF10=5 means data are 5× more likely under the alternative than the null).
- Credible interval: Bayesian version of an interval—“there’s a 95% probability the true value is in here” (different philosophy than CI).

## Meta-analysis and replication

- Meta-analysis: Combines many studies to estimate an overall effect.
    - Fixed vs random effects: Assume one true effect vs effects vary across studies.
    - Heterogeneity (I²): How much effects differ (25% low, 50% moderate, 75% high).
    - Publication bias: Missing null studies; checked with funnel plots.
- Replication: Re-do the study to see if it holds up.

## How to read a result quickly

- Look for the effect size (d, r, OR, R²) + its 95% CI. That tells you “how much” and “how sure.”
- Check N (was it big enough?) and power if reported.
- p-values: Treat p<.05 as “worth a look,” not “truth.” Many tests? Look for corrections.
- Measurement: Are the scales reliable/valid? (α reported? CFA fit ok?)
- Design: Within vs between? Randomized? Any obvious confounds?
- Assumptions/robustness: Did they check them or use appropriate methods?
- Practical meaning: Would this matter in real life, not just on paper?

**Supporting Content**


---
## References
[[Approaches to Research#Approaches to Research]]

## Questions

