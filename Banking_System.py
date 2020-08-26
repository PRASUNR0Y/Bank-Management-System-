import pickle
import os
import pathlib

class Accounts:
    accountNo = 0
    name = ''
    deposit = 0
    type = ''

    def createAccounts(self):
        self.accountNo= int(input("Enter thr account no : "))
        self.name= input("Enter the account holder name : ")
        self.type= input("Enter the type of account [C/S] : ")
        self.deposit= int(input("Enter The Initial amount(>= 500 for Saving and >=1000 for current : "))
        print("\n\n\nAccount Created")

    def showAccounts(self):
        print("Account Number : ",self.accountNo)
        print("Account Holder Name : ",self.name)
        print("Type of Account :",self.type)
        print("Balance : ",self.deposit)

    def modifyAccounts(self):
        print("Account Number : ",self.accountNo)
        self.name = input("Modify Account Holder Name : ")
        self.deposit = int(input("Modify Balance : "))

    def depositAmounts(self,amount):
        self.deposit += amount

    def withdrawAmounts(self,amount):
        self.deposit -= amount

    def report(self):
        print(self.accountNo, " ",self.name, " ",self.type, " ",self.deposit)

    def getAccountsNo(self):
        return self.accountNo

    def getAccountsHolderName(self):
        return self.name

    def getAccountsType(self):
        return self.type

    def getDeposit(self):
        return self.deposit

def intro():
    print("\t\t\t\t*******************************************")
    print("\t\t\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t*******************************************")
    print("\t\t\t\tBrought To You By - Prasun Roy")
    print("\t\t\t\tPress enter for main menu")
    input()

def writeAccounts():
    account = Accounts()
    account.createAccounts()
    writeAccountsFile(account)

def displayAll():
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open('accounts.data','rb')
            mylists =pickle.load(infile)
            for items in mylists :
                print(items.accountNo," ",items.name," ",items.type," ",items.deposit )
            infile.close()

        else:
            print("No records to display")

def displayssp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for items in mylist:
            if items.accountNo == num:
                print("Your Account Balance is = ",items.deposit)
                found = True
    else:
        print("No records to search")
    if not found:
        print("No existing record with this number")

def depositAndWithdraw(num1,num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data","rb")
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for items in mylist:
            if items.accountNo == num1 :
                if num2 == 1:
                    amount = int(input("Enter the amount of deposit : "))
                    items.deposit += amount
                    print("Your account is updated")

                elif num2 == 2:
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= items.deposit:
                        items.deposit -= amount
                    else :
                        print("You cannot withdraw larger amount")

    else:
        print("No records to Search")

    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist,outfile)
    outfile.close()
    os.rename('newaccounts.data','accounts.data')

def deleteAccounts(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for items in oldlist:
            if items.accountNo != num:
                newlist.append(items)
        os.remove('accounts.data')
        outfile =open('newaccounts.data','wb')
        pickle.dump(newlist,outfile)
        outfile.close()
        os.rename('newaccounts.data','accounts.data')

def modifyAccounts(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for items in oldlist :
            if items.accountNo == num:
                items.name = input("Enter the account holder name : ")
                items.type = input("Enter the account type : ")
                items.deposit = int(input("Enter the amount : "))
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist,outfile)
        outfile.close()
        os.rename('newaccounts.data','accounts.data')

def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')

    else:
        oldlist =[account]
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist,outfile)
        outfile.close()
        os.rename('newaccounts.data','accounts.data')





#front-end of the program

ch=''
num=0
#intro()



print("\t\t\t\t*******************************************")
print("\t\t\t\t\t\tBANK MANAGEMENT SYSTEM")
print("\t\t\t\t*******************************************")
print("\t\t\t\tBrought To You By - Prasun Roy")
print("\n\n\n\n")



print("\tMAIN MANU")
print("\t1. NEW ACCOUNT")
print("\t2. DEPOSIT AMOUNT")
print("\t3. WITHDRAW AMOUNT")
print("\t4. BALANCE ENQUIRY")
print("\t5. ALL ACCOUNT HOLDER LIST")
print("\t6. CLOSE AN ACCOUNT")
print("\t7. MODIFY AN ACCOUNT")
print("\t8. EXIT")
print("\tSelect Your Option [1-8]")



while ch !=8:
    ch = input("Enter your choice :")
    if ch == '1':
        writeAccounts()
    elif ch == '2':
        num = int(input("\tEnter The Account No. : "))
        depositAndWithdraw(num,1)
    elif ch == '3':
        num = int(input("\tEnter The Account No. : "))
        depositAndWithdraw(num,2)
    elif ch == '4':
        num = int(input("\tEnter The Account No. : "))
        displayssp(num)
    elif ch == '6':
        num = int(input("\tEnter The Account No. : "))
        deleteAccounts(num)
    elif ch == '5':
        displayAll()
    elif ch == '7':
        num = int(input("\tEnter The Account No. : "))
        modifyAccounts(num)
    elif ch == '8':
        print("\tThanks for using Bank Management System")
        break
    else:
        print("Invalid Choice")