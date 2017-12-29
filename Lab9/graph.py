__author__ = 'jrl'
__author__ = 'sk'

"""
CSCI 603, Lab 9
File: graph.py
Language: python3
Author: Justin Lad jrl8632@g.rit.edu
Author: Sagar Kukreja sk3126@rit.edu

Imports vertex object from vertex class
"""

from vertex import Vertex

class Graph:
    """
    A graph implemented as an adjacency list of vertices (directed, unweighted).

    :slot: vertList (list):  A list that holds all of the vertex objects
    :slot: numVertices (int):  The total number of vertices in the graph
    :slot: file_name (string): The file name
    :slot: paintballs (list):  A list that holds all of the paintball vertices
    :slot: cows (list):  A list that holds all of the cow vertices
    """

    __slots__ = 'vertList', 'numVertices', 'file_name', 'paintballs', 'cows'

    def __init__(self, file_name=None):
        """
        Initialize the graph
        :return: None
        """
        self.vertList = []
        self.numVertices = 0
        self.file_name = file_name
        self.paintballs = []
        self.cows = []
        if not file_name == None:
            self.build_graph()
            self.set_connections()

    def build_graph(self):
        """
        iterates through the file and instantiates vertex nodes for each line
        in file
        :return None
        """
        count = 0
        is_pb = False
        name = ''
        color = ''
        x = 0
        y = 0
        radius = 0

        try:
            with open(self.file_name, 'r') as f:
                for line in f:
                    info = line.split()
                    for data in info:
                        if count == 0:
                            if data == 'paintball':
                                is_pb = True
                            else:
                                is_pb = False
                        if is_pb:
                            if count == 1:
                                color = data
                            elif count == 2:
                                x = int(data)
                            elif count == 3:
                                y = int(data)
                            elif count == 4:
                                radius = int(data)
                            count += 1
                        else:
                            if count == 1:
                                name = data
                            elif count == 2:
                                x = int(data)
                            elif count == 3:
                                y = int(data)
                            count += 1
                    count = 0

                    if(is_pb):
                        #now can Initialize a paintball Vertex
                        v = Vertex(True, x, y, None, color, radius)
                        self.paintballs.append(v)
                        self.vertList.append(v)
                        self.numVertices += 1
                    else:
                        #now can Initialize a cow Vertex
                        v = Vertex(False, x, y, name)
                        self.cows.append(v)
                        self.vertList.append(v)
                        self.numVertices += 1
        except:
            print('File not found: '+ self.file_name)
            exit()

    def set_connections(self):
        """
        iterate through each paintball and see which connections they have
        Uses distance formula implemented in calc_distance to check if the
        current vertex is within reach of the current paintball

        :return None
        """
        for ball in self.paintballs:
            for other_ball in self.paintballs:
                if ball == other_ball:
                    pass
                elif(self.calc_distance(ball, other_ball) <= ball.get_radius()):
                    self.addEdge(ball, other_ball)
            for cow in self.cows:
                if(self.calc_distance(ball, cow) <= ball.get_radius()):
                    self.addEdge(ball, cow)


    def clean_cows(self):
        """
        removes paint from all the cows, so they are ready to be painted by the next ball
        :return None
        """
        for cow in self.cows:
            cow.remove_paint()

    def print_cows(self):
        """
        all of the cows and the colors they were painted in the round are
        returned in a list
        :return result: the list of all the cows and what color they have been painted
        """
        result = []
        index = 0
        had_paint = False
        for cow in self.cows:
            result.append('')
            result[index] = cow.name + ' { '
            for x in cow.painted_colors:
                result[index] += x + ', '
                had_paint = True
            if had_paint:
                result[index] = result[index][:-2]
            result[index] += ' } '
            result[index] += '\n'
            index += 1
            had_paint = False
        return result



    def calc_distance(self, point_a, point_b):
        """
        calculates the distance between vertex a and vertex b
        :param point_a: starting vertex
        :param point_b: ending vertex
        :return [float] the distance between vertex A and Vertex B
        """
        x = (point_a.get_x() - point_b.get_x()) ** 2
        y = (point_a.get_y() - point_b.get_y()) ** 2
        return (x + y) ** .5


    def addVertex(self, key):
        """
        Add a new vertex to the graph.
        :param key: The identifier for the vertex (typically a string)
        :return: Vertex
        """
        # count this vertex if not already present
        if self.getVertex(key) == None:
            self.numVertices += 1
            vertex = Vertex(key)
            self.vertList[key] = vertex
        return vertex

    def getVertex(self, key):
        """
        Retrieve the vertex from the graph.
        :param key: The vertex identifier
        :return: Vertex if it is present, otherwise None
        """
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, key):
        """
        Returns whether the vertex is in the graph or not.  This allows the
        user to do:

            key in graph

        :param key: The vertex identifier
        :return: True if the vertex is present, and False if not
        """
        return key in self.vertList

    def addEdge(self, src, dest):
        """
        Add a new directed edge from a source to a destination of an edge cost.
        :param src: The source vertex identifier
        :param dest: The destination vertex identifier
        :return: None
        """
        src.addNeighbor(dest)

    def getVertices(self):
        """
        Return the collection of vertex identifiers in the graph.
        :return: A list of vertex identifiers
        """
        return self.vertList.keys()

    def __iter__(self):
        """
        Return an iterator over the vertices in the graph.  This allows the
        user to do:

            for vertex in graph:
                ...

        :return: A list iterator over Vertex objects
        """
        return iter(self.vertList)

