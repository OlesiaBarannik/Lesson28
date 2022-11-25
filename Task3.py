class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class Queue:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)  # Node("Dog")
        temp.setNext(self.head)  # Node("Dog") -> Node("Head") = None
        self.head = temp

    def showItems(self):
        next_n = self.head
        while next_n:
            print(next_n.getData())
            next_n = next_n.getNext()

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def insert(self, index, item):
        new_n = Node(item)
        prev_n = None
        next_n = self.head
        n = 0
        while next_n:
            if n == index:
                break
            prev_n = next_n
            next_n = next_n.getNext()
            n += 1
        if prev_n == None:
            self.add(item)
        else:
            prev_n.setNext(new_n)
            new_n.setNext(next_n)

    def enqueue(self, item):
        self.insert(self.size(),item)

    def size(self):
        n = 0
        next_n = self.head
        while next_n is not None:
            n += 1
            next_n = next_n.getNext()
        return n


    def pop(self, i = None):
        last_n = self.head
        prev_n = None
        n = 0
        while last_n.getNext() != None:
            if i == n:
                break
            prev_n = last_n
            last_n = last_n.getNext()
            n += 1

        prev_n.setNext(last_n.getNext())
        return last_n.getData()

    def dequeue(self):
        return self.pop()


queue = Queue()
queue.enqueue(10)
queue.enqueue(5)
queue.enqueue(3)
queue.enqueue(7)
queue.showItems()
queue.dequeue()
queue.showItems()
