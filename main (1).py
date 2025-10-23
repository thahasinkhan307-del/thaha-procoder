class scart:
  def __init__(self):
    self.items=[]
  def add(self,name,qty):
   item=(name,qty)
   self.items.append(item)
  def remove(self,name):
    for item in self.items:
      if item[0]==name:
        self.items.remove(item)
        break
  def total(self):
    total=0
    for item in self.items:
      total+=item[1]
    return total
#main unicode

cart=scart()

cart.add("chocolate",1000)
cart.add("burger",4000)
cart.add("vennelaa stick",300)
print("Current items in cart: ")

for item in cart.items:
  print(item[0],"-",item[1])
  
total_qty = cart.total()
print("total quantity: ",total_qty)