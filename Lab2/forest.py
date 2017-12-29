__author__ = 'sk'

"""
CSCI 603 = Assignment 02
File: turtleScene.py
Language: python3
Author:  Sagar Kukreja sk3126@rit.edu
The program draws a night scene and a day scene from wood available from night scene
"""
import sys
import turtle
import random

# screen size
XWIDTH = 900
YHEIGHT = 700
# this is the space between tree trunks or buildings
SEPERATION = 100


def move_to_next():
    """ call this at end of draw function to move turtle to start of next tree
    :pre:  heading(east), up
    :post:  heading(east), up
    :return: none
    """
    turtle.setheading(0)
    turtle.down()
    turtle.forward(SEPERATION)


def draw_house(side):
    """ draws house with given wall height, side
    :param: side
    :pre:  heading(east), up
    :post:  heading(east), up
    :return: float
    """
    turtle.down()
    turtle.setheading(90)
    turtle.forward(side)
    turtle.setheading(45)
    turtle.forward(side / 2 * (pow(2, .5)))
    turtle.right(90)
    turtle.forward(side / 2 * (pow(2, .5)))
    turtle.setheading(270)
    turtle.forward(side)
    turtle.setheading(180)
    turtle.forward(side)
    turtle.up()
    turtle.setheading(0)
    turtle.forward(100)  # move turtle back to where move_to_next expects it
    return ((2**.5) * side) + side + side


def draw_triangle(height):
    """ draws right triangle at top of tree trunk for pine tree
    :param : height
    :pre:  heading(east), up
    :post:  heading(east), up
    :return: length
    """
    length = SEPERATION - 15
    turtle.up()
    turtle.setheading(90)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(length / 2)
    turtle.down()
    turtle.setheading(0)
    turtle.forward(length)
    turtle.setheading(135)
    turtle.forward(length / 2 * (pow(2, .5)))
    turtle.setheading(225)
    turtle.forward(length / 2 * (pow(2, .5)))
    # bring turtle to bottom of tree trunk so that move_to_next brings turtle to correct position
    turtle.up()
    turtle.setheading(270)
    turtle.forward(height)
    turtle.setheading(0)
    turtle.forward(length / 2)
    return length


def draw_circle(height):
    """ draws circle at top of tree trunk for maple tree
    :param : height
    :pre:  heading(east), up
    :post:  heading(east), up
    :return: diameter
    """
    radius = SEPERATION - 65
    turtle.up()
    turtle.setheading(90)
    turtle.forward(height)
    turtle.down()
    turtle.setheading(0)
    turtle.circle(radius)
    turtle.up()
    turtle.setheading(270)
    turtle.forward(height)
    turtle.setheading(180)
    return radius*2


def draw_square(height):
    """ draws square at top of tree trunk for walnut tree
    :param: height
    :pre:  heading(east), up
    :post:  heading(east), up
    :return: length
    """
    turtle.up()
    turtle.setheading(180)
    turtle.forward((SEPERATION - 25) / 2)
    turtle.setheading(90)
    turtle.forward(height)
    turtle.down()
    turtle.setheading(0)
    turtle.forward(SEPERATION - 25)
    turtle.setheading(90)
    turtle.forward(SEPERATION - 25)
    turtle.setheading(180)
    turtle.forward(SEPERATION - 25)
    turtle.setheading(270)
    turtle.forward(SEPERATION - 25)
    turtle.up()
    turtle.setheading(270)
    turtle.forward(height)
    turtle.setheading(0)
    turtle.forward((SEPERATION - 25) / 2)
    return SEPERATION-25;

def draw_trunk(height):
    """ draws tree trunk of specified height, ending at base of tree
    :param: height
    :pre:  heading(east), up
    :post:  heading(east), up
    :return: none
    """
    turtle.down()
    turtle.setheading(90)
    turtle.forward(height)
    turtle.setheading(270)
    turtle.forward(height)


def draw_pine_tree():
    """ draws pine tree of random height and returns height
    :pre:  heading(east), up
    :post:  heading(east), up
    :return: trunk height and branch height
    """
    height = random.randint(50, 200)
    draw_trunk(height)
    branch_height = draw_triangle(height)
    return height, branch_height


def draw_maple_tree():
    """ draws maple tree of random height and returns height
    :pre:  heading(east), up
    :post:  heading(east), up
    :return: trunk height and branch height
    """
    height = random.randint(50, 150)
    draw_trunk(height)
    branch_height = draw_circle(height)
    return height, branch_height


def draw_walnut_tree():
    """ draws walnut tree of random height and returns height
    :pre:  heading(east), up
    :post:  heading(east), up
    :return: trunk height and branch height
    """
    height = random.randint(50, 250)
    draw_trunk(height)
    branch_height = draw_square(height)
    return height, branch_height


def starting_position():
    """ moves turtle to good starting location
    :pre:  heading(east), up
    :post:  heading(east), up
    :return: none
    """
    turtle.up()
    turtle.setheading(0)
    turtle.forward(100)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(0)
    turtle.down()


def draw_star(position, highest_tree):
    """draws the star in night scene
    :param: position, highest_tree
    :pre:  heading(east), up
    :post:  heading(east), up
    :return: none
    """
    turtle.setposition(position)
    turtle.up()
    turtle.setheading(90)
    turtle.forward(highest_tree+10)
    turtle.down()
    turtle.forward(30)
    turtle.right(180)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.back(30)
    turtle.forward(15)
    turtle.left(45)
    turtle.forward(15)
    turtle.back(30)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.back(30)
    turtle.up()
    turtle.setposition(position)
    turtle.back(5)
    turtle.setheading(45)
    turtle.forward(5)
    turtle.back(10)
    turtle.forward(5)
    turtle.setheading(90)
    turtle.forward(10)
    turtle.back(10)
    turtle.up()
    turtle.setposition(position)
    turtle.setheading(0)


def draw_night_scene(num_trees, is_house):
    """ draws night scene
    :param: num_trees, is_house
    :pre:  heading(east), up
    :post:  heading(east), up
    :return: wood_available
    """
    wood_sum = 0
    highest_tree = 0
    temp_height = 0
    house_flag = is_house
    branch_height = 0

    #generate random house location if user wants house
    if is_house:
        house_location = random.randint(1, num_trees - 1)
    # have to add +1 to range to include drawing house
    for i in range(num_trees + 1):

        # if user doesn't want a house, we don't need the extra loop iteration
        if not house_flag:
            house_flag = True
            continue

        # generate random tree and draw it, keeping track of largest tree height
        tree_type = random.randint(0, 2)
        if is_house and i == house_location:
            wood_sum += draw_house(100)
        elif tree_type == 0:
            temp_height, branch_height = draw_pine_tree()
            highest_tree_temp = temp_height + branch_height
            wood_sum += temp_height
        elif tree_type == 1:
            temp_height, branch_height = draw_maple_tree()
            wood_sum += temp_height
            highest_tree_temp = temp_height + branch_height
        elif tree_type == 2:
            temp_height, branch_height = draw_walnut_tree()
            wood_sum += temp_height
            highest_tree_temp = temp_height + branch_height

        if highest_tree_temp > highest_tree :
            highest_tree = highest_tree_temp

        # makes sure drawing ends at the last tree trunk
        if i != num_trees:
            move_to_next()

    draw_star(turtle.pos(), highest_tree)
    return wood_sum


def bind(available_wood):
    """ binds the onscreen click event with draw_day function
    :param available_wood:
    :return: draw_day function
    """
    def draw_day(x,y):
        """function to draw day scene with a house and sun, triggered on mouse click"""
        turtle.reset()
        turtle.setworldcoordinates(0, 0, XWIDTH, YHEIGHT)
        #calculating side of the house based on equation wood = 2side + 1.414*side
        house_side = float(available_wood / 3.414)
        print('you will build the house of sides')
        print(house_side)
        #draws the house
        draw_house(house_side)
        #calculates height of sun to be placed
        height_sun = house_side + (house_side/2)
        position = turtle.pos()
        turtle.setworldcoordinates(0, 0, XWIDTH, YHEIGHT)
        turtle.up()
        turtle.forward(house_side/2)
        turtle.forward(house_side/4)
        turtle.left(90)
        turtle.forward(height_sun+70)
        turtle.down()
        #draws sun
        turtle.circle(30)
        turtle.up()
        turtle.setheading(0)
        print('Day is done . House is built')
        #sys.exit(0)
    return draw_day


def main():
    """ main function that calls night and day scene """
    turtle.setup(width=XWIDTH, height=YHEIGHT, startx=0, starty=0)
    turtle.setworldcoordinates(0, 0, XWIDTH, YHEIGHT)
    turtle.speed(0)
    num_trees = int(input('Enter number of trees: '))
    house_input = input('Would you like a house?: (yes or no) ')
    if house_input == 'yes':
        is_house = True
    else:
        is_house = False

    starting_position()
    #draw night scene
    available_wood = draw_night_scene(num_trees, is_house)
    print('We have this much units of lumber for building')
    print(available_wood)
    print('Click on screen to continue to day scene')
    #draw day scene
    turtle.onscreenclick(bind(available_wood))
    turtle.mainloop()

if __name__ == '__main__':
    main()
