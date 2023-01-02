from voi import Customer,Voi_Rental

def main():
    customer = Customer()
    dealer = Voi_Rental(50)
    
        
    while True:
        initial_registration = dealer.approve_verification(customer.submit_verification())
        user_details = dealer.approve_registration(customer.register_function())
        
        if(user_details):
            print("""
            ====== Bike Rental Shop =======
            1. Display available bikes
            2. Request a scooter on hourly basis $5
            3. Request a scooter on daily basis $20
            4. Request a scooter on weekly basis $60
            5. Return a scooter
            6. Exit
            """)
            choice = input("Enter choice: ")

            try:
                choice = int(choice)
            except ValueError:
                print("That's not an int!")
                continue
            
            if choice == 1:
                dealer.display_stock()

            elif choice == 2:
                customer.rentalTime = dealer.rent_scooter_on_hourly_basis(customer.request_scooter_plan())
                customer.rentalPlan = 1

            elif choice == 3:
                customer.rentalTime = dealer.rent_scooter_on_daily_basis(customer.request_scooter_plan())
                customer.rentalPlan = 2

            elif choice == 4:
                customer.rentalTime = dealer.rent_scooter_on_weekly_basis(customer.request_scooter_plan())
                customer.rentalPlan = 3

            elif choice == 5:
                customer.bill = dealer.generate_bill(customer.return_scooter())
                customer.rentalPlan, customer.rentalTime, customer.numOfScooter = 0,0,0        
            elif choice == 6:
                break
            else:
                print("Invalid input. Please enter number between 1-6 ")        
        print("Please try again.")


if __name__ == "__main__":
	main()