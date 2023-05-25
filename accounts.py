class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.deposits.append({"amount": amount, "narration": "deposit"})

    def withdrawal(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            self.withdrawals.append({"amount": amount, "narration": "withdrawal"})

    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
           return(f"{transaction['narration']} - {transaction['amount']}")

    def borrow_loan(self, amount):
        if self.loan_balance > 0:
            return "You have an outstanding loan"
        elif amount < 100:
            return "Loan amount be at least 100"
        elif len(self.deposits) < 10:
            return "You must have made at least 10 deposits to be eligible for a loan"
        elif amount > sum(transaction['amount'] for transaction in self.deposits) / 3:
            return "Loan amount cannot exceed 1/3 of your total deposits"
        else:
            self.loan_balance += amount
            self.balance += amount
            self.deposits.append({"amount": amount, "narration": "loan"})
            return "Loan  granted"
        
        


