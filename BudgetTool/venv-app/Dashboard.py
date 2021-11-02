from Backend import Backend

backend = Backend()

class Dashboard:

    def start(self):
        print("\nDashboard: log in successful")
        backend.username = self.username

        # Print 5 most recent transactions and balance
        self.recentTransactions()

        exit = False
        while not exit:
            input = self.nextAction()
            if input == "1": self.viewTransactions()
            elif input == '2': self.createTransaction()
            elif input == '3': exit = True
            else: print("Invalid input. Please try again")
        print("Logging out.")


    def nextAction(self):
        return input("\nEnter the #s for the following options:\n"
        + "1. See all\n"
        + "2. Create new transaction\n"
        + "3. Log out\n"
        + "Input: ")

    # Gets up to 5 recent transactions
    def recentTransactions(self):
        transactions = backend.recentTransactions()
        print(transactions)
        if(len(transactions) > 0):
            # Get and print (5) recent transactions
            print("\nYour recent transactions:\n")
            for entry in transactions:
                print(str(entry[0]) + "\t" + entry[1] + "\namount: $" +str(entry[2]))
            
            # Get and print balance
            backend.getBalance()
            print("\nBalance from all transactions: $" + str(backend.balance))
        else:
            print("There are no recent transactions")

    # Adds a new transaction
    def createTransaction(self):
        amount = input("Please enter an amount of today's expense/income\nAmount: ")
        desc = input("What is this for?\nDescription: ")
        backend.addTransaction(amount, desc)

    #  Get's all of user's transactions
    def viewTransactions(self):
        transactions = backend.getTransactions()
        if(len(transactions) > 0):
            # Get and print all transactions
            print("\nYour transactions:\n")
            for entry in transactions:
                print(str(entry[0]) + "\t" + entry[1] + "\namount: $" +str(entry[2]))

            # Get and print balance
            backend.getBalance()
            print("\nBalance from all transactions: $" + str(backend.balance))
        else:
            print("There are no recent transactions")


