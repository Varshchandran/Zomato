from Zomato.Restaurant import Restaurant
class Menu(Restaurant):
    Restaurantmenu = {"Veg Biriyani":150,"Veg Thali":130,"Veg Fried Rice":100,"Dosa": 60, "Pongal": 40,"idli":30}
    identifier = False
    selectedmenu="Null"

    def Menuavailability(self, Menukey):
        for eachmenu in self.Restaurantmenu.keys():
            if eachmenu == Menukey:
                print("The price of the item is :"+str(self.Restaurantmenu.get(Menukey)))  # to get the value from the corresponding keys
                self.identifier = True
                self.selectedmenu=Menukey
                break
        if self.identifier == False:
            print("The given menu is not available")

    def amount(self, Quantity):
        Price= self.Restaurantmenu.get(self.selectedmenu)
        Totalamount= Price*Quantity
        print("Your selected quanity is:" + str(Quantity))
        print("The total amount is :"+str(Totalamount))

"""obj = Menu()
obj.RestaurantName("KH")
obj.Menuavailability("Dosa")
obj.amount(20)"""
