# class User:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age

#     def display_info(self):
#         return f"My name is {self.name} and I am {self.age} years old."

#     def role_details(self):
#         self.role = "Devops Engineer"
#         return f"hi My self {self.name} and My role is {self.role}."

#     def place_details(self):
#         place = "Hyderabad"
#         return f"Myself {self.name} and I am from {place}."    

#     # def test(self):
#         # return f"I got this {place} role from previous function"    
    

# admin = User("Shravan", 30)

# print(admin.display_info())
# print(admin.role_details())
# print(admin.place_details())
# # print(admin.test())

# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def get_summary(self):
#         return f"Title: {self.title} \nAuthor: {self.author} \nYear: {self.year}"
    
# book1 = Book("Love The Effort", "Ghrims Jhonny", 1987)

# print(book1.get_summary())


class Bank_account:
    def __init__(self,account_holder,Balance):
        self.account_holder = account_holder
        self.Balance = Balance

    def deposit(self, amount):
        if amount > 0:
            self.Balance += amount
            return f"Deposited amount: {amount} \nnew balance : {self.Balance} \nThank you for depositing amount"
        else:
            return "Deposit amount must be positive"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.Balance:
            self.Balance -= amount
            return f" withdrawn amount: {amount} \nRemaning Balance: {self.Balance} \nThank you for withdrawing amount"
        elif amount > self.Balance:
            return "It seems you do not have insufficient funds"
        elif amount > 40000:
            return "You have excedded your limit"
        else:
            return "Withdraw amount should be positive"

    def Account_details(self):
        return f"Account_holder_name : {self.account_holder} \nAccount_Balance : {self.Balance} \nThank You for fetching account Details"


user1 = Bank_account("shravan",34789)              


print(user1.deposit(2000))
print('''
    
      ''')
print(user1.withdraw(20000))
print('''
    
      ''')
print(user1.Account_details())
