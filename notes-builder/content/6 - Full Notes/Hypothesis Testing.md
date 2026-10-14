---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2026-06-21T17:35
created: 2024-09-26T21:42
---
Status: #adult 
Tags: [[statistics]] [[psychology]]
# Hypothesis Testing
**Details**
This method is basically arguing with yourself. You suspect two groups differ, but you cannot measure if theres an effect directly, because sampling error guarantees some difference every time. So you assume the null hypothesis, that they are one population, then compute how often chance alone would produce a result this extreme. The p-value is exactly that probability, it shows the chance of the data being at least this extreme if the null were true. It would then provide supporting evidence for the research hypothesis being true too via Occam's Razor.

There are a few ways one can go at this: set a cutoff point. You'll reject only if a result would occur less than alpha (usually 5%, sometimes 1%) of the time under the null, which for a one-tailed 5% test is z = 1.645. Then either compare statistics — z = 2.2 beats 1.645, so reject — or compare probabilities — P(Z ≥ 2.2) ≈ 0.014 is below 0.05, so reject. Same conclusion, mirror images across the table. In plain terms, the sample mean has to sit at least 1.645 standard errors above μ. You can draw that same line in raw score units by inverting the formula: x = μ + z·σ_x̄ = 50 + 1.645×5 ≈ 58.2, so any sample mean past 58.2 rejects, and 61 clears it. Alpha itself is convention, partly cultural: social science leans on 0.05, stricter fields use 0.01. A fair rule of thumb — cheap, repeatable experiments can drive p down just by adding data, so they should hold themselves to a stricter alpha.

**Supporting Content**


---
## References
[[Variations of Hypothesis Testing]]
[[The Z-test]]

## Questions

