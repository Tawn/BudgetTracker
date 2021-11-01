import Backend

def start(username):
    print("\nDashboard: log in successful")
    
    # Print 5 most recent transactions and balance
    recentTransactions(username)

    userInput = 0
    while (userInput != 3):

		# User Options
        userInput = input("\nPlease enter a # for a transaction action:\n" 
        + "1. See all\n"
        + "2. Create\n"
        + "3. Exit\n"
        + "Input: ")
        userInput = int(userInput)

        # Create new entry
        if userInput == 1:
           viewTransactions(username)
            
        #  Create new user 
        elif userInput == 2:
            createTransaction(username)
            
        # Check outside cases
        elif userInput < 1 or userInput > 3 : 
            print("Invalid input. Please try again.")

    print("\nNow exiting...")

# Gets up to 5 recent transactions
def recentTransactions(username):
    transactions = Backend.recentTransactions(username)
    print(transactions)
    if(len(transactions) > 0):
        # Get and print (5) recent transactions
        print("\nYour recent transactions:\n")
        for entry in transactions:
            print(str(entry[0]) + "\t" + entry[1] + "\namount: $" +str(entry[2]))
        
        # Get and print balance
        balance = Backend.balance(username)
        print("\nBalance from all transactions: $" + str(balance))
    else:
        print("There are no recent transactions")

# Adds a new transaction
def createTransaction(user):
    amount = input("Please enter an amount of today's expense/income\nAmount: ")
    desc = input("What is this for?\nDescription: ")
    Backend.addTransaction(user, amount, desc)

#  Get's all of user's transactions
def viewTransactions(user):
    transactions = Backend.getTransactions(user)
    if(len(transactions) > 0):
        # Get and print all transactions
        print("\nYour transactions:\n")
        for entry in transactions:
            print(str(entry[0]) + "\t" + entry[1] + "\namount: $" +str(entry[2]))

        # Get and print balance
        balance = Backend.balance(user)
        print("\nBalance from all transactions: $" + str(balance))
    else:
        print("There are no recent transactions")