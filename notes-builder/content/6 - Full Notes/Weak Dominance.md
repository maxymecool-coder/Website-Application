---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2026-09-28T15:50
created: 2024-09-26T21:42
---
Status: #adult 
Tags: [[economics]] [[strategy]]
# Weak Dominance
**Details**
Formally, a game in normal form has three ingredients:

- Players (i, j, …).
    
- Strategies. Each player has a set of possible strategies Sᵢ, and sᵢ is one strategy from that set. A strategy profile s is one strategy for every player, like the spreadsheet of everyone's chosen numbers.
    
- Payoffs. Player i's payoff Uᵢ(s) depends on the whole profile. Writing s₋ᵢ for everyone's choices except i's lets you split this into Uᵢ(sᵢ, s₋ᵢ): my choice against everyone else's.
    

For most of the course, we assume every player knows all strategy sets and payoffs.

In this notation, s′ᵢ is strictly dominated by sᵢ if Uᵢ(sᵢ, s₋ᵢ) > Uᵢ(s′ᵢ, s₋ᵢ) for every s₋ᵢ. Polak's abstract example (Player I picks the row, Player II the column; Player I's payoff first):

|   |   |   |   |
|---|---|---|---|
||Left|Center|Right|
|Top|5, −1|11, 3|0, 0|
|Bottom|6, 4|0, 2|2, 0|

Player I has nothing dominated: bottom is better against left, top against center. For Player II, center strictly dominates right (3 > 0 against top, 2 > 0 against bottom). Once right is deleted, nothing else is dominated, so dominance alone leaves this game unsolved.

Weak dominance: s′ᵢ is weakly dominated by sᵢ if Uᵢ(sᵢ, s₋ᵢ) ≥ Uᵢ(s′ᵢ, s₋ᵢ) for every s₋ᵢ, with > for at least one. Polak's example is Hannibal invading Italy with two battalions:

- The hard pass over the Alps costs him one battalion.
    
- Running into the defender costs another, and the defender can guard only one pass.
    

Hannibal's payoff is battalions that get through; the defender's is battalions destroyed:

|   |   |   |
|---|---|---|
||Defend easy|Defend hard|
|Attack easy|1, 1|2, 0|
|Attack hard|1, 1|0, 2|

The defender has no dominated strategy; they only care about matching the attacker so that they can defend. Most of them chose the easy pass because they are evaluating from Hannibal’s side. For him, the easy path dominates the hard one, since he will always get at least one battalion. Then, expecting the easy path, you would go for the easy one.

**Supporting Content**
The "weak dominance" is a bit more subtle than strict dominance due to the effect of loss not being as clear as the latter. And so it can be misleading/allow people to mistake it for a bad strategy.

---
## References
[[Iterated Dominance]]
[[Dominance, the Prisoner's Dilemma, and why cooperaation needs enforcement]]
[[Payoffs define the game]]

## Questions

