---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2026-10-04T22:35
created: 2024-09-26T21:42
---
Status: #adult 
Tags: [[economics]]
# Production functions
**Details**
This is the first variable we will discuss regarding production theory. It is basically where products come from. Similar to how consumers want to maximize how much they get from products, manufacturers do the same.

Profits depend on three things: consumer demand, the costs of production, and competition. In the standard model, demand and competition are out of the firm's hands. (How advertising can shape demand, and how monopoly changes competition, come later.) What the firm controls is its costs, so Gruber treats maximizing profit as minimizing cost. Strictly, minimizing cost only tells you the cheapest way to make a given amount. How much to make also depends on revenue, which comes in later lectures.

Now we will treat the firm as a black box; that means we can only know what goes into the firm and what comes out. Whatever they do with it? We won't know. The course uses two inputs:

- **Labor (L):** hours worked at the firm. Its price is the wage.
- **Capital (K):** everything else, such as machines, buildings and land. Its price is the _rental rate_.

Think of both as rented. The wage is the rent on an hour of a worker's time, and the rental rate is the rent on a machine. (Firms owning machines comes later.) And we will now make it as. If these two are cookies and pizza slices.

The production function is q = f(L, K). It plays the role the utility function played for consumers: it turns inputs into output instead of goods into happiness. It's easier to picture than utility, because it's just technology. Lowercase q is one firm's output; uppercase Q is the whole market's.

Inputs are either _variable_ (easy to change) or _fixed_ (hard to change soon):

- **Short run:** the period in which some inputs are fixed.
- **Long run:** the period in which all inputs can change.

(Of course, in practice it isn't like this, but for simplicity). In the short run, q = f(L, K̄), with capital fixed at K̄. The key number is the _marginal product of labor_, MPL = dq/dL: the extra output from one more worker. The assumption is _diminishing marginal product_: each extra worker still adds output, but less than the one before. In symbols, dq/dL > 0 (local non-satiability) but d²q/dL² < 0.

His example is digging a hole with one shovel. A second worker might nearly double the pace by taking shifts, but a third probably doesn't triple it. By the hundredth worker, people mostly wait their turn. Rotating faster still helps a little, so 100 workers beat 90, but the hundredth adds far less than the second. In the long run you'd buy more shovels and wheelbarrows. The pattern isn't guaranteed (the second worker might be as good as the first), but it's the normal case.

Here's the math with the lecture's function and one shovel. With K = 1, q = √L. One to four workers produce 1, 1.41, 1.73 and 2 units, so each worker adds 1, then 0.41, 0.32 and 0.27. The derivative says the same thing in general: MPL = ½√(K/L), which falls as L rises.

And of course, just the same as consumer theory, we also have indifference curves, which are called isoquants in this case. They behave just like those curves and display all possibilities you can get one result.

The shape of an isoquant depends on how well the inputs substitute for each other, as a student guessed:

- **Perfect substitutes, q = L + K:** straight-line isoquants, since only the total count of units matters. Gruber's joke example is Harvard graduates and Beanie Babies.
- **Perfect complements, q = min(L, K):** L-shaped isoquants. Think of cereal and cereal boxes: every unit of cereal needs a box, and extra cereal without boxes just sits there. These are the production version of left and right shoes.
- **Real cases** fall in between, with curved isoquants (Figure 5-3).

And similar to [[Marginal Rate of Substitution]], we also have the _marginal rate of technical substitution_ (MRTS): the rate at which you can swap labor for capital and keep output the same. It comes from the same proof as the MRS. Moving along an isoquant, output doesn't change, so the output gained from extra labor cancels the output lost from less capital:

MPL × dL + MPK × dK = 0, so MRTS = dK/dL = −MPL/MPK

MPK, the marginal product of capital, also diminishes: with one worker, each extra shovel adds less. For q = √(L·K), MPL = K/(2√(L·K)) and MPK = L/(2√(L·K)), so the MRTS is −K/L. On the q = 2 isoquant:

- **At A (1 worker, 4 shovels),** the MRTS is −4. At the margin, a worker can stand in for four shovels.
- **At B (2, 2),** it's −1.
- **At C (4 workers, 1 shovel),** it's −¼. At the margin, a shovel can stand in for four workers.

**Supporting Content**
One difference isn't in the lecture. Output is a real quantity, so 4 units really is twice 2 units, whereas utility numbers only rank bundles. That's what makes returns to scale, below, a meaningful question.

---
## References
[[The Labor Theory of Value]]

## Questions

