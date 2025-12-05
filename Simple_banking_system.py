def Check_Balance():
    global balance
    print("Cheking Balance")

def Withdraw():
    amount = float(input("Enter your amount to Withdraw: "))
    global balance
    balance = balance - amount
    print("=================================")
    print("Withdrawal is Done")
    print("=================================")

def Deposit():
    print("Depositing Your amount")

balance = 0
print("Welcome ABC Bank")

while True:
    print("1 Check Balance")
    print("2 Withdraw an Amount")
    print("3 Deposit an Amount")
    print("4 Quit")

    choice = (input("Enter Your choice (1-4): "))

    if choice == 1:
        Check_Balance()
    elif choice == 2:
        Withdraw()
    elif choice == 3:
        Deposit()
    elif choice == 4:
        break
    else:
        print("invalid choice!!\n Re Try")

print("Thanks for the banking with us")