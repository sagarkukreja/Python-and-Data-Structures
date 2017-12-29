__author__ = 'jrl'
__author__ = 'sk'

"""
CSCI 603, Lab 9
File: holicow.py
Language: python3
Author: Justin Lad jrl8632@g.rit.edu
Author: Sagar Kukreja sk3126@rit.edu
"""
from graph import Graph
from sys import argv

class holicow:
    """
    drives the exploding paint balls simulation

    :slot: field (Graph): graph that holds the graph representation of the input file
    :slot: max_number (int): holds the max number of cows colored so far
    :slot: max_id (int): holds the id of the paintball that triggered the most cow color
            used to print correct cow color results
    :slot max_color (string): holds the paintball color that triggered the most color
    :slot: cow_paint_list (list): holds the list of all the cow color results for each
            paintball that was exploded.
    """

    __slots__ = 'field',  'max_number', 'max_id', 'max_color', 'cow_paint_list'

    def __init__(self, file_name):
        """
        initializes cow coloring simulation object
        """
        self.field = Graph(file_name)
        self.max_number = 0
        self.max_id = 0
        self.max_color = ''
        self.cow_paint_list = []


    def find_path(self, vertex):
        """
        breadth first search, starting at input vertex.
        iterates all possible moves from starting vertex

        :param start (Vertex): the start vertex
        :return: the number times a cow was painted during the BFS
        """
        # Using a queue as the dispenser type will result in a breadth first
        # search
        num_cow_hit = 0
        queue = []
        queue.append(vertex)         # prime the queue with the start vertex

        # The predecessor dictionary maps the current Vertex object to its
        # immediate predecessor.  This collection serves as both a visited
        # construct, as well as a way to find the path
        predecessors = {}
        predecessors[vertex] = None  # add the start vertex with no predecessor

        # Loop until either the queue is empty, or the end vertex is encountered
        while len(queue) > 0:
            current = queue.pop(0)
            for neighbor in current.getConnections():
                if neighbor.is_paintball:
                    print('\t' + neighbor.color + ' paintball is triggered by ' + current.color + ' paint ball')
                    if neighbor not in predecessors:        # if neighbor unvisited
                        predecessors[neighbor] = current    # map neighbor to current
                        queue.append(neighbor)              # enqueue the neighbor
                else:
                    print('\t'+neighbor.name + ' is painted ' + current.color)
                    num_cow_hit += 1
                    neighbor.addPaint(current.color)
        return num_cow_hit

    def print_field(self):
        """
        prints the graph
        :return None
        """
        print('Field of Dreams')
        print('---------------------------')
        for item in self.field:
            print(item)
        print('\n')

    def simulation(self):
        """
        runs the simulation part of the game, to see which paintball will be most effective
        :return None
        """
        curScore = 0
        max_number = 0
        max_color = ''
        ids = 0
        print(' ---- Beginning simulation ----')
        for item in self.field:
            if item.is_paintball:
                print('Triggering ' + item.color + ' paint ball... ')
                curScore = self.find_path(item)
                self.cow_paint_list.append(self.field.print_cows())
                if curScore > self.max_number:
                    self.max_number = curScore
                    self.max_color = item.color
                    self.max_id  = ids
                ids += 1
                self.field.clean_cows()
        print('\n')

    def results(self):
        """
        prints the results of the simulations
        :return None
        """
        print('Results:')
        if self.max_number == 0:
            print('No cows were painted by any starting paint ball!')
            for cow in self.cow_paint_list[self.max_id]:
                print(cow)

        else:
            print("Triggering the "+ self.max_color + ' paintball is the best choice with ' + str(self.max_number) + ' total paint on the cows: ')
            for cow in self.cow_paint_list[self.max_id]:
                print(cow)


def main():
    if(len(argv)!=2):
        print('Usage: python3 holicow.py')
        exit()
    the_field = holicow(argv[1])
    the_field.print_field()
    the_field.simulation()
    the_field.results()


if __name__ == '__main__':
    main()
