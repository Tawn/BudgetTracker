import Backend 
import LoginPage


def main():
    #Initialize DB
    Backend.initializeDB()

    # Log in
    LoginPage.start()


if __name__ == '__main__':
    main()
