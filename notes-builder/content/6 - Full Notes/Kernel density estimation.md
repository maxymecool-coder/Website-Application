---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2026-06-16T00:26
created: 2024-09-26T21:42
---
Status: #adult 
Tags: [[statistics]] [[psychology]]
# Kernel density estimation
**Details**
Histograms are a crude way to estimate a distribution because of edge effects: every subject in a bin is counted as if they sat at the bin's midpoint. A grad student earning $31,000 in a $30–40k bin contributes exactly as if they earned $35,000; someone at $19,500 near an edge is likewise shoved to the bin's centre. Each data point is "weighed in a weird way," and the result is jagged and sensitive to where you happened to draw the bin boundaries.

And so to remove these bins, we can use kernel density estimation. Basically, we mark every point on the axis, and then we replace each point with a small _identical_ bell curve (a _kernel_) whose area is 1/n, where n is the sample size. Because there are n of them, the bumps' areas sum to n × (1/n) = 1, so the total is a legitimate probability density. Lastly, we can add the bumps together to see more accurately where the graph might have a group that has a lot of data points and such.

You would never build this by hand, but software does it instantly. In R you create the estimate with `density(Prestigeincome)‘(the‘income)` (the ` income)‘(the‘` selects the *income* variable inside the *Prestige* dataset) and overlay it on a histogram with `lines()`. A practical learning tip from the same demo: drive R through the R Commander GUI, then read the command-line code it auto-generates in the script window and edit *that* — a gentle on-ramp to R as a programming language, which is what it originally was.

**Supporting Content**


---
## References
[[Probability density]]

## Questions

