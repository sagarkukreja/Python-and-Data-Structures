__author__ = 'sk'
__author__ = 'jrl'

"""
CSCI 603 = Assignment 03
File: polygons.py
Language: python3
Author: Justin Lad jrl8632@g.rit.edu
Author:  Sagar Kukreja sk3126@rit.edu
The program draws polygons using recursion and returns the total length of sides drawn.
"""

import turtle
import sys

#constants for color used at each depth
COLORS = 'red','orange','black','yellow','blue', 'red','green','orange','purple'

# Window dimensions
WINDOW_LENGTH = 800
SIDE_LENGTH = 200

#pen sizes to be used for filled and unfilled polygons
FILL_PEN_WIDTH = 2
UNFILL_PEN_WIDTH = 8
FILL = True

def init():
    """ initializes the turtle and writes name of team on screen
        :pre:  heading(east), up
        :post:  heading(east), up
        :return: trunk height and branch height
    """
    turtle.setup(width=WINDOW_LENGTH, height = WINDOW_LENGTH, startx=200, starty=200)
    turtle.speed(0)
    turtle.setheading(0)
    turtle.up()
    turtle.back(400)
    turtle.write("Designers :: Justin & Sagar",True, "left", font = ("Arial",10,"normal"))
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.setheading(0)
    turtle.tracer(0,0)

def draw(side, SIDE_LENGTH,FILL):
    """ draws polygon recursively
        :pre:  heading(east), up
        :post:  heading(east), down
        :return: sum of all sides drawn
    """

    sum = 0
    if side > 2:
        angle = (360) / side

        if FILL == True:
            turtle.color(COLORS[side], COLORS[side])
            turtle.begin_fill()
            for _ in range(1, side + 1, 1):
                turtle.up()
                turtle.forward(SIDE_LENGTH)
                turtle.left(angle)
            turtle.end_fill()

        turtle.down()
        for _ in range(1,side+1,1):
            turtle.pencolor(COLORS[side])
            turtle.forward(SIDE_LENGTH)
            sum += SIDE_LENGTH
            turtle.left(angle)
            sum += draw(side-1,SIDE_LENGTH/2,FILL)
    return sum

def main():
    """ Main function , takes input and draws polygoon and prints sum of sides
        :pre:  heading(east), up
        :post:  heading(east), down
    """

    if(len(sys.argv) > 3 or len(sys.argv) < 3 ):
        print('enter correct number of arguments')
        sys.exit(0)
    else:
        #command line input for number of sides
        num_sides = int(sys.argv[1])
        if  num_sides < 3 or num_sides > 8:
            print('Enter correct sides')
            sys.exit(0)
        else:
            init()
            #command line input for fill unfill option
            fill_unfill = sys.argv[2].lower()

            if fill_unfill == 'fill' or fill_unfill == 'unfill':
                if fill_unfill == 'fill':
                    FILL = True
                    turtle.pensize(FILL_PEN_WIDTH)
                else:
                    FILL = False
                    turtle.pensize(UNFILL_PEN_WIDTH)

                #print the length of sides drawn
                print('Length of total sides drawn is : ')
                print(draw(num_sides,SIDE_LENGTH,FILL))
                turtle.update()
                turtle.hideturtle()
                turtle.mainloop()
            else:
                print('enter correct input')
                sys.exit(0)

if __name__ == '__main__':
    main()