#bike renta;system
class BikeShop:
    def __init__(self, stock):
        self.stock = stock

    def showbike(self):
        print("Total bikes available:", self.stock)

    def rentbike(self, qty):
        if qty <= 0:
            print("Please enter a positive value.")
        elif qty > self.stock:
            print("Not enough bikes in stock. Please enter a smaller quantity.")
        else:
            self.stock -= qty
            print(f"Total price: ₹{qty * 100}")
            print("Bikes remaining:", self.stock)


# Create the shop object once
obj = BikeShop(100)

while True:
    try:
        user_input = int(input("\nChoose an option:\n1 -> Display stock\n2 -> Rent bikes\n3 -> Exit\nYour choice: "))
    except ValueError:
        print("Invalid input. Please enter a number (1-3).")
        continue

    if user_input == 1:
        obj.showbike()
    elif user_input == 2:
        try:
            n = int(input("Enter number of bikes to rent: "))
            obj.rentbike(n)
        except ValueError:
            print("Please enter a valid number.")
    elif user_input == 3:
        print("Thank you for using the Bike Rental System!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
