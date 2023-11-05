# import Person
from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __getitem__(self, pos):
        currNode = self.head

        if pos > self.size or pos < 0: 
            print("Invalid index to fetch item for")
            return

        for i in range(0, pos):
            currNode = currNode.getNext()
        
        return currNode.getData()

    def add(self, obj):
        newNode = Node(obj)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            current_last = self.tail
            current_last.setNext(newNode)
            newNode.setPrevious(current_last)
            self.tail = newNode
        self.size = self.size + 1

    def insert(self, pos, obj):
        newNode = Node(obj)

        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        elif pos >= self.size:
            self.add(obj)
        elif pos < 0:
            print("Invalid index to insert at")
            return
        else:
            currIndex = 0
            currNode = self.head

            if pos == 0:
                self.head = newNode
                newNode.setNext(currNode)
                currNode.setPrevious(newNode)
            else:
                while((currNode is not None) and (currIndex != pos - 1)):
                    currNode = currNode.getNext()
                    currIndex += 1

                nextNode = currNode.getNext()

                # Set prev relative to new
                currNode.setNext(newNode)
                newNode.setPrevious(currNode)

                # Set next relative to new
                nextNode.setPrevious(newNode)
                newNode.setNext(nextNode)
        self.size += 1

    def delete(self, pos):
        currIndex = 0
        currNode = self.head

        if pos >= self.size or pos < 0 or self.size == 0:
            return

        if pos == 0:
            newFirstNode = self.head.getNext()
            newFirstNode.setPrevious(None)
            self.head = newFirstNode
        elif pos == self.size - 1:
            newLastNode = self.tail.getPrevious()
            newLastNode.setNext(None)
            self.tail = newLastNode
        else:
            while((currNode is not None) and (currIndex != pos - 1)):
                currNode = currNode.getNext()
                currIndex += 1

            newNextNode = currNode.getNext().getNext()
            currNode.setNext(newNextNode)
            newNextNode.setPrevious(currNode)

        self.size -= 1

    def length(self):
        return self.size

    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head
        while (current is not None):
            stringToReturn = stringToReturn + "\n\n" + str(current)
            current = current.getNext()
        return stringToReturn

