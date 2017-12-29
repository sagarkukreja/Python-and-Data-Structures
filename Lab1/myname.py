__author__ = 'sk'

"""
CSCI-603 : Assignment 1
Author: Sagar Kukreja (sk3126@crit.edu)

This is a  program that draws person's last name using turtle.  It demonstrates
the importance of using a hierarchy of functions that can be re-used.
"""

import turtle


# global constants for window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

def init():
    """
    Initialize for drawing.  (-800, -800) is in the lower left and
    (800, 800) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (-750,0), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH, -WINDOW_HEIGHT,
        WINDOW_WIDTH, WINDOW_HEIGHT)
    turtle.up()
    turtle.setposition(-750,0)
    turtle.title('Print Name')
    turtle.speed(0)

def draw_space():
    """
    Initialize for spacing.
    :pre: heading (east), up
    :post: heading (east), up
    :return: None
    """
    turtle.up()
    turtle.forward(170)

def drawK() :
    """
    draws letter 'K'
    :pre: pos(-750, 0), heading(east), up
    :post: pos(-750, 0), heading(east), up
    """

    turtle.down()
    turtle.left(90)
    turtle.forward(300)
    turtle.up()
    turtle.right(180)
    turtle.forward(150)
    turtle.down()
    turtle.left(135)
    turtle.forward(212)
    turtle.back(212)
    turtle.right(90)
    turtle.forward(212)
    turtle.up()
    turtle.back(212)
    turtle.right(45)
    turtle.forward(150)
    turtle.up()
    turtle.left(90)



def drawU():

    """
    draws letter 'U'
    :pre: pos(-580, 0), heading(east), up
    :post: pos(-580, 0), heading(east), up
    """

    turtle.left(90)
    turtle.forward(30)
    turtle.down()
    turtle.forward(270)
    turtle.back(270)
    turtle.right(135)
    turtle.forward(36)
    turtle.left(45)
    turtle.forward(130)
    turtle.left(45)
    turtle.forward(36)
    turtle.left(45)
    turtle.forward(270)
    turtle.up()
    turtle.back(300)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(180)

def drawR():

    """
    draws letter 'R'
    :pre: pos(-410, 0), heading(east), up
    :post: pos(-410, 0), heading(east), up
    """

    turtle.down()
    turtle.left(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(135)
    turtle.forward(212)
    turtle.up()
    turtle.back(212)
    turtle.right(45)
    turtle.forward(150)
    turtle.left(90)

def drawE():

    """
    draws letter 'E'
    :pre: pos(-240, 0), heading(east), up
    :post: pos(-240, 0), heading(east), up
    """

    turtle.down()
    turtle.left(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(150)
    turtle.up()
    turtle.back(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()
    turtle.forward(150)
    turtle.up()
    turtle.back(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()
    turtle.forward(150)
    turtle.up()
    turtle.back(150)

def drawJ():

    """
    draws letter 'J'
    :pre: pos(-70, 0), heading(east), up
    :post: pos(-70, 0), heading(east), up
    """

    turtle.left(90)
    turtle.forward(30)
    turtle.right(135)
    turtle.down()
    turtle.forward(42)
    turtle.left(45)
    turtle.forward(45)
    turtle.left(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(75)
    turtle.back(150)
    turtle.up()
    turtle.right(90)
    turtle.forward(300)
    turtle.left(90)

def drawA():

    """
    draws letter 'A'
    :pre: pos(100, 0), heading(east), up
    :post: pos(100, 0), heading(east), up
    """

    turtle.left(90)
    turtle.down()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.back(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.up()
    turtle.right(90)
    turtle.forward(150)
    turtle.right(180)

def main():

    """
    The main function.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """

    init()
    drawK()
    draw_space()
    drawU()
    draw_space()
    drawK()
    draw_space()
    drawR()
    draw_space()
    drawE()
    draw_space()
    drawJ()
    draw_space()
    drawA()
    turtle.setposition(0,0)

    turtle.mainloop()

if __name__ == '__main__':
    main()