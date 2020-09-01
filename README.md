# Martingale
A simple martingale system for betting/trading purposes.

Martingale trading can be tricky and dangerous when not performed correctly,
it needs a extreme sense of money management to make it work right.

This algorythm is made to simplify it.

The flow is the following:

You take a bet, if the bet is winning, you keep the betsize, if you loses,
you increase the betsize using a factor. Usually bigger than 1.25x the size of the last losing bet.
if you lose again, then you raise the bet again, and you keep raising till you get a winning bet.

That's why it's dangerous. You can easily run out of cash if you don't use correct money management.

The class:
```python
class Martingale:

    def __init__(self, balance, factor, risk, goal):
        self.starting_balance = balance
        self.balance = balance
        self.factor = factor
        self.risk_p = risk / 100
        self.goal = goal + balance

        self.bet = self.balance * self.risk_p

        # STATS
        self.stats = {"games": 0,
                      "lowest_balance": self.balance,
                      "current_drawdown": 0,
                      "max_drawdown": 0}

        self.wins = []
        self.losses = []

    def lose(self, betsize):
        self.stats["games"] += 1
        self.bet = self.bet * self.factor
        self.balance -= betsize
        self.losses.append(betsize)
        print(f"[L][{self.stats['games'] - 1}] -{betsize:.2f} -> {self.balance:.2f}")

    def win(self, betsize):
        self.stats["games"] += 1
        self.bet = self.balance * self.risk_p
        self.balance += betsize
        self.wins.append(betsize)
        print(f"[W][{self.stats['games'] - 1}] +{betsize:.2f} -> {self.balance:.2f}")

    def refresh_stats(self):
        if self.balance < self.stats['lowest_balance']:
            self.stats['lowest_balance'] = round(self.balance, 2)
        self.stats['current_drawdown'] = round((self.balance - self.starting_balance) / 100, 2)
        if self.stats['current_drawdown'] < self.stats['max_drawdown']:
            self.stats['max_drawdown'] = round(self.stats['current_drawdown'], 2)

    def see_stats(self):
        print("\n-- STATISTICS ----------------------")
        print(f" Victories: {len(self.wins)}")
        print(f" Losses: {len(self.losses)}")
        for key in self.stats:
            print(f" {key.title()}: {self.stats[key]}")
        print(f" Avg. Profit: ${sum(self.wins) / len(self.wins):.2f}")
        print(f" Avg. Loss: ${sum(self.losses) / len(self.losses):.2f}")

        print("\n-- BALANCE ------------------------")
        print(f" Your goal was: ${self.goal:.2f}")
        print(f" Your Balance is: ${self.balance:.2f}")
        print("\n-- PROFIT ---------------------------")
        print(f"$                           {self.balance - self.starting_balance:.2f}")
        print("-------------------------------------")

    def play(self):
        result = random.randint(0, 1)
        if result == 0:
            self.lose(self.bet)

        elif result == 1:
            self.win(self.bet)

        self.refresh_stats()

```

The whole program is "modularized" so you can use it to build strategies for betting and/or trading.

Please take note that this system is not supposed to be used irresponsably and it's not a promise of profits.

@ngeorg at 31/08/2020, made during the pandemic!

