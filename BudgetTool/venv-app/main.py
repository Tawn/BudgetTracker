from BudgetApp import BudgetApp
from Backend import Backend 

def main():    
    #Initialize DB
    backend = Backend()
    backend.initializeDB()
    app = BudgetApp()
    app.start()

if __name__ == '__main__':
    main()
