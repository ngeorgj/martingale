import random
import time


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


m = Martingale(10000, 1.61, 1, 300)  # Balance, Increasing Factor, Risk, Monetary Goal

while True:
    m.play()
    if m.balance <= 0:
        print("You are out of cash!")
        m.see_stats()
        break

    elif m.balance > m.goal:
        print("Goal Achieved.")
        m.see_stats()
        break
