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
# The median people (i forgot) theorem
**Details**
Remember iterated deletion of dominated strategies? Yeah, so if we followed the method of doing so until the last possible instance, what we get would be a very small amount from what we had, rarely one though. However, we are missing critical context about how smart the people in the room really are.

The application is an election:
	•	Two candidates each pick a position from 1 (far left) to 10 (far right).
	•	Voters are spread evenly, 10% at each position.
	•	Each voter votes for the nearer candidate. If the candidates are equally near, that position's voters split half and half.
	•	Each candidate wants the largest vote share.


Is 2 dominated by 3? Not in the original game. Against an opponent at 1, standing at 2 gets 90% but standing at 3 gets only 85%. But once 1 and 10 are deleted, the opponent can't be at 1, so that column disappears:

Opponent at →	2	3	4	5	…
I'm at 2	50	20	25	30	…
I'm at 3	80	50	30	35	…

Now the "3" row is higher in every column. So the rounds go:

•	Round one deletes 1 and 10.
•	Round two deletes 2 and 9.
•	Round three deletes 3 and 8.
•	Round four deletes 4 and 7.

Only 5 and 6 remain, and between them it's a tie. The prediction is that candidates crowd the center, so the voters in the middle decide the election and therefore the policy. This is the median voter theorem (Anthony Downs, 1957, in political science). Polak's examples are:


The same model is older in economics, from Harold Hotelling (1929). Shops like gas stations bunch at the same junction instead of spreading out, because each is competing for the customers nearest to it.

The class listed what the model leaves out:

•	Voters aren't evenly spread.
•	Not everyone votes.
•	Primaries come before the general election.
•	Politics has more than one dimension: character, and separate issues like the environment or foreign policy.
•	There can be more than two candidates, and not voting works like an extra one.
•	Candidates can't just announce a position. Voters know their track records, so a claimed position isn't believed unless the candidate can commit to it.

But of course the model still has its uses, it is testing a very simple case, which is why its results are extremely clear and simplistic. It is still useful however as it proves a base case of the situation.

**Supporting Content**


---
## References
[[Iterated Dominance]]
[[Best response]]

## Questions

