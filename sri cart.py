class MCart:
    def __init__(self):
        self.items = []
        
    def add_item(self,item_name,qty):
        item =  (item_name,qty)
        self.items.append(item)

    def remove_item(self,item_name):

        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total


#driver code
cart=MCart()    
cart.add_item("honey",100)
cart.add_item("c-nuts",100)
cart.add_item("toys",500)
print("Current Items in cart:")
for item in cart.items:
    print(item[0],"-",item[1])

total_qty = cart.calculate_total()
print("Total Quantity:",total_qty)

cart.remove_item("honey")
print("\nUpdated Items in Cart after removing honey:")
for item in cart.items:
    print(item[0],"-",item[1])
total_qty = cart.calculate_total()
print("Total Quantity:",total_qty)
