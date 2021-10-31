import Backend 
import LoginPage
from datetime import datetime


def main():
    
    #Initialize DB
    Backend.initializeDB()

    # Log in
    LoginPage.start()


if __name__ == '__main__':
    main()
