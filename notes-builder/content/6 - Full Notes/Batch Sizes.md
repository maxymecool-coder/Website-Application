---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2025-03-06T19:41
created: 2024-09-26T21:42
---
Status: #baby 
Tags: [[AI]]
# Batch Sizes
**Details**
It is the number of examples used in one iteration before updating the model’s parameters. Usually 8 is the best for most models. Smaller batch sizes will make gradients noisier and more unstable, its recommended only when the dataset is small, less diverse, repetitive,… it can lead to instability or noisy graphs. The only pro is the generalization, which MIGHT be improved. Bigger batch sizes will promote smoother, more stable gradients, its recommended when the dataset is big and diverse. Can lead to early overtraining or stuck graphs and the generalization might be worse.

**Supporting Content**


---
## References
[[Epochs and Overtraining]]

## Questions

