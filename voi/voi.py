import datetime
import db_app

class Customer:

	def __init__(self):
		#initialize the variables
		self.scooter = 0
		self.rentalPlan = 0	
		self.rentalTime = 0

	def register_function(self):
 	 	#  this will register the user to the system
		first = str(input("Enter your first name: ").lower())
		last = str(input("Enter your last name: ").lower())
		return first, last
		
	def submit_verification(self):
 	 	# customer submits verification proof like id card 
		proof = (input("Enter the license number or passport number: "))
		return proof

	def request_scooter_plan(self):
 	 	#  1hr or daily or weekly
		scooter = input("How many bikes do you want")
		
		try:
			scooter = int(scooter)	
		except ValueError:

			print("It is not a positive number")
			return -1
		if scooter < 1:
			print("enter the number greater than zero")
			return -1
		else:
			self.scooter = scooter
		return self.scooter


	def return_scooter(self):
 	 	# finally customer returns the scooter
		if self.scooter and self.rentalPlan and self.rentalTime:
			return self.scooter, self.rentalPlan , self.rentalTime
		else:
			return 0,0,0


	

class Voi_Rental:
	def __init__(self,stock=0):
		self.stock = stock


	def approve_registration(self,details):
 	 	# approve the customer registration function
		# tuple is stored as details to make as a single parameter.
		first,last = details
		full_name = first,last
		#print("details is :")
		#print(details)
		#print("full_name is :")
		#print(full_name)

		for tup in db_app.stuff:
			#print("tup[0:2] is:")
			#print(tup[0:2])
			#print("full_name is ")
			#print(full_name)
			if full_name == tup[0:2]:
				print(first,last)
				print("your records matched with us")
				return True
			else:
				print("Your name doesnt match our records, sorry")
				pass
			#return False
		#return True
		
		#print("Your name doesnt match our records, sorry")
		#return False

	def display_stock(self):
		print("we have {} stock of scooter currently".format(self.stock))
		return self.stock

		
	def approve_verification(self,proof):
 	 	# approve the verification of the customer document
		if len(proof) == 8:
			print("Your {} is verified".format(proof))
			return True 
			
		else:
			print("Enter the proof correctly")
			return False


	def rent_scooter_on_hourly_basis(self,n):
		# approve the bike and plan request
		if n < 0:
			print("enter the positive number")
			return None
		elif n > self.stock:
			print("sorry we dont have enough stocks of scooter")
		else:
			now = datetime.datetime.now()
			print("you have chosen an hourly plan for {} scooter at {}".format(n,now))
			print("It will be charged £5 per hour for each scooter")
		self.stock = self.stock-n
		return now

	def rent_scooter_on_daily_basis(self,n):
		if n < 0:
			print("enter the positive number")
			return None
		elif n > self.stock:
			print("sorry we dont have enough stocks of scooter")
		else:
			now = datetime.datetime.now()
			print("you have chosen an hourly plan for {} scooter at {}".format(n,now))
			print("It will be charged £20 for each day per scooter ")
		self.stock = self.stock-n
		return now

	def rent_scooter_on_weekly_basis(self,n):
		if n < 0:
			print("enter the positive number")
			return None
		elif n > self.stock:
			print("sorry we dont have enough stocks of scooter")
		else:
			now = datetime.datetime.now()
			print("you have chosen an hourly plan for {} scooter at {}".format(n,now))
			print("It will be charged £50 per hour")
		self.stock = self.stock-n
		return now


	def generate_bill(self,usage):
 	 	# generate the bill for the customer based on usage
		numOfScooter,rentalPlan,rentalTime = usage
		bill = 0
		if numOfScooter and rentalPlan and rentalTime:
			self.stock = self.stock + numOfScooter
			timeNow = datetime.datetime.now()
			print ("Time you started : ", rentalTime)
			print ("Time now is : ", timeNow)
			print ("Time diff is : ",  timeNow-rentalTime)

			totalTime = timeNow - rentalTime
			
			if rentalPlan == 1:
				bill =(totalTime.seconds/3600)*5*numOfScooter
				print(bill)
			elif rentalPlan == 2:
				bill = round(totalTime.days) * 20 * numOfScooter
			
			elif rentalPlan == 3:
				bill = round(totalTime.days/7) *50 * numOfScooter

			if (3<= numOfScooter <= 5) :
				print("Your having a discount of 30%")
				bill = bill * 0.7
			print("Total amount is {}£ for your ride".format(bill))
			return bill
		else:
			print("are you sure you rented a scooter with us?")
			return None

		




				 

		


