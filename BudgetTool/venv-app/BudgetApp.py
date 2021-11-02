from LoginPage import LoginPage
from Dashboard import Dashboard
from Backend import Backend

lp = LoginPage()
dashboard = Dashboard()
backend = Backend()

class BudgetApp:

    lp = LoginPage()
    backend.initializeDB()
    
    def start(self):


        print("Welcome to your Budget App!")
        exit = False
        while not exit:
            input = self.nextAction()
            if input == "1": self.login()
            elif input == '2': self.createUser()
            elif input == '3': exit = True
            else: print("Invalid input. Please try again")
        print("Now exiting App.")

    def nextAction(self): 
        return input("\nEnter the #s for the following options:\n"
        + "1. Log in\n"
        + "2. Create new user\n"
        + "3. Exit\n"
        + "Input: ")

    def login(self):
        lp.username = input("Enter a username: ")
        lp.pw = input("Enter a password: ")
        
        loginSuccess = lp.login()
        if loginSuccess:
            dashboard.username = lp.username
            dashboard.start()

        print("\nLog out successful!")

    def createUser(self):
        lp.username = input("\nEnter a username: ")
        lp.pw = input("Enter a password: ")
        lp.createUser()


        


    