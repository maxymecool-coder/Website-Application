---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2026-01-18T18:11
created: 2024-09-26T21:42
---
Status: #adult 
Tags: [[Clinical Psychology]]
# Preventing Suicides from Machine Learning
**Details**
Suicide is the most lethal outcome of mental disorders, and much of the field have been dedicated to finding effective ways to prevent this outcome from happening. Due to recent technological advancements, people are using EMA (Ecological Momentary Assessment) to record the responses of surveys of participants to up to 6 times per day for up to 3 months.

The questions include the below with others about their emotions at the time throughout the day.

- **Suicidal Urges:** "Right now, how strong is your urge to kill yourself?" (Rated 0–10).
    
- **Suicidal Intent:** "Right now, how strong is your intention to kill yourself today?" (Rated 0–10).

They split the patient's data in half. They trained the model on the first 50% of the responses and tested it on the last 50% to see if early data could predict later data. This would then result in them using Gaussian models, which will learn upon the response that it predicts. This allowed the model to **continuously learn and update** as the patient's symptoms changed over time.

Surprisingly, the questions about moods did not help the model become more accurate in predicting, only the answers about urges and intents did help. Also, the best performing model was the simple Gaussian model, significantly outperforming the base models (machine learning).

- **Suicidal Urges:** GP models explained ~17% of the variance ($R^2 = 0.17$) vs. 10% for baseline models.
    
- **Suicidal Intent:** GP models explained ~12% of the variance ($R^2 = 0.12$) vs. 8% for baseline models.

**Supporting Content**
The model did though, not help with those who didn't report any suicidal intentions, urges.

---
## References
[[Essential Terms for Psychological Statistics]]

## Questions

