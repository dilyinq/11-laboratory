class Restaurant:
    def __init__(self, name, cuisine_type):
       self.name = name
       self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Ресторан {self.name} предлагает блюда кухни {self.cuisine_type}.")

restaurant1 = Restaurant("PIZZA PAZZA", "италии")
restaurant2 = Restaurant("Jack & Chan", "китая")
restaurant3 = Restaurant("Старый Токио", "японии")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()