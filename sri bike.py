Rental System
#Bike
class BikeShop:

    def __init__(self,stock):
        self.stock = stock

    def ShowBike(self):
         print("Total Bike :",self.stock)

         
    def rentBike(self,quantitfy):

        if quantity<=0:
            print("please enter the positive value or greater than zero")
        elif quantity>self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock = self.stock-quantity
            print("Total price :",quantity * 100)
            print("Total Bikes",self.stock)
                 
                 
while True:
    obj=BikeShop(100)
    user_input = int(input('''1->Display Stock
2-> Rent a Bike
3->exit'''))
    if user_input ==1:
        obj.ShowBike()
    elif user_input ==2:
        n = int(input("Enter The rent Bike :->"))
        obj.rentBike(n)
    else:
        break
                           

