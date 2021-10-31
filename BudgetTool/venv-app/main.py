import LoginPage as LP
from tkinter import *

root = TK()

myLabel = Label(root, text="Hello World!")

def main():
    # Create an instance of a Login Page and start program
    login = LP.LoginPage()
    login.start()

if __name__ == '__main__':
    main()
