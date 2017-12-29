__author__ = 'sk'
__author__ = 'jrl'

"""
CSCI 603 = Assignment 06
File: genetester.py
Language: python3
Author: Justin Lad jrl8632@g.rit.edu
Author:  Sagar Kukreja sk3126@rit.edu
The program is a test class for DNAList
"""
from dnalist import DNAList

class test:

    def test_join(self,list1, list2):
        """
        test for join operation
        :param: list2,list1
        :return:
        """
        print("\nJoin operation::\n")
        print("original list 1 is:")
        print(list1)
        print("original list 2 is:")
        print(list2)
        print("new list after join is: ")
        print(list1.join(list2))

    def test_append(self,list,item):
        """
        test for append operation
        :param: list
        :param : item
        :return:
        """
        print("\nappend operation::\n")
        print("original list is:")
        print(list)
        print("new list after append is: ")
        print(list.append(item))

    def test_replace(self,list1,list2):
        """
        test for operation replace
        :return:
        """
        repstr = "GT"
        print("\nReplace operation::\n")
        print("original list 1 is:")
        print(list1)
        print("original list 2 is:")
        print(list2)
        print("list after replace  with string ",repstr)
        print(list1.replace(repstr, list2))

    def test_splice(self, list1, list2):
        """
        tests splice operation
        :param list1:
        :param index:
        :param list2:
        :return:
        """
        index = 0
        print("\nSplice operation::\n")
        print("original list 1 is:")
        print(list1)
        print("original list 2 is:")
        print(list2)
        print("list after splice  after index ",index)
        print(list1.splice(index,list2))

    def test_snip(self,list1):
        """
        test for snip function
        :param self:
        :param list1:
        :return:
        """
        index1 = 0
        index2 = 5
        print("\nSnip operation::\n")
        print("original list is:")
        print(list1)
        print("indices are ",index1 ,index2)
        print("list after snip  ")
        print(list1.snip(index1, index2))

    def test_copy(self, list):
        """
        test for copy operation
        :param self:
        :param list:
        :return:
        """
        print("\ncopy operation::\n")
        newList = list.copy()
        print("Copied list is :")
        print(newList)
        print("original list is: ")
        print(list)

def main():
    """
    main class
    :return:
    """
    test1 = test()
    list1 = DNAList()
    list2 = DNAList("GCC")
    list3 = DNAList("GCACT")
    list4 = DNAList("CTT")
    list5 = DNAList("TAGC")
    list6 = DNAList("GTA")
    list7 = DNAList("GCATACGT")
    list8 = DNAList("TGG")
    test1.test_copy(list2)
    test1.test_append(list1,"G")
    test1.test_join(list2,list3)
    test1.test_splice(list4,list5)
    test1.test_snip(list7)
    test1.test_replace(list6,list8)


if __name__ == '__main__':
    main()