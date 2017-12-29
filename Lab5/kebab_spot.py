"""
A module that represents "spots" on the skewer.

Author: Sean Strout @ RITCS
"""

class KebabSpot:
    """
    Class: KebabSpot
    Description: This class is used to represent an individual
        spot on the skewer.  Each spot contains a food item,
        and a reference to the next spot.  
    """
    __slots__ = "item", "next"

    def __init__(self, item, next):
        """
        Construct a KebabSpot instance.
        :param item: the item (Food) to store at this spot
        :param next: the next KebabSpot on the skewer
        """
        self.item = item
        self.next = next

    def size(self):
        """
        Return the number of elements from this KebabSpot instance to the end
        of the skewer.
        :return: the number of elements (int)
        """
        count = 0
        while self != None:
            count += 1
            self = self.next
        return count

    def is_vegan(self):
        """
        Return whether there are all vegetables from this spot to the end of
        the skewer.
        :return True if there are no vegetables from this spot down, 
        False otherwise.
        """

        while self != None:
                if self.item.is_veg != True:
                    return False
                else:
                    self = self.next
        return True


    def has(self, name):
        """
        Return whether there are any vegetable from this spot to the end of
        the skewer.
        :param name: the name (string) being searched for.
        :return True if any of the spots hold a Food item that equals the
        name, False otherwise.
        """
        found = False

        while self != None:
            if self.item.name == name:
                found = True
                return found
            else:
                self = self.next
        return found

    def string_em(self):
        """
        Return a string that contains the list of items in the skewer from
        this spot down, with a comma after each entry.
        :return A string containing the names of each of the Food items from
        this spot down.
        """
        names = ""
        while self != None :
            names = names + self.item.name + ","
            self = self.next
        return names

    def get_item(self):
        return self.item

    #use to calculate calories
    def calories(self):
        """
        calculates number of calories in skewer from this spot to down
        :return: integer value calories
        """
        calories = 0
        while self != None:
            calories += self.item.calorie
            self = self.next
        return calories