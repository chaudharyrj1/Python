from AccountSchedular import AccountSchedular
from Customer import Customer
from Account import Account
from UserError import duplicateAccNo
from UserError import notEnoughBalance
from UserError import invalidAccountNumber

from Test.BankingApp.UserError import notEnoughBalance


class Client:
    accountSchedular=AccountSchedular()
    def showOptions(self):
        flag=0
        while flag==0:
            choice=input("\n1.Create Account\n2.Deposit Amount\n3.Withdraw Amount\n4.Transfer Amount\n5.Show Account Details\n6.Exit")
            try:
                if(choice=="1"):
                    self.addAccount()
                elif(choice=="2"):
                    self.depositAmount()
                elif(choice=="3"):
                    self.withdrawAmount()
                elif(choice=="4"):
                    self.transferAmount()
                elif(choice=="5"):
                    self.showAccounts()
                elif(choice=="6"):
                    flag=1;
                else:
                    print("Please Choose valid option")
            except duplicateAccNo:
                print("Account Number already exists!!!!")
            except notEnoughBalance:
                print("Not enough balance")
            except invalidAccountNumber:
                print("Account does not exist!!!!")



    def addAccount(self):
        print("Enter Account Details:")
        accountNumber=input("Enter Account Number:")
        acc=self.accountSchedular.getAccountByAccountNumber(accountNumber)
        if(acc is None):
            name=input("Enter Customer Name:")
            address=input("Enter Customer Address:")
            phone=input("Enter Phone Number:")
            balance=int(input("Enter Current Balance:"))
            customer=Customer()
            customer.setName(name)
            customer.setAddress(address)
            customer.setPhone(phone)
            self.accountSchedular.customers.append(customer)
            account=Account()
            account.setAccountNumber(accountNumber)
            account.setBalance(balance)
            account.setCustomer(customer)
            self.accountSchedular.addAccount(account)
        else:
            raise duplicateAccNo


    def depositAmount(self):
        accountNumber=input("Enter Account Number:")
        amount=int(input("Enter amount to be deposited"))
        status=self.accountSchedular.depositAmount(accountNumber,amount)
        if(status=="NotExist"):
            raise invalidAccountNumber
        if(status=="failed"):
            raise notEnoughBalance
        if(status=="success"):
            print("Done Successfully!!!!")

    def withdrawAmount(self):
        accountNumber = input("Enter Account Number:")
        amount = int(input("Enter amount to be withdrawed:"))
        status=self.accountSchedular.withdrawAmount(accountNumber,amount)
        if (status == "NotExist"):
            raise invalidAccountNumber
        if (status == "failed"):
            raise notEnoughBalance
        if (status == "success"):
            print("Done Successfully!!!!")

    def transferAmount(self):
        fromAccountNumber = input("Enter Your Account Number:")
        toAccountNumber = input("Enter Account Number in which you want to transfer amount:")
        amount = int(input("Enter amount to be transferred:"))
        status=self.accountSchedular.transferAmount(fromAccountNumber,toAccountNumber,amount)
        if (status == "NotExist"):
            raise invalidAccountNumber
        if (status == "failed"):
            raise notEnoughBalance
        if (status == "success"):
            print("Done Successfully!!!!")

    def showAccounts(self):
        accounts=self.accountSchedular.accounts
        if(accounts==[]):
            print("No Account Available!!!!")
        else:
            for account in accounts:
                print("Account Number: ",account.getAccountNumber()," Name:",account.getCustomer().getName()," Address:",account.getCustomer().getAddress()," Phone:",account.getCustomer().getPhone()," Balance:",account.getBalance())
client=Client()
client.showOptions()