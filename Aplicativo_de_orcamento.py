class Category:

    def __init__(self, product):
        self.product = product
        self.ledger = []
        self.money = 0

    def check_funds(self, value):
        if self.money > value:
            return True
        else:
            return False

    def deposit(self, deposit, description=''):
        self.money += deposit
        self.ledger.append({'amount': deposit, 'description': description})

    def withdraw(self, withdrawn, description=''):
        if self.check_funds(withdrawn):
            self.money -= withdrawn
            self.ledger.append({'amount': withdrawn, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        return self.money

    def transfer(self, transferred, local):
        if self.check_funds(transferred):
            self.money -= transferred
            self.ledger.append({'amount': transferred, 'description': f'Transfer to {local.product}'})
            local.money += transferred
            local.ledger.append({'amount': transferred, 'description': f'Transfer from {self.product}'})
            return True
        else:
            return False
