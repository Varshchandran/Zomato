from Zomato.Menu import Menu
class Price(Menu):
     def totalamount(self):
          print("Here is your menu!!!!!!!")
          for eachmenu in self.Restaurantmenu.keys():
           print(eachmenu)
          
obj1= Price()
obj1.RestaurantName("KH")
obj1.Menuavailability("Dosa")
obj1.totalamount()
obj1.Menuavailability("Dosa")
obj1.amount(20)