# import Person
from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, e):
        newNode = Node(e)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            current_last = self.tail
            current_last.setNext(newNode)
            newNode.setPrevious(current_last)
            self.tail = newNode
        self.size = self.size + 1

    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head
        # don't do this
        # while (current != None)
        # while (current)
        while (current is not None):
        # like saying while (not(current is None))    
            stringToReturn = stringToReturn + "\n\n" + str(current)
            current = current.getNext()
        return(stringToReturn)

    def bubble_once(self):
        if self.size == 0:
            return

        currentNode = self.head
        nextNode = self.head.getNext();

        while (nextNode is not None):
            if currentNode.getData() > nextNode.getData():
                tempData = nextNode.getData()
                nextNode.setData(currentNode.getData())
                currentNode.setData(tempData)
            currentNode = currentNode.getNext()
            nextNode = nextNode.getNext()
    
    def bubble(self):
        if self.size == 0:
            return

        sorted = False
        while sorted is False:
            lastValue = self.head.getData()
            currentNode = self.head.getNext()
            while currentNode is not None:
                if lastValue <= currentNode.getData():
                    lastValue = currentNode.getData()
                    currentNode = currentNode.getNext()
                else:
                    lastValue = self.head.getData()
                    currentNode = self.head.getNext()
                    self.bubble_once()
            sorted = True


if __name__ == "__main__":
    newList = LinkedList()
    newList.add(4)
    newList.add(16)
    newList.add(75)
    newList.add(80)
    print(newList)
    newList.bubble()
    print(newList)
