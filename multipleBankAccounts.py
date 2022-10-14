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
    print()
    
def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Wrong password. Try again')
        return None
    return accountBalancesList[accountNumber]

def deposit( accountNumber,amountToDeposit, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToDeposit < 0:
        print('Error: You cannot deposit a negative amount')
        return None
    if password != accountPasswordsList[accountNumber]:
        print('Wrong password')
        return None
    accountBalancesList[accountNumber] =  accountBalancesList[accountNumber] + amountToDeposit
    return accountBalancesList[accountNumber]

def withdraw( accountNumber,amountToWithdraw, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToWithdraw < 0:
        print('Error: You cannot withdraw a negative amount')
        return None
    if password != accountPasswordsList[accountNumber]:
        print('Wrong password')
        return None
    if amountToWithdraw > accountBalancesList[accountNumber]:
        print('Insufficient funds')
    accountBalancesList[accountNumber] =  accountBalancesList[accountNumber] - amountToWithdraw
    return accountBalancesList[accountNumber]

          
    
