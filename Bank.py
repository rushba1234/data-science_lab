class Bank:
    def __init__(self):
        self.acc_no=0
        self.bal=0
        print(self.bal)

    def addbank(self):
        self.acc_no=int(input("Enter account number:"))
    def deposit(self):
        amt=int(input("Enter amount:"))
        self.bal=self.bal+amt
    def withdraw(self):
        amt=int(input("Enter amount:"))
        self.bal=self.bal-amt
        print("amount withdrawn")
    def transfer(self):
        print("Transferred")

    def balance(self):
        print("Total Balance:", self.bal)


b = Bank()
ch = 1

while (ch != 0):

    print("1. Add Bank Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Show Balance")
    print("0. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        b.addbank()

    if ch == 2:
        b.deposit()

    if ch == 3:
        b.withdraw()

    if ch == 4:
        b.transfer()

    if ch == 5:
        b.balance()
