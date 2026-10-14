---
created: 2024-09-26T21:42
updated: 2026-09-28T15:52
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
---
Status: #adult 
Tags: [[economics]] [[math]]
# Penalty kick game
**Details**
In Polak's penalty-kick game, the shooter kicks Left, Middle or Right, and the goalie dives Left or Right (for now the goalie can't stay put). The shooter's payoff is the chance of scoring, written in tens, so 4 means 40%. The goalie's payoff is the negative of the shooter's. Rows are the shooter's kicks and columns are the goalie's dive; the table shows only the shooter's payoff:

	Goalie dives Left	Goalie dives Right
Kick Left	4	9
Kick Middle	6	6
Kick Right	9	4

Nothing is dominated. Compare within each column:

	•	Against a goalie diving Left, Right is best (9), then Middle (6), then Left (4).
	•	Against a goalie diving Right, the order flips.

So Middle beats Left in the first column but loses to it in the second, and the same goes for Middle against Right. The class split roughly evenly among the three kicks.

Best responses get further. Let p be the chance you give the goalie diving Right. Each kick's expected payoff is then a line in p:

	•	Left: 4 + 5p, rising from 4 to 9.
	•	Middle: 6, flat.
	•	Right: 9 − 5p, falling from 9 to 4.

Chance goalie dives Right (p)	Left	Middle	Right	Best response
0	4	6	9	Right
1/2	6.5	6	6.5	Left and Right tie
1	9	6	4	Left

Left and Right cross at p = ½, where each is worth 6.5. Whichever of the two is higher is never below 6.5, while Middle is stuck at 6. So Right is the best response when p < ½, Left is the best response when p > ½, and Middle is the best response to no belief at all.

So the lesson? Don’t kick to the middle cause it’s never the best. Threshold is always fulfilled by the two options anyways.
What the model leaves out, per the class:

	•	Footedness. Kicking across your body, to your "natural side," is easier. For a right-footer, that's the goalie's right.
	•	The goalie can stay in the middle. This is left for the problem set.
	•	Height. The kick can go high or low.
	•	Power versus placement. See below.

One suggested gap isn't a real one: timing. Whenever the decision is made, neither player sees the other's choice in time, so the game works as simultaneous.

Real data come from Chiappori and co-authors (AER, 2002), drawn half from the Italian league and half from the French. The sides are relabeled as the kicker's natural side and the other side:

	Goalie dives to kicker's natural side	Goalie dives to other side
Kick to natural side	63.6%	94.4%
Kick to other side	89.3%	43.7%

The natural side is easier. When the goalie guesses correctly, a natural-side kick still scores 63.6% of the time, against 43.7% for the other side. But nothing is dominated:

	•	Against a goalie diving to the natural side, kicking the other way is better (89.3 vs 63.6).
	•	Against a goalie diving the other way, the natural side is better (94.4 vs 43.7).

Polak's made-up numbers were close. But again, there are many more factors affecting the chances such as the player’s habits and abilities.

**Supporting Content**


---
## References
[[Payoffs define the game]]
[[Weak Dominance]]

## Questions

