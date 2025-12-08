kyc_documents = {}
balance = 0

def Check_Balance():
    global balance
    print("====================================")
    print()
    print(f"Your Balance is {balance}")
    print()
    print("====================================")

def Deposit():
    global balance
    amount1 = int(input("Enter an amount to Deposit: "))
    if amount1 > 0:
        balance += amount1
    else:
        print("cannot deposited a negative amount ")
    
    print("====================================")
    print()
    print("Deposit Done")
    print()
    print("====================================")

def Withdraw():
    global balance
    amount2 = int(input("Enter an amount to withdraw: "))
    if amount2 < 0:
        print("cannot withdraw a negative or zero amount")
    elif amount2 > balance:
        print("You have insufficient balance, amount cannot be withdrawn")
    else:
        balance -= amount2
    print("====================================")
    print()
    print("Withdrawal Done")
    print()
    print("====================================")


def Update_KYC(docs):
    global kyc_documents
    kyc_documents.update(docs)

def Check_KYC():
    if len(kyc_documents) == 0:
        print("====================================")
        print()
        print("KYC not done")
        print("")
        print("====================================")
    else:
        for doc in kyc_documents:
            print(f"{doc}:{kyc_documents[doc]}")

        print("====================================")

if __name__ == "__main__":
    print("====================================")
    print("Welcome SWATI Bank")
    print("====================================")

    while True:
        print("1 Check Balance")
        print("2 Depositdraw an Amount")
        print("3 Wthdraw an Amount")
        print("4 Check KYC")
        print("5 Update KYC")
        print("6 Quit")

        choice = input("Enter Your choice (1-6): ")

        if choice == '1':
            Check_Balance()
        elif choice == '2':
            Deposit()
        elif choice == '3':
            Withdraw()
        elif choice == '4':
            Check_KYC()
        elif choice == '5':
            kyc_docs = {}
            n_documents = int(input("Enter the number of documents you want to add: "))
            for i in range(n_documents):
                key = input("enter the document name you want to add: ")
                value = input("enter the document number: ")
                kyc_docs[key] = value
            Update_KYC(kyc_docs)
            print("====================================")
            print()
            print("KYC updated sucsessfully")
            print("")
            print("====================================")

        
        elif choice == '6':
            break
        else:
            print("invalid choice!!\n Re Try")
    print("====================================")
    print()
    print("Thank You\n Have a nice day")
    print()
    print("====================================")