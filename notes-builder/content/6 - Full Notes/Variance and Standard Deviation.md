---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2026-06-19T00:05
created: 2024-09-26T21:42
---
Status: #adult 
Tags: [[statistics]] [[psychology]]
# Variance and Standard Deviation
**Details**
Variance measures **spread**: on average, how far each score sits from the mean. You take each deviation xᵢ − x̄, **square** it (so distances on either side of the mean both count as positive instead of cancelling), sum the squares, and average. In symbols, s² = Σ(xᵢ − x̄)² / (n − 1) = SS / (n − 1), 

The one wrinkle is the denominator. You divide by **n − 1**, not n, whenever you estimate the _population's_ variance from a sample. Dividing by n gives a _biased_ estimate that systematically **underestimates** the spread — because the sample mean is itself fitted to the data, the deviations come out a little too small — and the n − 1 correction repairs this (it can be proven, not just asserted; demo to come). You divide by the full n only in two cases: you genuinely know the population mean μ, or you only want to describe the sample with no inference about a population.

Standard deviation happens when you root whatever you just got from the equation above. This metric exist so that statisicians can eliminate the need for units and instead focus entirely on the statistics.

The concrete tool is the **z-score**: z = (x − x̄)/s, read as _how many standard deviations a score lies from the mean_. It is unitless, and you invert it with x = z·s + x̄. By construction a set of z-scores always has mean 0 and standard deviation 1, so any distribution can be redrawn on a common z-axis: a tall student at 77 inches is no longer "77" but z ≈ 2.8. This "in units of spread" language is what the rest of the course runs on — the coefficient of variation (spread relative to the mean), and later the t-test and ANOVA (_analysis of variance_) all work by dividing the spread out. What we usually care about is not raw width but _where a score sits relative to the spread_.

**Supporting Content**


---
## References
[[Kernel density estimation]]
[[Describing distribution shape]]

## Questions

