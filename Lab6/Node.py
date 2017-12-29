class LinkedNode:
    __slots__ = "value","link"

    def __init__(self,value,link=None):
        self.value = value
        self.link = link

    def __str__(self):
        return self.value

def size_to_end(node):
    if node==None:
        return 0
    else:
        return 1+size_to_end(node.link)
