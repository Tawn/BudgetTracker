import Backend



def start(username):
    print("\nDashboard: log in successful")

    # Print 5 most recent transactions and balance
    recentTransactions(username)

    userInput = 0
    while (userInput != 3):
		# User Options
        userInput = input("\nTransaction Actions:\n" 
        + "1. See more\n"
        + "2. Create\n"
        + "3. Exit\n"
        + "Input: ")
        userInput = int(userInput)

        # Check if log in is true 
        # True: Log in to dashboard 
        if userInput == 1:
            print("user inputs 1")
            
        #  Create new user 
        elif userInput == 2:
            print("user inputs 2")
            
        # Check outside cases
        elif userInput < 1 or userInput > 3 : 
            print("Invalid input. Please try again.")

    print("\nNow exiting...")

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

# Todo Allow user to see all transaction based on the month
# Todo Allow user to add an transaction
# Todo Allow user to delete transaction