---
tags:
  - type/sketchnote
  - type/note
  - theme/xyz
template_type: Note
template_version: "1.27"
updated: 2026-10-04T20:48
created: 2024-09-26T21:42
---
Status: #adult 
Tags: [[economics]]
# Deriving demand
**Details**
Lecture 1 drew demand and supply curves and promised to explain where they come from. Lectures 2 and 3 built the pieces: preferences and the budget. This lecture puts them together. A demand curve shows how much of a good you want at each price. You get it by solving the consumer's problem again at each price

The method is the one from Lecture 3, and Gruber warns you'll repeat it until you're sick of it. Take U = √(C·S), income Y = $24, a slice at $4 and a cookie at $2. Two equations give the two unknowns:

**• Tangency:** MRS = −S/C must equal −Pc/Ps = −½, so S = C/2.

**• Budget:** 4S + 2C = 24.

Substituting gives C = 6 and S = 3.

Now raise the cookie price to $3. The tangency becomes S/C = ¾, and the budget becomes 4S + 3C = 24. Substituting S = ¾C gives 3C + 3C = 24, so C = 4 and S = 3. (Gruber first said the new slope was −⅓; a student corrected it to −¾.) If you lower the cookie price to $4/3 instead, you get C = 9 and S = 3.

Plot the cookie price against the cookies you choose: (2, 6), (3, 4), (4/3, 9). That is the demand curve. Graphically, each price gives a new budget line, pivoting around the pizza intercept. A higher cookie price shrinks the opportunity set, and you end up with fewer cookies.

The general version is the formula from the Lecture 3 note. With this utility function you spend half your income on each good, so C = Y/(2Pc) = 12/Pc. That's the whole demand curve in one line.

A student noticed that pizza stayed at 3 slices whatever the cookie price. That's a quirk of this utility function, not a law: S = Y/(2Ps) doesn't depend on the cookie price. Gruber calls the line through the chosen bundles a flat price-consumption curve. In general, changing one price changes the demand for both goods.

His homework runs the other way: change the pizza price, and cookies stay put while pizza moves. At $6 a slice, S = 24/12 = 2 and C stays at 6. The next note explains why the line is flat: two effects cancel.

ε = (ΔQ/Q) ÷ (ΔP/P), or with derivatives, ε = (dQ/dP) × (P/Q)

Gruber loosely calls it the derivative of quantity with respect to price. But the slope dQ/dP alone changes with the units, such as cookies per dollar or per cent. Multiplying by P/Q turns it into percent per percent, which doesn't depend on units. ε is zero or negative, because people buy less when the price rises. The one theoretical exception is in the next note.

Two extremes don't exist, but they fix the idea:

**• Perfectly inelastic (ε = 0):** a vertical demand curve, where quantity doesn't respond to price at all. Students suggested gas and water. Gruber pointed to the substitutes (a bus, a bike, other drinks), so neither is perfectly inelastic. Insulin is the classic near-case: a diabetic won't skip it over an extra $1. Even insulin is only inelastic within a normal price range, since at $1 million some people couldn't buy it.

**• Perfectly elastic (ε = −∞):** a horizontal demand curve, where any tiny price rise wipes out demand. The near-cases are things you don't really need, or goods with close substitutes. If McDonald's charged twice what Burger King does for a burger, almost everyone would switch. 

The lesson is that elasticity comes down to substitutability. The more substitutes a good has, the more elastic its demand. Every real good sits somewhere between the extremes.

Gruber also warns that the course cheats with straight lines. A demand curve with the same elasticity everywhere has to be curved, and he leaves the reason as homework. On a straight line the slope is fixed, but P/Q changes as you move along it. For Q = 10 − P, ε = −P/Q:

**•** At P = 8, ε = −4.

**•** At P = 5, ε = −1.

**•** At P = 2, ε = −0.25.

The cookie demand curve C = 12/Pc is the opposite case. Its elasticity is (−12/Pc²) × (Pc/C) = −1 at every price, and the curve bends. You can check this without calculus. Spending on cookies is $12 at every price ($2 × 6, $3 × 4, $4/3 × 9). Spending that stays the same when the price changes is exactly what an elasticity of −1 means. So when the course gives one elasticity for a straight line, read it as true near one point.

Changing income instead of price traces a different curve. Raise income from $24 to $32 with prices fixed. The tangency stays at S/C = ½, since prices and tastes haven't changed. Only the budget moves out in parallel, to 32 = 4S + 2C, so C = 8 and S = 4. Cut income to $16, and C = 4 and S = 2.

The relationship between income and quantity is the **Engel curve**; here it's C = Y/4 for cookies. Its version of elasticity is the **income elasticity of demand**:

γ = (ΔQ/Q) ÷ (ΔY/Y), or γ = (dQ/dY) × (Y/Q)

Unlike ε, γ can take any sign, and its value sorts goods into types:

- **Normal goods (γ > 0):** you buy more as income rises.
    - **Luxuries (γ > 1):** quantity rises faster than income, so the good takes a growing share of your budget. Examples are restaurant meals and nice watches.
    - **Necessities (0 < γ < 1):** you buy more, but the share of your budget falls. Examples are groceries for eating at home, clothes and rent. A poor household might spend 60% of its income on housing and a rich one far less, even though the rich one has the nicer flat.
- **Inferior goods (γ < 0):** you buy less as income rises, because you only bought it for being cheap. Ramen is Gruber's example.

Luxury and necessity are defined by income, not price. The curve is named after the statistician Ernst Engel. His 1857 study of household budgets found that the share spent on food falls as income rises, which makes food the original necessity.

For this note's cookies, γ = (¼) × (Y/C) = 1 exactly. Both goods always take half the budget, which puts them right on the line between luxury and necessity.

**Supporting Content**


---
## References
[[Payoffs define the game]]
[[Weak Dominance]]

## Questions

