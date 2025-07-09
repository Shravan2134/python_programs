from datetime import datetime

class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1004231

    def create_account(self, account_holder , initial_balance = 0):
        account_number = self.next_account_number
        self.accounts[account_number] = Account(account_number, account_holder, initial_balance)
        self.next_account_number += 1
        return account_number


    def get_account_details(self, account_number):
        return self.accounts.get(account_number)
    
    def transfers(self, from_acc, to_acc , amount):
        src = self.get_account_details(from_acc)
        dst = self.get_account_details(to_acc)

        if not src or not dst:
            return "One or Both accounts are invalid"
        
        withdrawal_status = src.withdraw(amount)
        if "Insufficient" in withdrawal_status:
            return "Transfer Failed: Insufficient funds"
        
        Deposit_status = dst.deposit(amount)
        src.transactions.append(f"Transferred ₹{amount} to {to_acc}")
        dst.transactions.append(f"Received ₹{amount} from {from_acc}")
        return f"Transfer of amount {amount} from account {from_acc} to account {to_acc} has been succesful"
    
    def closing_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            return "Your account has been closed"      

class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance        = balance
        self.transactions   = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            entry = f"deposited amount rs{amount}"
            self.transactions.append(entry)
            return f"Deposited amount: {amount} \nnew balance : {self.balance} \nThank you for depositing amount"
        else:
            return "Deposit amount must be positive"
        
    def get_details(self):
        return (f"Account No: {self.account_number}\n"
                f"Holder: {self.account_holder}\n"
                f"Balance: ₹{self.balance}")    
    
        
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > 0:
            self.balance -= amount
            entry = f"withdrawn amount rs{amount}"
            self.transactions.append(entry)
            return f"The amount has been successfully withdrawn"
        else:
            return "withdraw amount should be positive"

    def get_transaction_history(self):
        if not self.transactions:
            return "No transactions performed yet"
        else:
            return self.transactions      



if __name__ == "__main__":

    bank = Bank()

  
    acc1 = bank.create_account("Shravan", 2000)
    acc2 = bank.create_account("Alice")

    print(bank.get_account_details(acc1).deposit(200))
    print(bank.get_account_details(acc2).withdraw(100))
    print(bank.transfers(acc1, acc2, 300))

    for acc_num in (acc1, acc2):
        acct = bank.get_account_details(acc_num)
        print("\n---")
        print(acct.get_details())
        for entry in acct.get_transaction_history():
            print(entry)



