__author__ = 'jrl'
__author__ = 'sk'

"""
CSCI 603, Lab 9
File: Vertex.py
Language: python3
Author: Justin Lad jrl8632@g.rit.edu
Author: Sagar Kukreja sk3126@rit.edu

"""
class Vertex:
    """
    An individual vertex in the graph.

    :slot: is_paintball (boolean): true if it is a paint ball, false if it's a cow vertex
    :slot: x_cord (int): the x_coordinate of the vertex on the map
    :slot: y_cord (int): the y_coordinate of the vertex on the map
    :slot: color (string):  the color of the ball (if is_paintball)
    :slot: name (string):    the name of the cow (if not a paintball)
    :slot: splash_radius (int): the splash radius (if is_paintball)
    :slot: connectedTo (list):  A list of adjacent neighbors
    :slot: painted_colors (list): a list of all the colors a cow has been painted
    """

    __slots__ = 'is_paintball', 'x_cord', 'y_cord', 'color', 'name','splash_radius', 'connectedTo', 'painted_colors'


    def __init__(self, is_pb, x, y, name = None, color=None, radius=None):
        """
        Initialize a vertex
        :param key: The identifier for this vertex
        :return: None
        """
        self.is_paintball = is_pb
        self.x_cord = x
        self.y_cord = y
        self.name = name
        self.color = color
        #print("THIS IS THE RADIUS IN VERTEX CONSTRUCTOR: " + str(radius))
        self.splash_radius = radius
        self.connectedTo = []
        self.painted_colors = []

    def addNeighbor(self, nbr):
        """
        Connect this vertex to a neighbor
        :param nbr (Vertex): The neighbor vertex
        :return: None
        """
        self.connectedTo.append(nbr)

    def addPaint(self, pigment):
        """
        adds a color to the cow's paint list
        :param pigment: the color to add to list
        :return: None
        """
        self.painted_colors.append(pigment)

    def remove_paint(self):
        """
        removes paint_colors list so that cow is clean for next round
        :return: None
        """
        self.painted_colors = []

    def __str__(self):
        """
        Return a string representation of the vertex and its direct neighbors:

            vertex-id connectedTo [neighbor-1-id, neighbor-2-id, ...]

        :return: The string
        """
        if(self.is_paintball):
            neighbors = []
            for x in self.connectedTo:
                if(x.is_paintball):
                    neighbors.append(x.color)
                else:
                    neighbors.append(x.name)
            return str(self.color) + ' connectedTo: ' + str(neighbors)
        else:
            return str(self.name) + ' connectedTo: ' + str([str(x.name) for x in self.connectedTo])


    def getConnections(self):
        """
        Get the neighbor vertices.
        :return: A list of Vertex neighbors
        """
        return self.connectedTo
        # return self.connectedTo.keys()

    def getWeight(self, nbr):
        """
        Get the edge cost to a neighbor.
        :param nbr (Vertex): The neighbor vertex
        :return: The weight (int)
        """
        return self.connectedTo[nbr]

    def get_x(self):
        """
        :return: returns x coordinate of this vertex
        """
        return self.x_cord

    def get_y(self):
        """
        :return: returns y coordinate of this vertex
        """
        return self.y_cord

    def get_radius(self):
        """
        :return: radius of the paintball splash
        """
        return self.splash_radius
