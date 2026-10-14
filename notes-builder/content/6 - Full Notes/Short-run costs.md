---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2026-10-03T22:20
created: 2024-09-26T21:42
---
Status: #adult 
Tags: [[economics]]
# Short-run costs
**Details**
Suppose a firm rents capital at rate $r$ and hires labor at wage $w$. In the short run with capital fixed at $\bar{K}$, total expenditure as a function of output $q$ is $C(q) = r\bar{K} + w L(q)$. The only choice variable in the short run is labor, and Gruber notes that he treats hours of labor and the count of workers interchangeably as the measure of labor input unless specified otherwise. To obtain the explicit cost function $C(q)$, you invert the short-run production function to express the required labor $L$ in terms of output $q$, and then substitute that expression directly into the cost equation.

Using the lecture's working example, let the production function be $q = \sqrt{L \cdot K}$, with input prices set at wage $w = \$5$ and rental rate $r = \$10$. Holding capital fixed at $\bar{K} = 1$, the production function simplifies to $q = \sqrt{L}$, which inverts to $L = q^2$. Substituting this into the expenditure relationship yields the short-run total cost function $C(q) = 10(1) + 5(q^2) = 10 + 5q^2$. The function maps the technological requirements of production straight into dollars: producing twice as much output does not merely double labor costs, but quadruples them because of diminishing returns to the single variable input.

From this cost function, Gruber constructs several foundational metrics. Fixed costs ($FC$) are expenses that do not vary with output in the short run, which in this case equals the $10$ spent on fixed capital. Variable costs ($VC$) are the expenses that fluctuate directly with production, represented here by $5q^2$. Total cost ($TC$) is simply their sum, $10 + 5q^2$. Marginal cost ($MC$) is the differential of total cost with respect to quantity, $dTC/dq$. Because fixed costs do not change when output shifts, $dFC/dq = 0$, meaning marginal cost is identical whether differentiated from total cost or variable cost: $MC = dVC/dq = 10q$. Average cost ($AC$ or $ATC$) is total cost divided by output, which breaks down into average fixed cost ($AFC = 10/q$) plus average variable cost ($AVC = 5q$).

This U-shape explains why marginal cost must cross average cost precisely at its minimum point. The intuition is purely mathematical and mirrors a grade point average. When the marginal cost of producing the next unit is below the current average cost, that additional unit pulls the overall average downward. Once the marginal cost of producing the next unit exceeds the current average cost, that next unit pushes the average upward. It follows that the turning point—the absolute minimum of average cost—must occur exactly where marginal cost equals average cost. Setting $10q = (10/q) + 5q$leads to $5q = 10/q$, which simplifies to $q^2 = 2$, or $q = \sqrt{2} \approx 1.41$, which Gruber rounds to roughly $1.5$ in lecture.

Marginal cost and the marginal product of labor are two sides of the same coin. Starting from the short-run cost relation $C = r\bar{K} + wL$ and differentiating with respect to quantity gives $dC/dq = w \cdot (dL/dq)$. Because the marginal product of labor is $MP_L = dq/dL$, the inverse function rule establishes that $dL/dq = 1 / MP_L$. Substituting this in yields $MC = w / MP_L$. The economic intuition is immediate: producing one extra unit of output requires $1 / MP_L$additional hours of labor, and each hour costs the wage $w$. When workers are highly productive, an additional unit requires very little labor, keeping marginal cost low. As diminishing marginal returns set in and $MP_L$ falls, each subsequent unit demands progressively more labor hours, causing short-run marginal cost to rise.

We are then introduced to sunk costs. They are basically costs that once you buy, you never get it back regardless of what happens. Its quite an essential and yet difficult concept to understand but yeah it's just gone bro. But at the end it is still separate from opportunity costs rather than as if we are saying the opportunity cost is also zero in this situation.

The fundamental decision rule of economics is that sunk costs are sunk, meaning they must be entirely ignored in forward-looking decisions. Because past expenditures cannot be altered by any present or future choice, factoring them into a decision is irrational. To illustrate how counterintuitive this is, Gruber shares his experience buying two tickets to see the rock band Journey in Mansfield, Massachusetts, for $\$125$ each ($\$250$ total) to see their replacement vocalist discovered on YouTube. After reviewing the concert setlist, he realized he only cared for three songs and decided that sitting through a ninety-minute show was not worth his evening.

He considered selling the tickets on StubHub, raising the question of how the $\$250$ purchase price should influence his listing price. The instinctive human response—which a student in the audience offered—is to try to recover the $\$250$. Gruber stresses that this is textbook sunk-cost fallacy. The $\$250$ is gone whether he attends, resells, or burns the tickets. The rational floor on his selling price depends entirely on his opportunity cost of going. If his subjective value of attending is zero because he would genuinely rather sit on his couch, he should be willing to part with the tickets for anything above zero dollars. If he values attending at $\$50$ a ticket, he should set $\$50$ as his reservation price: if the market pays more than $\$50$, he sells; if it pays less, he attends. What he paid in the past does not enter the arithmetic.

When a student asked whether intent separates fixed costs from sunk costs, Gruber acknowledged that the line can feel fuzzy. If you buy a building intending from the outset to hold it as an asset and eventually resell it, the expense is an avoidable fixed cost. If you buy a non-transferable service or an asset with zero salvage value, it is sunk immediately. He recalled being reprimanded by his own graduate school advisor when agonizing over non-refundable plane tickets: his advisor reminded him that the money was spent, and the only relevant consideration was the utility of taking the trip versus staying home.

**Supporting Content**


---
## References
[[Marginal Rate of Substitution]]
[[Marginal Utility]]
[[Long-run costs]]
[[Production functions]]

## Questions

