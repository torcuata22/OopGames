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

#create dummy accounts, use len(accountNamesList) as account number:
print("Joe's account number is: ", len(accountNamesList))
newAccount("Joe", 100, "soup")

print("Mary's account number is: ", len(accountNamesList))
newAccount("Mary", 12345, "nuts")

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()
    
    action = input('What do you want to do? ') # this is a string
    action = action.lower()  # forces answer to be lowercase
    action = action[0]  # use only the first letter of the string
    print()

    if action == "b":
        print('Retrieve account balance for: ')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter your password')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance != None:
            print('Your available balance is: ')
        
    elif action == "d":
        print("Deposit")
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter your password')
        userDepositAmount = input("How much would you like to deposit?")
        userDepositAmount = int(userDepositAmount)
        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance != None:
            print('Your new balance is:', newBalance)
        
  
    elif action == "n":
        print('New account')
        userName = input('Please enter your desired user name')
        userStartingDeposit = input("Please enter your initial deposit for your new account")
        userStartingDeposit = int(userStartingDeposit)
        userPassword = input('Please create your password')
        userAccountNumber = len(accountNamesList)
        newAccount(userName, userStartingDeposit, userPassword)
        print('Your new account number is:', userAccountNumber)
        
   
    elif action == "w":
        print("Deposit")
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter your password')
        userWithdrawAmount = input("How much would you like to deposit?")
        userWithdrawAmount = int(userWithdrawAmount)
        newBalance = deposit(userAccountNumber, userWithdrawAmount, userPassword)
        if newBalance != None:
            print('Your new balance is:', newBalance)      
    
    elif action == "s":
        print("Show: ")
        nAccounts = len(accountNamesList)
        for accountNumber in range(0, nAccounts):
            show(accountNumber)
            
    if action == "q":
       print('Goodbye!')
       break
print('Done')
    
