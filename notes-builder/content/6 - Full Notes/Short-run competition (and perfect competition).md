---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2026-10-04T20:50
created: 2024-09-26T21:42
---
Status: #adult 
Tags: [[economics]] [[market]]
# Profit Maximization under perfect competition
**Details**
Finally, we move on to how we decide how much of a product to make.
Market structures run between two extremes:

- **Perfect competition:** many firms selling identical goods. The course starts here.
- **Monopoly:** a single firm. This comes next.
- **Oligopoly:** a handful of firms. Gruber calls it his favorite word in economics, and it describes most real industries: there's more than one car company, but not a thousand. It comes after the midterm.

The technical definition of perfect competition is that every firm is a **price-taker**: nothing one firm does can move the market price, because each firm is tiny relative to the market. So the demand curve facing a single firm is perfectly elastic, horizontal at the market price p.

This is about one firm's demand (little q), not market demand (big Q). Demand for Eiffel Tower keychains overall isn't perfectly elastic, but demand for one seller's keychains is. If one firm's costs shift, its output changes but the price doesn't.

Three assumptions make firms price-takers:

1. Identical products.
2. Full knowledge of prices: every buyer knows every firm's price.
3. No transaction costs: buyers can easily shop at any firm.

No real market fits exactly; the extreme is a benchmark. eBay looks close for a standard item, like a particular chip or a shirt in a given size and style: the products match, prices are listed, and shopping is easy. In practice, it falls short in two ways:

- For years, eBay ranked listings by price without shipping. That makes shipping a _shrouded attribute_, a hidden part of the price.
- Few products are truly identical, so comparing them takes time, which is itself a transaction cost.

Gruber's favorite near-example is the hundreds of sellers on blankets around the Eiffel Tower, all offering the same keychain within sight of each other. After he taught it online, a student mailed him a bag of the keychains. The student reported that sellers right by the tower all charged exactly the same price, while those further away charged differently. A different location makes it a different product.

A firm chooses quantity to maximize profit, π(q) = R(q) − C(q): revenue minus cost. Setting the derivative to zero gives

dR/dq = dC/dq, or marginal revenue = marginal cost (MR = MC)

That's profit maximization in one equation, and it holds in any market. Under perfect competition, every extra unit sells for the market price, so MR = p and the rule becomes

p = MC

Gruber's example uses the cost function from Lecture 6, C = 10 + 5q², with a price of $30. The 10 is the _fixed cost_, which you pay whatever you produce. The 5q² is the _variable cost_, which grows with output. Marginal cost is MC = dC/dq = 10q, so p = MC gives 10q = 30, and q* = 3.

The unit-by-unit view shows why. Each extra unit brings in $30; the last column is what that unit adds to cost:

|Units|Revenue|Cost|Profit|Cost of that unit|
|---|---|---|---|---|
|0|0|10|−10||
|1|30|15|15|5|
|2|60|30|30|15|
|3|90|55|35|25|
|4|120|90|30|35|

The first three units each cost less than the $30 they sell for, so each one raises profit. The fourth costs $35, so it lowers profit.

Gruber's image is climbing a mountain in the clouds. You can't see the top, only whether your next step goes up or down, and you're at the top when the next step goes down. The table steps in whole units. The derivative is the same test for a tiny next step, which is why the method also works with fractional amounts, as Gruber told a student.

Profit shows up on the cost-curve graph as a rectangle. Write profit as (revenue per unit − cost per unit) × number of units:

π = (p − AC) × q

Here AC = C/q is _average cost_, which works out to 10/q + 5q. At q = 3, AC = 10/3 + 15 ≈ 18.33. Each unit sells for 30 and costs 18.33 on average, so profit per unit is 11.67. The rectangle is 11.67 tall and 3 wide, so profit is 35. Gruber says 40 in class, but 11.67 × 3 = 35, which matches revenue of 90 minus cost of 55.

He then asked what a $10-per-unit tax does. The new cost function is C = 10 + 5q² + 10q. The common first answer, 20 + 5q², treats it as a single flat $10, which is wrong because the tax is paid on every unit.

- Marginal cost rises to 10q + 10, so p = MC gives 10q + 10 = 30, and q* = 2.
- The price hasn't changed. Output falls because each unit now costs more to make.
- Both sides of the profit rectangle shrink: fewer units, and less profit on each, since average cost rises too. In numbers (not given in the lecture), AC at q = 2 is 5 + 10 + 10 = 25, so profit falls from 35 to (30 − 25) × 2 = 10.

A flat $10 tax, by contrast, wouldn't change output at all. It doesn't touch marginal cost, so the firm still makes 3 units and simply earns 25 instead of 35.

The last short-run complication is whether to shut down. Losing money isn't, by itself, a reason to stop. Suppose the price falls to $10 (no tax). Then 10q = 10 gives q = 1. Revenue is 10 and cost is 10 + 5 = 15, so profit is −5. But if the firm produces nothing, it still owes the fixed cost and loses 10. Losing 5 beats losing 10, so it keeps producing.

In the short run, the fixed cost is _sunk_: you've already paid it whatever you do, so it shouldn't affect the decision. Staying open also keeps the option to fix your costs later, in the long run.

So the **shutdown rule** compares revenue with variable cost only. Shut down if

p × q < VC, or, dividing by q, p < AVC

where AVC = VC/q is _average variable cost_. Keep producing as long as the price covers average variable cost.

In this example the firm never shuts down. AVC = 5q²/q = 5q. A profit-maximizing firm produces q = p/10, so AVC = 5 × p/10 = 0.5p, which is always below p.

In the long run nothing is fixed, so there are no sunk costs to ignore. A firm that has fully re-optimized and still loses money should leave the industry.

**Supporting Content**


---
## References
[[Where demand comes from]]
[[Deriving supply]]

## Questions

