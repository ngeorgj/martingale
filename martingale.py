import random
import matplotlib.pyplot as plt


class Martingale:

    def __init__(self, balance, factor, risk, goal, print_stats=True):
        """
        Initializes a Martingale object with the following parameters:
        - balance: Initial balance of the account
        - factor: Multiplier to use for increasing the bet size after a loss
        - risk: Percentage of the balance to use as the initial bet size
        - goal: Target balance to try to reach
        - print_stats: Whether to print stats after each game
        """
        self.starting_balance = balance
        self.balance = balance
        self.factor = factor
        self.risk_p = risk / 100
        self.goal = goal + balance

        self.bet = self.balance * self.risk_p

        # Print stats after each game
        self.print_stats = print_stats

        # STATS
        self.stats = {"games": 0,
                      "lowest_balance": self.balance,
                      "current_drawdown": 0,
                      "max_drawdown": 0}

        # Initialize lists for storing wins and losses
        self.wins = []
        self.losses = []
        
        # Initialize the balances list
        self.balances = []
        
        # Initialize max_loss_streak and max_win_streak
        self.max_loss_streak = 0
        self.max_win_streak = 0
        
        # Initialize lists for storing loss and win streaks
        self.loss_streaks = [0]
        self.win_streaks = [0]
        
        # Initialize last_play to None
        self.last_play = None

    def lose(self, betsize):
        self.stats["games"] += 1
        self.bet = self.bet * self.factor
        self.balance -= betsize
        self.losses.append(betsize)
        
        # Update max_loss_streak and loss_streaks
        self.max_loss_streak = max(self.loss_streaks)
        if self.last_play == "loss":
            self.loss_streaks[-1] += 1
        else:
            self.loss_streaks.append(1)
        self.last_play = "loss"
        
        if(self.print_stats):
            print(f"[L][{self.stats['games'] - 1}] -{betsize:.2f} -> {self.balance:.2f}")

    def win(self, betsize):
        self.stats["games"] += 1
        self.bet = self.balance * self.risk_p
        self.balance += betsize
        self.wins.append(betsize)
        
        # Update max_win_streak and win_streaks
        self.max_win_streak = max(self.win_streaks)
        if self.last_play == "win":
            self.win_streaks[-1] += 1
        else:
            self.win_streaks.append(1)
        self.last_play = "win"
        
        if(self.print_stats):
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
        if len(self.wins) == 0:
            avg_profit = 0
        else:
            avg_profit = sum(self.wins) / len(self.wins)
        print(f" Avg. Profit: ${avg_profit:.2f}")
        if len(self.losses) == 0:
            avg_loss = 0
        else:
            avg_loss = sum(self.losses) / len(self.losses)
        print(f" Avg. Loss: ${avg_loss:.2f}")

        print("\n-- Streaks ------------------------")
        print(f" Max Win Streak: {self.max_win_streak}")
        print(f" Max Loss Streak: {self.max_loss_streak}")
        
        print("\n-- BALANCE ------------------------")
        print(f" Your goal was: ${self.goal:.2f}")
        print(f" Your Balance is: ${self.balance:.2f}")
        print("\n-- PROFIT ---------------------------")
        print(f"$                           {self.balance - self.starting_balance:.2f}")

    def play(self):
        result = random.randint(0, 1)
        if result == 0:
            self.lose(self.bet)

        elif result == 1:
            self.win(self.bet)

        self.refresh_stats()
        
        # check if liquidated
        if(self.balance <= 0):
            print("You are liquidated!")
            return 2
        
        return result
            
    def play_multiple_times(self, num_games):
        for i in range(num_games):
            result = self.play()
            if(result == 2):
                break
            else:
                self.balances.append(self.balance)

# create a Martingale instance
m = Martingale(balance=1000, factor=1.1, risk=0.1, goal=1000, print_stats=False)

# play the game 1000 times
m.play_multiple_times(10000)
m.see_stats()

# plot equity curve
plt.plot(m.balances)
plt.show()