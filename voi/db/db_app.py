import database

# Create the database
database.create_db()

# add a single record to database
database.add_one("anushya","balakrishnan","anushya816@gmail.com","1111111")

# delete a single record from the database
#database.delete_one('2')

# list of tuples to hold the records to be stored in the database
stuff = [
	('yanu','sahi','yanu816@gmail.com','22222222'),
	('kavin','kumar','kavin816@gmail.com','33333333'),
	('sushu','kutty','susshu816@gmail.com','44444444'),
	('balakrishnan','halliah','amutha@gmail.com','55555555'),
	('amutha','balakrishnan','balakrishnan@gmail.com','66666666')
	]

# method to add multiple entries to the database
database.add_many(stuff)

# email lookup method
#database.email_lookup('anushya816@gmail.com')

# a generic column lookup and valid the user generated data with the one in the database
#database.column_lookup('personal_id','1111111', "anushya", "balakrishnan")
#database.column_lookup('personal_id','1111111', "anushya", "balakrishna")
#database.column_lookup('first_name','yanu')
#database.column_lookup('last_name','halliah')

# show the records in the datbase
database.show_all()
