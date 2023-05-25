class Account:
    def __init__(self, balance):
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
        self.current_balance = balance

    def check_balance(self):
        return self.current_balance

    def deposit(self, amount):
        self.current_balance += amount
        self.deposits.append({
            "amount": amount,
            "cash": "deposit"
        }) 

    def withdrawal(self, amount):
        if amount > self.current_balance:
            print("Insufficient balance.")
            return
        self.current_balance -= amount
        self.withdrawals.append({
            "amount": amount,
            "cash": "withdrawal"
        })

    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(transaction["cash"], "-", transaction["amount"])

    def borrow_loan(self, amount):
        if self.loan_balance > 0:
            print("You already have a loan.")
            return
        if amount < 100:
            print("Minimum amount to borrow is 100.")
            return
        if len(self.deposits) < 10:
            print("You need at least 10 deposits to borrow.")
            return
        total_deposits = sum(transaction["amount"] for transaction in self.deposits)
        if amount > total_deposits / 3:
            print("Amount requested is too high.")
            return
        self.loan_balance += amount
        self.current_balance += amount

    def repay_loan(self, amount):
        if amount >= self.loan_balance:
            self.current_balance += self.loan_balance
            self.loan_balance = 0
            overpayment = amount - self.loan_balance
            if overpayment > 0:
                self.current_balance += overpayment
        else:
            self.loan_balance -= amount

    def transfer(self, amount, recipient_account):
        if amount <= self.current_balance:
            self.current_balance -= amount
            recipient_account.current_balance += amount
        else:
            return("no balance to transfer the requested amount.")
            
