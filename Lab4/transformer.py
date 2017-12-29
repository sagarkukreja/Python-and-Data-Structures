__author__ = 'sk'
__author__ = 'jrl'

"""
CSCI 603 = Assignment 04
File: transformer.py
Language: python3
Author: Justin Lad jrl8632@g.rit.edu
Author:  Sagar Kukreja sk3126@rit.edu
The program implements encryption and decryption
"""
import sys

#ascii value of A and Z
UPPER_BOUND=91
LOWER_BOUND=64

def encryptSigma( msg, i):
    '''
    shifts the letter at index i forward one letter in alphabet
    :param msg: the input String
    :param i: index value
    :return: encrypted message
    '''

    i = int(i)
    if i < 0:
        param=len(msg)-(-i)
    if ord(msg[i]) == 90:
      return msg[:i] + chr(65) + msg[i + 1:]
    else:
        return msg[:i] + chr(ord(msg[i]) + 1) + msg[i + 1:]

def decryptSigma(msg, i):
    '''
    decryption of sigma
    :param msg: the input String
    :param i: index value
    :return: decrypted message
    '''

    i = int(i)
    if i < 0:
        i= len(msg) - (-i)

    if ord(msg[i]) == 65:
        return msg[:i] + chr(90) + msg[i + 1:]

    else:
        return msg[:i] + chr(ord(msg[i]) - 1) + msg[i + 1:]

def encryptSigmaK(msg, i, exponent):
    '''
    shift letter i by exponent forward
    :param msg: the input String
    :param index: index value
    :param exponent: exponent value
    :return: encrypted message
    '''

    i = int(i)
    exponent = int(exponent)
    if i < 0:
        param= len(msg) - (-i)
    k=0
    while(k < exponent%26 ):
        value = ord(msg[i]) + 1
        if(value >= UPPER_BOUND):
            value = 65
        msg= msg[:i] + chr(value) + msg[i + 1:]
        k += 1
    return msg

def decryptSigmaK(msg, i, exponent):
    '''
    decryption of shift operation
    :param msg: the input String
    :param i: index value
    :param exponent: exponent value
    :return: decrypted message
    '''

    i = int(i)
    exponent = int(exponent)
    k = 0
    if i < 0:
        param = len(msg) - (-i)
    while(k < exponent%26 ):
        value = ord(msg[i]) - 1
        if(value == LOWER_BOUND):
            value = 90
        msg= msg[:i] + chr(value) + msg[i + 1:]
        k+=1

    return msg

def transformR(msg, param):
    '''
    roatates the string one position right
    :param msg: the input String
    :param param: index value
    :return: encrypted message
    '''

    param = int(param)
    if param > 0:
     for _ in range(param):
        msg = msg[len(msg) - 1] + msg[:len(msg) - 1]
    else:
        param = -(param)
        for _ in range(param):
            msg = msg[1:] + msg[0]
    return msg

def encryptD(msg, i):
    '''
     String transform using duplicate transformation
    :param msg: the input String
    :param i: index value
    :return: encrypted message
    '''
    i = int(i)
    if i == len(msg) - 1:
        return msg + msg[i]
    return msg[0:i] + msg[i] + msg[i:]

def decryptD(msg, i):
    '''
     Decryption of string using duplicate transformation
    :param msg: the input String
    :param i: index value
    :return: decrypted message
    '''
    i = int(i)
    list =[_ for _ in msg]
    del list[i]
    return ''.join(list)

def encryptDK(msg, i, exponent):
    '''
     String transform using duplicate transformation exponent times
    :param msg: the input String
    :param i: index value
    :param exponent: exponent value
    :return: encrypted message
    '''
    i = int(i)
    exponent = int(exponent)
    str =""
    for _ in range(exponent):
        str = str + msg[i]
    return msg[0:i] + str + msg[i:]

def decryptDK(msg, i, exponent):
    '''
     Decryption of string using duplicate transformation exponent times
    :param msg: the input String
    :param i: index value
    :param exponent: exponent value
    :return: decrypted message
    '''
    i = int(i)
    exponent = int(exponent)
    list =[_ for _ in msg]
    for _ in range(exponent):
        del list[i]
    return ''.join(list)

def transformT(msg, i, j):
    '''
     String transform using swap transformation
    :pre: Original String
    :post:String after swap transformation on index and index2 value
    :param msg: the input String
    :param index1: index value
    :param index2: index value
    :return: encrypted message
    '''
    i = int(i)
    j = int(j)
    newParam1 = min(i,j)
    newParam2 = max(i,j)
    return msg[:newParam1] + msg[newParam2] + msg[newParam1 + 1:newParam2] + msg[newParam1] + msg[newParam2 + 1:]

def transformT1(msg, index1, index2, group):
    '''
     String transform using duplicate transformation
    :param msg: the input String
    :param index1: index value
    :param index2: index value
    :param group: no of groups to be formed.
    :return: encrypted message
    '''
    index1 = int(index1)
    index2 = int(index2)
    newParam1 = min(index1, index2)
    newParam2 = max(index1, index2)
    nGroup=int(len(msg) / group)
    list=[]
    for x in range(group):
        list.append(msg[x * nGroup: (x + 1) * nGroup])

    temp = list[:]
    temp[newParam2] = list[newParam1]
    temp[newParam1] = list[newParam2]
    return ''.join(temp)

def encryptJ(msg, index1, index2, exponent):
    '''
       own transformation:: swap and shift transformation represented by J(k)i,j
       If a string is "CANAL", after J(2)1,4 transformation the string is encrypted as CNNAC
      :return: encrypted message
    '''

    index1 = int(index1)
    index2 = int(index2)
    newParam1 = min(index1, index2)
    newParam2 = max(index1, index2)
    temp1=encryptSigmaK(msg, newParam1, exponent)
    msg = encryptSigmaK(temp1, newParam2, exponent)
    return msg[:newParam1] + msg[newParam2] + msg[newParam1 + 1:newParam2] + msg[newParam1] + msg[
                                                                                                              newParam2 + 1:]
def decryptJ(msg, index1, index2, exponent):
    '''
       swap and shift transformation represented by J(k)i,j
       If a string is CANAL, after J(2)1,4 transformation the string is decrypted as CJNAY
      :param msg: the input String
      :param index1: index value
      :param index2: index value
      :param exponent: shift value
      :return: decrypted message
      '''
    index1 = int(index1)
    index2 = int(index2)
    newParam1 = min(index1, index2)
    newParam2 = max(index1, index2)
    temp1=decryptSigmaK(msg, newParam1, exponent)
    msg = decryptSigmaK(temp1, newParam2, exponent)
    return msg[:newParam1] + msg[newParam2] + msg[newParam1 + 1:newParam2] + msg[newParam1] + msg[
                                                                                                              newParam2 + 1:]


def reorder(transformlist):
    '''
       Reverse the transformlist
      :pre: Original list
      :post:Reverse the order of the list
      :param transformlist: the input list to be reversed
      :return: reversed list
      '''
    return transformlist[::-1]

def methodSE(transindex, msg):
    '''
    method for shift in encryption
    :return: msg
    '''
    if len(transindex) == 1:
        if abs(int(transindex[0])) > len(msg) - 1:
            print("Index out of Bounds")
        else:
            msg = encryptSigma(msg, transindex[0])
    else:
        msg = encryptSigmaK(msg, transindex[0], transindex[1])
    return msg

def methodRE(transindex, msg):
    '''
    method for rotation in encryption
    :return: msg
    '''

    if transindex[0] == '':
        msg = transformR(msg, 1)
    else:
        msg = transformR(msg, transindex[0])
    return msg

def methodDE(transindex, msg):
    '''
    duplicate and encryption
    :return: msg
    '''
    if len(transindex) == 1:
        if int(transindex[0]) < 0:
            print("Operation Not permittted")
            sys.exit(1)
        if int(transindex[0]) <= len(msg) - 1:
            msg = encryptD(msg, transindex[0])
        else:
            print("Please enter valid transformation.")
    else:
        if int(transindex[1]) < 0:
            print("Please enter a positive exponent!")
        else:
            msg = encryptDK(msg, transindex[0], transindex[1])
    return msg

def methodTE(transindex, msg):
    '''
    swap in encryption
    :return: msg
    '''
    if transindex[0].find(')') == -1:
        msg = transformT(msg, transindex[0], transindex[1])
    else:
        group = int(transindex[0][transindex[0].find('(') + 1:transindex[0].find(')')])
        param1 = int(transindex[0][transindex[0].find(')') + 1:])
        param2 = int(transindex[1])
        if len(msg) % group == 0:
            if param2 < group and param1 < group:
                msg = transformT1(msg, param1, param2, group)
            else:
                print("Please Enter valid index")
        else:
            print("Please enter valid group.")
    return msg

def methodJE(transindex, msg):
    '''
    J in encryption
    :return: msg
    '''
    if transindex[0].find(')') == -1:
        msg = encryptJ(msg, transindex[0], transindex[1], 1)
    else:
        exponent = int(transindex[0][transindex[0].find('(') + 1:transindex[0].find(')')])
        param1 = int(transindex[0][transindex[0].find(')') + 1:])
        param2 = int(transindex[1])
        length = len(msg)
        if param2 < length and param1 < length:
            msg = encryptJ(msg, param1, param2, exponent)
        else:
            print("Please Enter valid index")
    return msg

def methodSD(transindex, msg):
    '''
    method for shift operation in decryption
    :return: msg
    '''

    if len(transindex) == 1:
        msg = decryptSigma(msg, transindex[0])
    else:
        msg = decryptSigmaK(msg, transindex[0], transindex[1])
    return msg

def methodRD(transindex, msg):
    '''
    method for rotation and decryption
    :return: msg
    '''

    if transindex[0] == '':
        msg = transformR(msg, -1)
    else:
        msg = transformR(msg, - transindex[0])
    return msg

def methodDD(transindex, msg):
    '''
    duplicate in decryption
    :return: msg
    '''
    if len(transindex) == 1:
        if int(transindex[0] )< len(msg) - 1:
            msg = decryptD(msg, transindex[0])
        else:
            print("Please enter valid transformation.")
    else:
        if int(transindex[1]) < 0:
            print("Please enter a positive exponent!")
        else:
            msg = decryptDK(msg, transindex[0], transindex[1])
    return msg

def methodTD(transindex, msg):
    '''
    swap in decryption
    :return: msg
    '''
    if transindex[0].find(')') == -1:
        msg = transformT(msg, transindex[0], transindex[1])
    else:
        group = int(transindex[0][transindex[0].find('(') + 1:transindex[0].find(')')])
        param1 = int(transindex[0][transindex[0].find(')') + 1:])
        param2 = int(transindex[1])
        if len(msg) % group == 0:
            if param2 < group and param1 < group:
                msg = transformT1(msg, param1, param2, group)
            else:
                print("Please Enter valid index")
        else:
            print("Please enter valid group.")
    return msg

def methodJD(transindex, msg):
    '''
    method J in decryption
    :return: msg
    '''
    if transindex[0].find(')') == -1:
        msg = decryptJ(msg, transindex[0], transindex[1], 1)
    else:
        exponent = int(transindex[0][transindex[0].find('(') + 1:transindex[0].find(')')])
        param1 = int(transindex[0][transindex[0].find(')') + 1:])
        param2 = int(transindex[1])
        length = len(msg)
        if param2 < length and param1 < length:
            msg = decryptJ(msg, param1, param2, exponent)
        else:
            print("Please Enter valid index")
    return msg

def mainloop():
    '''
    Main program which handles the files and processes the transformation.
    :return:None
    '''
    msgFile=input(" Enter the Message file name: ")
    transformFile=input(" Enter the transformation file name:  ")
    #msgFile = "msg.txt"
    #transformFile = "transform.txt"
    type=int(input("1. Encrypt or 2. Decrypt ?"))
    #type = 1
    message= open(msgFile)
    transform=open(transformFile)

    for msg in message:
        for transformline in transform:
            if type==1:
                transformlist=transformline.split(";")
                for _ in range(len(transformlist)):
                    tranlist=transformlist[_]
                    numbers = (tranlist[1:])
                    transindex = numbers.split(",")
                    if tranlist[0] ==  "S" :
                        msg = methodSE(transindex, msg)
                    elif tranlist[0]=="R" :
                        msg = methodRE(transindex, msg)
                    elif tranlist[0] == "D":
                        msg = methodDE(transindex, msg)
                    elif tranlist[0] == "T":
                        msg = methodTE(transindex, msg)
                    elif tranlist[0] == "J":
                        msg = methodJE(transindex, msg)
            elif type==2:
                transformlist = transformline.split(";")
                #reverse the transform list first
                transformlist=reorder(transformlist)
                for _ in range(len(transformlist)):
                    tranlist = transformlist[_]
                    numbers = (tranlist[1:])
                    transindex = numbers.split(",")
                    if tranlist[0] == "S":
                        msg = methodSD(transindex, msg)
                    elif tranlist[0] == "R":
                        msg = methodRD(transindex, msg)
                    elif tranlist[0] == "D":
                        msg = methodDD(transindex, msg)
                    elif tranlist[0] == "T":
                        msg = methodTD(transindex, msg)
                    elif tranlist[0] == "J":
                        msg = methodJD(transindex, msg)
    if type == 1:
        print("Encrypted message : " + msg)
    elif type == 2:
        print("Decrypted message : " + msg)
    else:
        print("Option entered is not valid.")

if __name__== '__main__' :
    mainloop()