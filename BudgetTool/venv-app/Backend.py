import sqlite3

# initialize SQLite 
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

def initializeDB():
	# Create table
	cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY, password TEXT)")

	# Insert data
	cursor.execute("INSERT INTO users VALUES (:username, :password)", {'username': "Thanh", 'password': "t123"})
	cursor.execute("INSERT INTO users VALUES (:username, :password)", {'username': "Ryan", 'password': "r123"})
	cursor.execute("INSERT INTO users VALUES (:username, :password)", {'username': "Alice", 'password': "a123"})

	# Output
	cursor.execute("SELECT * FROM users")
	print(cursor.fetchall())

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