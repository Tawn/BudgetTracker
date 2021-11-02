from Backend import Backend

backend = Backend()

class LoginPage: 

	def login(self):
		loginSuccess = backend.checkLogin(self.username, self.pw)
		if loginSuccess: 
			return True
		print("\n\nInvalid username or password.")
		return False

	def createUser(self):
		userExists = backend.checkUser(self.username)
		if not userExists: 
			backend.insertUser(self.username, self.pw)
		else: 
			print("\nUser already exists.")






