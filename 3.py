class Restaurant:
    def __init__(self, name, kitchen, rating):
        self.name = name
        self.kitchen = kitchen
        self.rating = rating

    def update_rating(self, new_rating): # обновление рейтинга
        self.rating = new_rating

restaurant = Restaurant("Душа востока", "восточная", 4.5)
print(restaurant.rating)

restaurant.update_rating(4.9)
print(restaurant.rating)