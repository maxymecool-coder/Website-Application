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
Status:
Tags: [[economics]]
# Long-run costs
**Details**
Moving on to long-run costs, we would have to expand the firm's optimization problem. In the short run, capital had always been fixed at some level of K, and the firm could only adapt to demand swings by labor (hiring or firing workers). But in the long run, capital is fully flexible. This allows an essential economic rule: long-run costs will always be at the lower bound of short-run costs, because firms have more freedom in their decisions.

Graphically, the long-run average cost curve forms the lower envelope of all possible short-run average cost curves. Imagine a firm facing three potential plant sizes, each represented by a distinct short-run average cost curve: $SRAC_1$for small output, $SRAC_2$ for intermediate output, and $SRAC_3$ for massive production. If the firm anticipates low output $q_1$, building plant size $1$ is optimal. If demand surges to $q_3$, running that small plant requires hiring enormous amounts of labor, forcing the firm deep into diminishing marginal returns and driving costs skyward. In the long run, the firm can construct plant size $3$, lowering its average cost back down to the frontier. Gruber describes the long run as a sequence of short-run games: in every period, the firm picks a plant scale, operates along that short-run cost curve, and then evaluates whether to re-optimize its capital stock for the next cycle.

Gruber ties this envelope logic directly to Elon Musk and Tesla. When Tesla began ramping up manufacturing in 2013, management had to commit to a specific battery factory capacity, planning for a projected demand of roughly 20,000 vehicles by 2017. Musk had effectively locked the firm into $SRAC_1$. Instead, consumer demand exploded, producing a backlog of 200,000 reservations that the existing plant could not service efficiently. Operating on the upward-sloping limb of an undersized short-run curve, Tesla incurred major production bottlenecks. To solve this, Tesla transitioned to $SRAC_3$ by constructing the massive Gigafactory in Nevada, capable of supplying 500,000 vehicles annually. Yet Gruber notes the lingering risk: if consumer sentiment shifts and demand contracts, Tesla will find itself stranded on the steep left tail of an oversized plant, burdened by massive capital overhead until it can re-optimize again.

To formalize this concept in mathematical terms and work to cost minimization, producer theory constructs the isocost line, the direct analogue to the consumer's budget constraint. An isocost line depicts all combinations of labor $L$ and capital $K$ that generate the identical total expenditure, $C = wL + rK$. Solving for capital gives $K = (C/r) - (w/r)L$, showing that the vertical intercept is $C/r$ and the slope is $-w/r$. With input prices $w = \$5$ and $r = \$10$, the slope is $-5/10 = -1/2$. This slope captures the economic opportunity cost of factors: along any given expenditure line, hiring one additional worker requires surrendering half a unit of capital.

Similar to consumer theory, where the market allows you to exchange goods and your own marginal utility, minimizing the cost of producing any targeted output requires finding the point where the isoquant is tangent to the lowest achievable isocost line. At this tangency, the slope of the isoquant (the marginal rate of technical substitution, or $MRTS$) must equal the slope of the isocost line (the negative input price ratio):

$$MRTS = -\frac{MP_L}{MP_K} = -\frac{w}{r}$$

For the lecture's production function $q = \sqrt{L \cdot K}$, the marginal products derived in Lecture 5 are $MP_L = K / (2\sqrt{LK})$ and $MP_K = L / (2\sqrt{LK})$. Their ratio simplifies to $MRTS = -K/L$. Setting this equal to the input price ratio $-w/r = -1/2$ yields the optimal capital-labor ratio $K/L = 1/2$, or $L = 2K$. The firm should always employ twice as many workers as machines. Intuitively, the market dictates that labor costs half as much as capital ($w/r = 1/2$), while technological trade-offs dictate an exchange rate of $K/L$; cost minimization balances the two.

This is where they diverge however, because in producer theory, we don't have a budget constraint. So now we have to learn how do we achieve the optimal budget constraint and product amount.

**Supporting Content**
[[Marginal Rate of Substitution]]
[[Marginal Utility]]
[[Production functions]]
[[Returns to scale]]

---
## References


## Questions

