class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Имя ресторана: {self.restaurant_name}")
        print(f"Вид кухни: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт")

newrestaurant = Restaurant("Душа востока", "грузинская") # новый экземпляр класса

print(newrestaurant.restaurant_name)
print(newrestaurant.cuisine_type)
newrestaurant.describe_restaurant()
newrestaurant.open_restaurant()