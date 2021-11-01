import Backend
import Dashboard

def start():
	
	userInput = 0

	while (userInput != 3):
		# User Options
		userInput = input("\nEnter the #s for the following options:\n"
		+ "1. Log in\n"
		+ "2. Create new user\n"
		+ "3. Exit\n"
		+ "Input: ")
		userInput = int(userInput)

		# Log in to dashboard
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
	username = input("Enter a username: ")
	pw = input("Enter a password: ")
	loginSuccess = Backend.checkLogin(username, pw)
	
	
	if loginSuccess: # Log in to dashboard
		Dashboard.start(username)
	else: # Go back to User Options  
		print("\n\nInvalid username or password.")

def createUser():
	username = input("\nEnter a username: ")
	pw = input("Enter a password: ")
	# 1. Check to see if user exists
	userExists = Backend.checkUser(username)

	if not userExists: # Insert new user to DB
		Backend.insertUser(username, pw)
	else: # Go back to User Options
		print("\n\n User already exists.")






