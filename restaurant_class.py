class Restaurant:
    """A simple attempt to create a class for restaurant and cuisine."""

     def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes."""
        self.restaurant_name = name
        self.cuisine_type = cuisine

❹     def describe_restaurant(self):
       """Describe the restuarant."""
        print(f"{self.name} is the name of the restuarant.")
        print(f"The {self.cuisine} is the food in this restuarant")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} hours are 12pm till 10pm!")


my_food = Restaurant('McDs','Chinese')