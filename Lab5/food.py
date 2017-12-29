"""
A module that represents the valid food types.

Author: Sean Strout @ RITCS
"""
import sys

# The set of valid food items
FOODS = {'beef', 'pork', 'chicken', 'onion', 'pepper', 'tomato'}

# The set vegetables
VEGGIES = {'onion', "pepper", 'tomato'}

# The calories for each food item (a dictionary, where 
# key = food name (string) and value = calories (int)
CALORIES = {
    'beef': 200,
    'chicken': 140,
    'pork': 100,
    'onion': 30,
    'pepper': 25,
    'tomato': 10,
}

# Implement Food class here
class Food:
    __slots__ = ("name","is_veg","calorie")

    def __init__(self,name):
        self.name = name
        self.is_veg = self.is_veggie()
        self.calorie = self.calories()

    #to calculate if the item is veg or not
    def is_veggie(self):
        for item in VEGGIES:
            if self.name == item:
                return True
        return False

    #calculates the number of calories in item
    def calories(self):
        for data_item in CALORIES:
                if self.name in CALORIES:
                    return CALORIES[self.name]
                else:
                    print("item doesnt exist")
                    sys.exit(0)

#adding mushroom
def newFood(name):

    VEGGIES.add(name)
    CALORIES.update({name:7})
    FOODS.add(name)
    f = Food(name)

newFood("mushroom")

