import sqlite3
from datetime import datetime

# initialize SQLite 
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

class Backend:

	def initializeDB(self):
		# User table
		cursor.execute("""CREATE TABLE IF NOT EXISTS users(
			username TEXT PRIMARY KEY, 
			password TEXT)""")

		# Transaction table
		cursor.execute("""CREATE TABLE IF NOT EXISTS transactions(
			setDate DATETIME,
			description TEXT, 
			amount INT,
			username TEXT, FOREIGN KEY(username) REFERENCES users(username))""")

		# Insert data into users
		cursor.execute("INSERT INTO users VALUES (:username, :password)", {'username': "Thanh", 'password': "t123"})
		cursor.execute("INSERT INTO users VALUES (:username, :password)", {'username': "Ryan", 'password': "r123"})
		cursor.execute("INSERT INTO users VALUES (:username, :password)", {'username': "Alice", 'password': "a123"})

		# Insert data into transactions
		cursor.execute("INSERT INTO transactions VALUES (:setDate, :description, :amount, :username)", {'setDate': "2021-10-25 12:00:00", 'description': "Side job", 'amount': 200, 'username': "Thanh"})
		cursor.execute("INSERT INTO transactions VALUES (:setDate, :description, :amount, :username)", {'setDate': "2021-10-24 12:00:00", 'description': "Side job", 'amount': 150, 'username': "Thanh"})
		cursor.execute("INSERT INTO transactions VALUES (:setDate, :description, :amount, :username)", {'setDate': "2021-10-23 12:00:00", 'description': "Dining reimbusement", 'amount': 30, 'username': "Thanh"})
		cursor.execute("INSERT INTO transactions VALUES (:setDate, :description, :amount, :username)", {'setDate': "2021-10-22 12:00:00", 'description': "Dining", 'amount': -30, 'username': "Thanh"})
		cursor.execute("INSERT INTO transactions VALUES (:setDate, :description, :amount, :username)", {'setDate': "2021-10-21 12:00:00", 'description': "Rent", 'amount': -500, 'username': "Thanh"})
		cursor.execute("INSERT INTO transactions VALUES (:setDate, :description, :amount, :username)", {'setDate': "2021-10-20 12:00:00", 'description': "Paycheck", 'amount': 600, 'username': "Thanh"})

		self.printDB()
		
	def checkLogin(self, username, pw):
		print("Test\n\n")

		query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + pw + "'"
		print(query)
		cursor.execute(query)
		result = cursor.fetchall()
		if len(result) == 0:
			return False
		return True

	def checkUser(self, username):
		query = "SELECT * FROM users WHERE username = '" + username + "'"
		print(query)
		cursor.execute(query)
		result = cursor.fetchall()
		if len(result) == 0:
			return False
		return True

	# Adds new user to the user table
	def insertUser(self, username, pw):
		cursor.execute("INSERT INTO users VALUES (:username, :password)", {'username': username, 'password': pw})
		print(username + " is now registered!")

	# Get's up to 5 recent transactions
	def recentTransactions(self):
		query  = "SELECT * FROM transactions WHERE username = \"" + self.username + "\" ORDER BY setDate DESC LIMIT 5"
		cursor.execute(query)
		return cursor.fetchall()

	# Get's balance of all user's transactions
	def getBalance(self):
		query = "SELECT amount FROM transactions WHERE username = \"" + self.username + "\""
		cursor.execute(query)
		
		self.balance = 0
		for x in cursor.fetchall():
			self.balance += x[0]
		return self.balance

	# Adds new transaction to the transaction table
	def addTransaction(self, amt, desc):
		curDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		cursor.execute("INSERT INTO transactions VALUES (:setDate, :description, :amount, :username)", {'setDate': curDate, 'description': desc, 'amount': amt, 'username': self.username})

	# Get's user's transactions
	def getTransactions(self):
		query  = "SELECT * FROM transactions WHERE username = \"" + self.username + "\" ORDER BY setDate"
		cursor.execute(query)
		return cursor.fetchall()

	# Prints the both tables in the DB with their data
	def printDB(self):
		cursor.execute("SELECT * FROM users")
		print(cursor.fetchall())
		cursor.execute("SELECT * FROM transactions")
		print(cursor.fetchall())


