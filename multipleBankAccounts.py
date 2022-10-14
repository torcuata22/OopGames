#multiple bank account simulations using lists

accountNamesList = []
accountBalancesList=[]
accountPasswordsList=[]

def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
#To create new account: append appropriate value to each list:
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)
    
def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList
    print('Account: ', accountNumber)
    print(' Name: ', accountNamesList[accountNumber])
    print(' Balance: ', accountBalancesList[accountNumber])
    print(' Password: ', accountPasswordsList[accountNumber])
    
