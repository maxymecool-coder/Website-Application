---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2026-06-16T00:25
created: 2024-09-26T21:42
---
Status: #adult 
Tags: [[statistics]] [[psychology]]
# Describing distribution shape
**Details**
Before quantifying anything, you can describe a distribution's _shape_ in words along three axes.

**Modality** = number of peaks. _Unimodal_ has one peak; _bimodal_ has two (treat small wiggles as noise); a flat distribution with no peak, where every value is about equally likely, is _rectangular_ or _uniform_. A bimodal shape is diagnostic: it often means two subgroups are mixed together (e.g., men and women), hinting that you should split the data by some underlying variable.

**Symmetry / skew.** A symmetric distribution's two halves mirror each other (the bell curve is the type case). An asymmetric one has a tail stretching to one side, and that asymmetry is called skew, named for the direction the tail points. Positive (right) skew: the long tail runs toward high values — income is the classic case, because a floor effect at $0 blocks the left side while the right can run on to the very rich. Negative (left) skew: the tail runs toward low values — e.g., years of education or an easy test, where a ceiling bunches most scores high. (Mnemonic: point your fist's finger along the tail; the axis direction it points is the sign of the skew.)

**Kurtosis** = peakedness relative to the normal curve, holding variance fixed. High kurtosis (leptokurtic) is more peaked and has heavier tails; low kurtosis is flatter with lighter tails. The subtle part: two distributions can share the same variance yet differ in kurtosis. A past midterm asked students to draw a high-kurtosis curve on top of a normal one with the same variance and total area 1 — the trick being that you must move probability mass into both the peak and the tails while removing it from the shoulders (the intermediate values), so the area still integrates to 1.

**Supporting Content**


---
## References
[[Probability density]]
[[Kernel density estimation]]

## Questions

