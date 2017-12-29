__author__ = 'sk'
__author__ = 'jrl'

"""
CSCI 603 = Assignment 06
File: genetester.py
Language: python3
Author: Justin Lad jrl8632@g.rit.edu
Author:  Sagar Kukreja sk3126@rit.edu
The program implements hashtable
"""
from collections import namedtuple
import re
Entry = namedtuple('Entry', ('key', 'value'))

'''
To make sure that the DELETED sentinel does not match
anything we actually want to have in the table, make it
a unique (content-free!) object.
'''
class _delobj: pass
DELETED = Entry(_delobj(),None)

class Hashmap:

    __slots__ = 'table','numkeys','cap','maxload', 'probeCount','collisionCount','hashType'

    def __init__(self,initsz=100,maxload=0.7, hashType = 1):
        '''
        Creates an open-addressed hash map of given size and maximum load factor
        :param initsz: Initial size (default 100)
        :param maxload: Max load factor (default 0.7)
        '''
        self.cap = initsz
        self.table = [None for _ in range(self.cap)]
        self.numkeys = 0
        self.maxload = maxload
        self.probeCount = 0
        self.collisionCount = 0
        self.hashType = hashType

    def put(self,key,value):
        '''
        Adds the given (key,value) to the map, replacing entry with same key if present.
        :param key: Key of new entry
        :param value: Value of new entry
        '''
        index = self.hash_func(key) % self.cap
        if self.table[index] is not None:
            self.collisionCount += 1
            self.probeCount += 1
        while self.table[index] is not None and \
                        self.table[index] != DELETED and \
                        self.table[index].key != key:
            index += 1
            self.probeCount += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is None:
            self.numkeys += 1
            self.probeCount += 1
        self.table[index] = Entry(key,value)
        if self.numkeys/self.cap > self.maxload:
            # rehashing
            oldtable = self.table
            # refresh the table
            self.cap *= 2
            self.table = [None for _ in range(self.cap)]
            self.numkeys = 0
            # put items in new table
            for entry in oldtable:
                if entry is not None:
                    self.put(entry[0],entry[1])


    def remove(self,key):
        '''
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.table[index] = DELETED


    def get(self,key):
        '''
        Return the value associated with the given key
        :param key: Key to look up
        :return: Value (or KeyError if key not present)
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            self.probeCount += 1
            if index == self.cap:
                index = 0
        if self.table[index] is not None:
            return self.table[index].value
        else:
            raise KeyError('Key ' + str(key) + ' not present')

    def contains(self,key):
        '''
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            self.probeCount += 1
            if index == self.cap:
                index = 0
        return self.table[index] is not None

    def hash_func(self,key):
        '''
        Not using Python's built in hash function here since we want to
        have repeatable testing...
        However it is terrible.
        Assumes keys have a len() though...
        :param key: Key to store
        :return: Hash value for that key
        '''
        h = 0
        index = 1
        if self.hashType == 1:
            """
            this hash function calculates the ascii value of each character in word and adds it to final hash value
            """
            for ch in key:
                h += ord(ch)
        elif self.hashType == 2:
            """
            This hash function calculates the weighted ascii value i.e. for cat it does h = ord(c)*1 + ord(a)*2 +ord(t)*3
            """
            for ch in key:
                h += ord(ch)*index
                index += 1
        else:
            """
            implments default hash function
            """
            h = hash(key)
        # if we want to switch to Python's hash function, uncomment this:
        #return hash(key)
        return h

def printMap(map):
    for i in range(map.cap):
        print(str(i)+": " + str(map.table[i]))

def count_words(filename,maxload,hashType):
    """
    counts the words in a file and creates key value pairs , key is word, value is count of that and finds
    the word that occurs most
    :param filename:
    :param hashType:
    :param maxload:
    :return:
    """
    count = 0
    bestCount = -1
    bestWord=""
    words = Hashmap(initsz=500,maxload = maxload ,hashType=hashType)
    with open(filename, encoding="utf-8") as f:
        for line in f:
            for word in re.split('\W+', line):
                word = word.lower()
                try:
                    if word == '':
                        continue
                    count = words.get(word)
                    count += 1
                    words.put(word,count)
                except KeyError:
                    if word == '':
                        continue
                    count = 1
                    words.put(word,count)
                if count >= bestCount:
                    bestCount = count
                    bestWord = word
    print("The best count is :")
    print(bestCount)
    print("The best word is : ")
    print(bestWord)
    print("\nnumber of probes::\n")
    print(words.probeCount)
    print("\nnumber of collisions::\n")
    print(words.collisionCount)
    return words

def main():

    """
    main fucntion
    :return:
    """
    """
    takes three files..counts the words and creates mapping for them, creates key value pairs, key is words 
    values is count of words
    """
    novel1file = "C:\\Users\\Sagar\\PycharmProjects\\Lab7\\prison2.txt"
    novel2file = "C:\\Users\\Sagar\\PycharmProjects\\Lab7\\spirit1.txt"
    dictionaryfile = "C:\\Users\\Sagar\\PycharmProjects\\Lab7\\dict.txt"

    """
    testing for file 1 for all 3 hash functions and 3 different maxloads
    """
    print("testing file 1 for hash function 1 with payload = 0.7...................................\n")
    novel1wordsh1m1 = count_words(novel1file, maxload = 0.7,hashType=1)
    print("testing file 1 for hash function 2 with payload = 0.7...................................\n")
    novel1wordsh2m1 = count_words(novel1file,maxload=0.7, hashType=2)
    print("testing file 1 for default hash function with payload = 0.7...................................\n")
    novel1wordsh3m1 = count_words(novel1file, maxload=0.7,hashType=3 )

    print("testing file 1 for hash function 1 with payload = 0.9...................................\n")
    novel1wordsh1m2 = count_words(novel1file, maxload=0.9, hashType=1)
    print("testing file 1 for hash function 2 with payload = 0.9...................................\n")
    novel1wordsh2m2 = count_words(novel1file, maxload=0.9, hashType=2)
    print("testing file 1 for default hash function with payload = 0.9...................................\n")
    novel1wordsh3m2 = count_words(novel1file, maxload=0.9, hashType=3)

    print("testing file 1 for hash function 1 with payload = 0.5...................................\n")
    novel1wordsh1m3 = count_words(novel1file, maxload=0.5,hashType=1)
    print("testing file 1 for hash function 2 with payload = 0.5...................................\n")
    novel1wordsh2m3 = count_words(novel1file,maxload=0.5, hashType=2)
    print("testing file 1 for default hash function with payload = 0.5...................................\n")
    novel1wordsh3m3 = count_words(novel1file, maxload=0.5,hashType=3)

    """
        testing for file 2 for all 3 hash functions and 3 different maxloads
    """

    print("testing file 2 for hash function 1 with payload = 0.7...................................\n")
    novel2wordsh1m1 = count_words(novel2file,maxload=0.7, hashType=1)
    print("testing file 2 for hash function 2 with payload = 0.7...................................\n")
    novel2wordsh2m1 = count_words(novel2file,maxload=0.7, hashType=2)
    print("testing file 2 for default hash function with payload = 0.7...................................\n")
    novel2wordsh3m1 = count_words(novel2file,maxload=0.7, hashType=3)

    print("testing file 2 for hash function 1 with payload = 0.9...................................\n")
    novel2wordsh1m2 = count_words(novel2file, maxload=0.9,hashType=1 )
    print("testing file 2 for hash function 2 with payload = 0.9...................................\n")
    novel2wordsh2m2 = count_words(novel2file, maxload=0.9, hashType=2)
    print("testing file 2 for default hash function with payload = 0.9...................................\n")
    novel2wordsh3m2 = count_words(novel2file, maxload=0.9, hashType=3)

    print("testing file 2 for hash function 1 with payload = 0.5...................................\n")
    novel2wordsh1m3 = count_words(novel2file, maxload=0.5,hashType=1)
    print("testing file 2 for hash function 2 with payload = 0.5...................................\n")
    novel2wordsh2m3 = count_words(novel2file, maxload=0.5,hashType=2)
    print("testing file 2 for default hash function with payload = 0.5...................................\n")
    novel2wordsh3m3 = count_words(novel2file, maxload=0.5,hashType=3)

    """
    testing for ubuntu dictionary for all 3 hash functions and 3 different maxloads
    """

    print("testing dictionary for hash function 1 with payload = 0.7...................................\n")
    dictionaryfileh1m1 = count_words(dictionaryfile, maxload=0.7, hashType=1)
    print("testing dictionary for hash function 2 with payload = 0.7...................................\n")
    dictionaryfileh2m1 = count_words(dictionaryfile, maxload=0.7,hashType=2)
    print("testing dictionary for default hash function with payload = 0.7...................................\n")
    dictionaryfileh3m1 = count_words(dictionaryfile, maxload=0.7,hashType=3)

    print("testing dictionary for hash function 1 with payload = 0.9...................................\n")
    dictionaryfileh1m2 = count_words(dictionaryfile, maxload=0.9,hashType=1)
    print("testing dictionary for hash function 2 with payload = 0.9...................................\n")
    dictionaryfileh2m2 = count_words(dictionaryfile, maxload=0.9,hashType=2 )
    print("testing dictionary for default hash function with payload = 0.9...................................\n")
    dictionaryfileh3m2 = count_words(dictionaryfile, maxload=0.9,hashType=3)

    print("testing dictionary for hash function 1 with payload = 0.5...................................\n")
    dictionaryfileh1m3 = count_words(dictionaryfile, maxload=0.5,hashType=1)
    print("testing dictionary for hash function 2 with payload = 0.5...................................\n")
    dictionaryfileh2m3 = count_words(dictionaryfile, maxload=0.5,hashType=2)
    print("testing dictionary for default hash function with payload = 0.5...................................\n")
    dictionaryfileh3m3 = count_words(dictionaryfile, maxload=0.5,hashType=3)


if __name__ == '__main__':
    main()