#multiple bank account simulations using lists

accountNamesList = []
accountBalancesList=[]
accountPasswordsLists=[]

def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsLists
#To create new account: append appropriate value to each list:
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsLists.append(password)
    
def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsLists
    
