import Backend
import Dashboard

def start():
	
	userInput = 0

	while (userInput != 3):
		# User Options
		userInput = input("\nEnter the #s for the following options:\n1. Log in\n2. Create new user\n3. Exit\nInput: ")
		userInput = int(userInput)
		print(userInput)

		# Check if log in is true 
		# True: Log in to dashboard 
		if userInput == 1:
			login()
			
		#  Create new user 
		elif userInput == 2:
			createUser()
			
		# Check outside cases
		elif userInput < 1 or userInput > 3 : 
			print("Invalid input. Please try again.")

	print("\nNow exiting...")

def login():
	print("\nLoginPage.login() called")
	username = input("Enter a username: ")
	pw = input("Enter a password: ")
	loginSuccess = Backend.checkLogin(username, pw)
	
	
	if loginSuccess: # Log in to dashboard
		Dashboard.login(username)
	else: # Go back to User Options  
		print("\n\nInvalid username or password.")

	

def createUser():
	print("LoginPage.createUser() called")
	username = input("\nEnter a username: ")
	pw = input("Enter a password: ")
	# 1. Check to see if user exists
	userExists = Backend.checkUser(username)

	if not userExists: # Insert new user to DB
		Backend.insertUser(username, pw)
	else: # Go back to User Options
		print("\n\n User already exists.")





