import sqlite3

# initialize SQLite 
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

def checkLogin(username, pw):
	query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + pw + "'"
	print(query)
	cursor.execute(query)
	result = cursor.fetchall()
	if len(result) == 0:
		return False
	return True

def checkUser(username):
	query = "SELECT * FROM users WHERE username = '" + username + "'"
	print(query)
	cursor.execute(query)
	result = cursor.fetchall()
	if len(result) == 0:
		return False
	return True

def insertUser(username, pw):
	cursor.execute("INSERT INTO users VALUES (:username, :password)", {'username': username, 'password': pw})
	print(username + " is now registered!")

def recentTransactions(user):
	query  = "SELECT * FROM transactions WHERE username = \"" + user + "\" ORDER BY setDate DESC LIMIT 5"
	cursor.execute(query)
	return cursor.fetchall()

def balance(user):
	query = "SELECT amount FROM transactions WHERE username = \"" + user + "\""
	cursor.execute(query)
	
	balance = 0
	for x in cursor.fetchall():
		balance += x[0]
	return balance

def printDB():
	cursor.execute("SELECT * FROM users")
	print(cursor.fetchall())
	cursor.execute("SELECT * FROM transactions")
	print(cursor.fetchall())

def initializeDB():
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

	accounts = (

		)

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

	printDB()

