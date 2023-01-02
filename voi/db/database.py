import sqlite3

# create a database

def create_db():
	# connect to a db
	conn = sqlite3.connect('customer.db')
	# create a cursor
	c = conn.cursor()

	c.execute(""" CREATE TABLE customers (
			first_name text,
			last_name text,
			email text,
			personal_id integer
			)""") #, ('anushya', 'b', 'anushya.b@gmail.com', 1111111))
	# commit our command
	conn.commit()
	#close our connection
	conn.close()

# query the database and return all records
def show_all():
	# connect to a db
	conn = sqlite3.connect('customer.db')
	# create a cursor
	c = conn.cursor()

	# query the database
	c.execute("SELECT rowid, * FROM customers")
	items = c.fetchall()

	for item in items:
		print(item)	

	# commit our command
	conn.commit()
	#close our connection
	conn.close()

# add a new record to the table
def add_one(first, last, email, personal_id):
	# connect to a db
	conn = sqlite3.connect('customer.db')
	# create a cursor
	c = conn.cursor()

	c.execute("INSERT INTO customers VALUES (?,?,?,?)", (first, last, email, personal_id))
	# commit our command
	conn.commit()
	#close our connection
	conn.close()

# add many new records to the table
def add_many(list):
	# connect to a db
	conn = sqlite3.connect('customer.db')
	# create a cursor
	c = conn.cursor()

	c.executemany("INSERT INTO customers VALUES (?,?,?,?)", (list))
	# commit our command
	conn.commit()
	#close our connection
	conn.close()

# delete a record from the table
def delete_one(id):
	# connect to a db
	conn = sqlite3.connect('customer.db')
	# create a cursor
	c = conn.cursor()

	c.execute("DELETE FROM customers WHERE rowid = (?)", id)
	# commit our command
	conn.commit()
	#close our connection
	conn.close()

# lookup with where 
def email_lookup(email):
	# connect to a db
	conn = sqlite3.connect('customer.db')
	# create a cursor
	c = conn.cursor()

	c.execute("SELECT * FROM customers WHERE email = (?)", (email,))
	items = c.fetchall()

	for item in items:
		print(item)

	# commit our command
	conn.commit()
	#close our connection
	conn.close()

# lookup with where 
def column_lookup(column_name, column_value, given_first_name, given_last_name):
	# connect to a db
	conn = sqlite3.connect('customer.db')
	# create a cursor
	c = conn.cursor()

	c.execute("SELECT * FROM customers WHERE "+column_name+" = (?)", (column_value,))
	items = c.fetchall()

	for item in items:
		print(item)
		print(item[0])

		if(given_last_name==item[1] and given_first_name==item[0]):
			print("Validation successful!!!")
		else:
			print("Validation not successful :-()")


	# commit our command
	conn.commit()
	#close our connection
	conn.close()