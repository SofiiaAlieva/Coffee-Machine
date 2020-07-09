class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
    def add_money(self, deposit_dollars, deposit_cents):
        self.deposit_dollars = deposit_dollars
        self.deposit_cents = deposit_cents
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        self.total_cents = self.cents + self.deposit_cents
        self.dollars = self.total_cents // 100
        self.cents = self.total_cents % 100
