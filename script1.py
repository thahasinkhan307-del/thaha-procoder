#bike renta;system
class bike shop:
  def __init__(self,stock)
   self.stock = stock
  def showbike(self)
    print("Total bikes: ",self.stocks)
  def rentbike(self,qty):
    if qty<=0:
      print("Pplease enter the positive value :")
    elif qty>self.stock:
      print("Enter the value less than stocks")
    else:
      self.stock=self.stock-qty
      print("Total price : ",qty*100)
      print("Total bikes : ",self.stock)
while True:
  obj = bikeshop(100)
  user_input = int(input("1->display stock  2->rent bikes  3->exit"))