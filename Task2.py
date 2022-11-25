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

class Stack:
    def __init__(self):
        self.head = None

    def showItems(self):
        next_n = self.head
        while next_n:
            print(next_n.getData())
            next_n = next_n.getNext()

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def push(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp


    def peek(self):
        next_n = self.head
        while next_n is not None:
            if next_n.getNext() == None:
                return next_n.getData()
            next_n = next_n.getNext()


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


stack = Stack()
stack.push(2)
stack.push(5)
stack.push(3)
stack.push(7)
stack.showItems()
# print(stack.isEmpty())
# print(stack.peek())
# print(stack.size())
print(stack.pop(2))
stack.showItems()