---
created: 2024-09-26T21:42
updated: 2026-09-28T15:51
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
---
Status: #adult 
Tags: [[economics]] [[math]]
# The partnership game
**Details**
Two partners split profits 50–50; think of a law firm, or two students on a problem set. Each chooses an effort level sᵢ anywhere from 0 to 4. This is the course's first game with a continuum of strategies.

The firm's profit is 4(s₁ + s₂ + b·s₁s₂), where b is between 0 and 1/4. The b·s₁s₂ term is synergy: each partner's effort is worth more when the other also works, which is the reason to work as a team at all. Each partner gets half the profit and pays an effort cost equal to their own effort squared. So Player 1's payoff is

u₁ = 2(s₁ + s₂ + b·s₁s₂) − s₁²

and Player 2's payoff is the same with s₂² subtracted instead. The subtraction in this situation is merely a cost, as without cost it would be a simple problem: the more you work, the more you get. And well real life just doesn’t work like that.

With infinitely many strategies you can't draw a line for each one, so the best response comes from calculus:

	•	Player 1 treats s₂ as fixed and picks s₁ to maximize u₁.
	•	Set the derivative with respect to s₁ to zero: 2(1 + b·s₂) − 2s₁ = 0, so ŝ₁ = 1 + b·s₂.
	•	The second derivative is −2, so this is a maximum.
	•	By symmetry, ŝ₂ = 1 + b·s₁.

In words, the best effort is where one more unit adds as much to your share of the profit, 2(1 + b·s₂), as it adds to your cost, 2s₁. Best responses rise with the partner's effort, because synergy makes your work pay more when they work harder.

Take b = 1/4, so each best response is 1 + s/4. Now apply the rule from the penalty-kick note and delete strategies that are never a best response:

Round	Efforts still possible (either player)	Reason
Start	0 to 4	All strategies
1	1 to 2	The partner's effort is 0 to 4, so 1 + s/4 runs from 1 to 2
2	1.25 to 1.5	The partner's effort is now 1 to 2
3	1.3125 to 1.375	The partner's effort is now 1.25 to 1.5
…	shrinks toward 4/3 ≈ 1.33	

As with iterated dominance, the efforts deleted in round 2 are best responses to something. But they are best responses only to efforts already deleted in round 1. Polak drew this as boxes within boxes, each a smaller copy of the last, closing in on the point where the two best-response lines cross. At that point each partner's effort is a best response to the other's: s* = 1 + b·s*, so s* = 1/(1 − b). That is 4/3 when b = 1/4.


**Supporting Content**


---
## References
[[Payoffs define the game]]
[[Dominance of Finance Capital]]
[[Weak Dominance]]

## Questions

