# Simple Blackjack Simulation

## Overview

This project implements a **simple Blackjack simulator** to analyze the expected payoff of different player strategies.

The player is allowed to choose only **Hit** or **Stand**. Other Blackjack actions such as **double, split, surrender, or blackjack bonuses are not allowed**.

The program simulates many rounds of Blackjack and calculates the **expected payoff** based on the game results.

Payoff rules:

| Result | Payoff |
| ------ | ------ |
| Win    | +1     |
| Draw   | 0      |
| Lose   | -1     |

The goal is to determine a **strategy table** and compute the **expected value (EV)** of playing the game.

---

# Game Rules

### Card Values

Cards are assigned the following values:

| Card        | Value      |
| ----------- | ---------- |
| A           | 1 or 11    |
| 2–9         | Face value |
| 10, J, Q, K | 10         |

For simulation purposes the deck can be represented as:

```
1,2,3,4,5,6,7,8,9,10,10,10,10
```

---

### Player Actions

The player may only perform two actions:

* **Hit** → draw another card
* **Stand** → stop drawing cards

If the player's total exceeds **21**, the player **busts** and loses immediately.

---

### Dealer Rules

The dealer follows a fixed rule:

* Dealer must **draw until total ≥ 17**
* If the dealer has **Soft 17 (Ace counted as 11)**, the dealer must **draw again**

Examples:

| Dealer Hand     | Action |
| --------------- | ------ |
| 16              | Hit    |
| 17              | Stand  |
| A + 6 (Soft 17) | Hit    |
| 18              | Stand  |

---

### Determining the Winner

After both player and dealer finish:

| Condition       | Result |
| --------------- | ------ |
| Player busts    | Lose   |
| Dealer busts    | Win    |
| Player > Dealer | Win    |
| Player < Dealer | Lose   |
| Player = Dealer | Draw   |

---

# Strategy Table

The player follows a predefined strategy depending on the hand total.

Example strategy:

| Player Total | Action |
| ------------ | ------ |
| 4–16         | Hit    |
| 17–21        | Stand  |

This strategy can later be modified to evaluate different strategies.

---

# Simulation Process

The program performs the following steps:

1. Start a new game
2. Deal two cards to the player
3. Deal two cards to the dealer
4. Player plays according to the strategy table
5. If the player busts → game ends
6. Dealer plays according to dealer rules
7. Compare player and dealer totals
8. Record result (Win / Lose / Draw)
9. Repeat for many games


# Expected Payoff Calculation

Expected value (EV) is computed as:

EV = P(win) × 1 + P(draw) × 0 + P(loss) × (−1)

Which simplifies to:

EV = P(win) − P(loss)

```
EV = (Wins - Losses) / Games
```

