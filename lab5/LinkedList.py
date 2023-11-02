import Person

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, e):
        if self.size == 0:
            self.head = e
            self.tail = e
        else:
            current_last = self.tail
            current_last.setNext(e)
            e.setPrevious(current_last)
            self.tail = e
        self.size = self.size + 1

    def delete(self, i):
        if i < 0 or i >= self.size:
            return print("Index out of bounds")

        current = self.head
        if i == 0:  # If the element is the head
            self.head = current.getNext()
            if self.head:
                self.head.setPrevious(None)
            else:
                self.tail = None
        elif i == self.size - 1:  # If the element is the tail
            current = self.tail
            self.tail = current.getPrevious()
            if self.tail:
                self.tail.setNext(None)
            else:
                self.head = None
        else: # otherwise just change previous/next of the surrounding elements
            counter = 0
            while current is not None and counter != i:
                current = current.getNext()
                counter += 1
            prev_node = current.getPrevious()
            next_node = current.getNext()
            if prev_node:
                prev_node.setNext(next_node)
            if next_node:
                next_node.setPrevious(prev_node)

        self.size -= 1


    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head
        while (current is not None):
            stringToReturn = stringToReturn + "\n\n" + str(current)
            current = current.getNext()
        return(stringToReturn)

if __name__ == "__main__":
    listOfPeople = LinkedList()
    listOfPeople.add(Person.Person("Jaime", "Amherst"))
    listOfPeople.add(Person.Person("Maria", "Stow"))
    listOfPeople.add(Person.Person("Maria", "Malden"))
    print(listOfPeople)
    listOfPeople.delete(2) # Should delete Maria Malden
    print(listOfPeople)
    listOfPeople.add(Person.Person("Robert", "New York"))
    listOfPeople.delete(0) # Should delete Jaime Amherst
    print(listOfPeople)
    listOfPeople.delete(1) # Should delete Robert New York
    print(listOfPeople)
    listOfPeople.delete(0) # Deletes the last element
    print(listOfPeople)

