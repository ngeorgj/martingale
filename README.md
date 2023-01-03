# Martingale Simulator

A python implementation of the Martingale betting strategy.

## Usage

To use the Martingale class, instantiate it with the following parameters:

- balance: Initial balance of the account
- factor: Multiplier to use for increasing the bet size after a loss
- risk: Percentage of the balance to use as the initial bet size
- goal: Target balance to try to reach
- print_stats: Whether to print stats after each game

Optionally, you can also specify whether to print stats after each game with the `print_stats` parameter.

## Install Dependencies
```python
pip install matplotlib
```  

## Create a Martingale object

```python
m = Martingale(balance=1000, factor=2, risk=10, goal=5000)
```

## Run 10000 simulations

```python
# play the game 1000 times
m.play_multiple_times(1000)
m.see_stats()

# plot equity curve (matplotlib required)
plt.plot(m.balances)
plt.show()
```

# General Information about the Martingale Trading Strategy

The Martingale trading strategy is a popular method in forex and binary options trading, but is not without its risks. It is based on the idea that by doubling the size of a trade after a loss, you will eventually recoup your losses and make a profit.

## How it works

1. Choose a trading instrument and set the initial trade size.
2. If the trade is successful, repeat step 1 with the same trade size.
3. If the trade is unsuccessful, double the trade size and repeat step 1.
4. Repeat this process until a trade is successful, at which point you will have recouped your losses and made a profit equal to the initial trade size.

## Pros

- Simple to implement
- Can be profitable in a series of trades with a high win rate

## Cons

- Can lead to rapid account depletion if a long losing streak occurs
- Does not account for the inherent risk and return of the underlying asset
- Ignores the impact of transaction costs and slippage

## Risk Management

It is important to use risk management techniques when using the Martingale strategy, such as setting stop losses and limiting the maximum trade size. It is also crucial to have a sound understanding of the underlying market and to trade within one's means.

## Conclusion

The Martingale strategy can be a useful tool in certain trading situations, but it is not a guarantee of success and carries a high level of risk. As with any trading strategy, it is important to thoroughly understand the risks and to use proper risk management techniques.
