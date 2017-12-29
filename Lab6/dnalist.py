__author__ = 'sk'

"""
CSCI 603 = Assignment 06
File: DNAList.py
Language: python3
Author:  Sagar Kukreja sk3126@rit.edu
The program implements a list
"""
import sys
from Node import LinkedNode

class DNAList:

    __slots__ = "head","rear","length"

    def __init__(self, gene="",length = 0):
        """
        This function creates a new list. Thegeneargument isan optional argument
         for which a default (empty string) value is provided
        :param gene:
        :param length:
        """

        self.head = None
        self.rear = None
        self.length = 0


        if gene:
            for i in range(len(gene)):
                if self.head == None:
                    self.head = LinkedNode(gene[i])
                    tmp = self.head
                    self.length += 1
                else:
                    newNode = LinkedNode(gene[i])
                    tmp.link = newNode
                    tmp = tmp.link
                    self.length += 1
                self.rear = tmp


    def append(self, item):
        """
        This function takes in a single character and extends the list with a node that represents this character
        :param: item
        :return: list
        """
        tmp = self.head
        newNode = LinkedNode(item)
        self.length +=1
        if tmp == None:
            self.head = newNode
            tmp = self.head

        else:
            tmp = self.rear
            tmp.link = newNode
        self.rear = newNode
        return self

    def join(self, other):
        """
        This function takes in another DNAList and adds it to the end of the list.
        :param: other list
        :return: list
        """
        tmp = self.head

        if self.head == None:
            self.head = other.head
            self.rear = other.rear
        else:
            self.rear.link = other.head
            self.rear = other.rear

        self.length = self.length + other.length
        return self

    def copy(self):
        """
        This function returns a new list with the same contents as the list called upon.
        :return:=list
        """
        tmp = self.head
        copyList = DNAList()
        if tmp == None:
            return copyList
        else:
            newNode = LinkedNode(tmp.value)
            copyList.head = newNode
            copyList.length += 1
            copyTmp = copyList.head

            while tmp.link != None:
                tmp = tmp.link
                newNode = LinkedNode(tmp.value)
                copyTmp.link = newNode
                copyList.length += 1
                copyTmp = newNode
            copyList.rear = copyTmp
            return copyList


    def __str__(self):
        """
        This should simply return a string with the contents of the nodesall together,
        :return:string
        """
        tmp = self.head
        if tmp == None:
            print("List is empty")
            s =" "

        else:
            s = ""
            while tmp != None:
                s = s + str(tmp.value)
                tmp = tmp.link
        return s


    def snip(self, i1, i2):
        """
        This function removes a portion of the gene (list) as specified
        by the integers i1 and i2.Specifically, counting from the beginning of the list as 0
        ,the list should no longer contain all nodes from the node at positioni1(inclusive)
        up to but not including positioni2
        :param i1:index 1
        :param i2:index 2
        :return:list
        """
        count = 0
        diff = i2 - i1
        if i1 > i2:
            print("enter correct values")
            sys.exit(0)

        elif  i1 == i2:
            print("enter correct values")
            sys.exit(0)

        elif i1 == 0:
            tmp = self.head
            while count < i2:
                tmp = tmp.link
                count += 1
            self.head = tmp
            if self.head == None:
                self.rear = None


        elif i2 == self.length and i1 != 0:
            tmp = self.head
            while count < i1-1:
                tmp = tmp.link
                count += 1
            tmp.link = None
            self.rear = tmp


        elif i1 != 0 and i2 != self.length:
            tmp = self.head

            while count < self.length:
                count += 1
                if count == i1:
                    i1node = tmp

                if count == i2:
                    i2node = tmp
                tmp = tmp.link
            self.rear = tmp
            i1node.link = i2node.link
        return self


    def splice(self,ind,other):
        """
        This  function  takes  in  an  integer ind representing  an index
        into the list, and another DNAList. It should then insert the other list into
        the list immediately after the ind'th character of this list
        :param ind:
        :param other:
        :return:list
        """
        headN = self.head
        len = 0
        while headN != None and len <= ind-1:
            headN = headN.link
            len += 1
        if headN == None:
            print("Wrong Indices value")
            sys.exit(1)
        middle = headN.link

        if other != None:
            headN.link = other.head

        other.rear.link = middle
        return self

    def replace(self, repstr, other):
        """
        This  function  should find  the string repstr as
        a subsequence of the list and replace it with
        the list given by other.
        :param repstr:
        :param other:
        :return: list
        """
        tmp = self.head
        curString = ''
        tmpBack = self.head
        found = False
        while tmp != None:
            curString += tmp.value
            if curString in repstr:
                if curString == repstr:
                    found = True
                    if self.head.value == repstr[0]:
                        self.head = other.head
                        other.rear.link = tmp.link
                    else:
                        tmpBack.link = other.head
                        other.rear.link = tmp.link
                else:
                    tmp = tmp.link
            else:
                curString = ''
                tmpBack = tmp
                tmp = tmp.link
        if found == False:
            print("\nstring not present\n")
        return self
