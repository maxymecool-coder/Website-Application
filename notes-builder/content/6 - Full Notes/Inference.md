---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2025-03-06T19:43
created: 2024-09-26T21:42
---
Status: #baby 
Tags: [[AI]]
# Inference
**Details**
These are options that can influence the conversion process. They can improve the output quality and reduce artifacting if configured appropriately 

Transpose (Pitch) adjust the tones of the voice, modify this until it matches the tone of the model. 

Search Feature Ratio (Index Rate) which determines the level of the influence of model’s .INDEX file. Higher values will apply more of its characteristics, lowering can reduce artifacting Pitch Extraction Algorithm Basically converting the vocals. The majority are obsolete so focus on RMVPE and Mangio-Crepe. 

RMVPE is fast, decent quality but usually sounds a bit harsh but its convenient and produce better with harmonic-rich voices/fuller voices. 

Mangio-Crepe: Its Crepe but able to adjust the hop_length. It determines the time th voice takes to get to a note, the lower the value, the more detailed results but also the longer the process. Its especially useful when the audio performs drastic note shifts and if the audio is extremely clean. (Also better with soft, whispery or voices with feminine timbres. Dont lower below 64 because that can make voice cracks. 

Protect Voiceless Consonants: As the name suggests, it remove breathing sounds which can cause artifacting. (0.5 disables it) 

Volume Envelope (Remix Mix Rate) It controls the loudness of the output, the closer to 0 the closer it is to the input audio. The closer to 1, the closer it is to the dataset. 

Split Audio Gives a faster inference and more consistent volume. It splices the audio into smaller parts and infers them each, uniting them at the end. This is way faster than normal so its just recommended.

**Supporting Content**


---
## References
[[Epochs and Overtraining]]

## Questions

