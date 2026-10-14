---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2025-03-06T19:40
created: 2024-09-26T21:42
---
Status: #baby 
Tags: [[AI]]
# Epochs and Overtraining
**Details**
Epoch is a measurement for the cycles that an AI model has been trained. Basically each time the AI goes over the dataset and learns from it is 1 epoch. There isnt really a method to know the right amount of epochs to use before training since it depends on the size, length and quality of the dataset. But if aimed at a quality model, its not convenient to input a semi-arbitrary amount, as that makes it prone to underfitting/overtraining. So the best way is to use a TensorBoard to determine how long one should train Overtraining is when an AI learns the dataset too well to the point it centers too much around it and replicates unnecessary data, which it will use to learn again (this data isn’t exactly the highest of quality since its not actually the original). In technical terms, its when an AI stops learning the patterns of the data and just memorizes the data from which it created.

**Supporting Content**


---
## References
[[Datasets]]

## Questions

