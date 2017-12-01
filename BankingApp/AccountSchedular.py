from Account import Account
from Customer import Customer
class AccountSchedular:
    accounts=[]
    customers=[]

    def addAccount(self,account):
        self.accounts.append(account)

    def depositAmount(self,accountNumber,amount):
        account=self.getAccountByAccountNumber(accountNumber);
        if(account is None):
            return "NotExist"
        else:
            account.setBalance(account.getBalance()+amount)
            return "success"

    def getAccountByAccountNumber(self,accountNumber):
        flag=0
        for account in self.accounts:
            if(account.getAccountNumber()==accountNumber):
                flag+=1
                return account
        if(flag==0):
            return None

    def withdrawAmount(self, accountNumber, amount):
        account = self.getAccountByAccountNumber(accountNumber);
        if (account is None):
            return "NotExist"
        else:
            if(account.getBalance()<amount):
                return "failed"
            else:
                account.setBalance(account.getBalance() - amount)
                return "success"

    def transferAmount(self,fromAccountNumber,toAccountNumber,amount):
        fromAccount=self.getAccountByAccountNumber(fromAccountNumber)
        toAccount=self.getAccountByAccountNumber(toAccountNumber)
        if((fromAccount is None)|(toAccount is None)):
            return "NotExist"
        else:
            if(fromAccount.getBalance()<amount):
                return "failed"
            else:
                fromAccount.setBalance(fromAccount.getBalance()-amount)
                toAccount.setBalance(toAccount.getBalance() + amount)
                return "success"
