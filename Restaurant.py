class Restaurant():
    RestaurantAdress={"SRB":"Welcome to Saravana Bhavan, chennai","KH":"Welcome to Kerala Hotel, chennai","KV":"Welcome to Krishna Vilas, chennai"}
    identifier=False
    def RestaurantName(self,Restaurantkey):
        for eachrestaurant in self.RestaurantAdress.keys():
            if eachrestaurant==Restaurantkey:
                print(self.RestaurantAdress.get(Restaurantkey))#to get the value from the corresponding keys
                self.identifier=True
                break
        if self.identifier==False:
            print("The given restaurant is not available")


