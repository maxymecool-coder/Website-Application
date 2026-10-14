---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2026-06-19T11:58
created: 2024-09-26T21:42
---
Status: #adult 
Tags: [[statistics]] [[psychology]]
# The empirical rule
**Details**
For a normal distribution it pays to memorize roughly how much of the data sits within a given number of standard deviations of the mean, because it lets you sanity-check any probability calculation at a glance. The area from the mean out to +1 SD is about **34%**; by symmetry the same holds out to −1 SD, so **±1 SD captures ≈ 68%** of scores. **±2 SD captures ≈ 95%**, and **±3 SD captures ≈ 99%** — so a z-score beyond ±3 is genuinely rare (you would be more extreme than ~99% of the population).

As these areas are quoted in deviation, you can apply them to any normal curve. You could even convert them into z-scores with x = μ + z·σ: on a test with mean 70 and SD 9, a score exactly 3 SD above the mean is 70 + 3×9 = 97. Use the rule as a reality check _before_ trusting an exact figure pulled from a table

**Supporting Content**


---
## References
This rule can obviously be applied to the table and z-scores themselves. The area of the curve can be calculated through the equation: (bigger slice) − (smaller slice); e.g. P(0.6 ≤ z ≤ 1.09) = 0.3621 − 0.2257 = 0.1364. A **tail** beyond z = 0.5 − (slice from 0 to z); e.g. P(z ≥ 1.09) = 0.5 − 0.3621 = 0.1379. Everything **below a positive z** = 0.5 + (slice from 0 to z); e.g. P(z ≤ 1.09) = 0.5 + 0.3621 = 0.8621. Negative z's need no new numbers — by symmetry the slice from 0 to −z equals the slice from 0 to +z; the sign only says which side.

## Questions
[[Variance and Standard Deviation]]
[[Probability density]]
