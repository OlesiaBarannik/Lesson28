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

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item) # Node("Dog")
        temp.setNext(self.head) # Node("Dog") -> Node("Head") = None
        self.head = temp # Node("cat) -> Node("Dog") -> None


    def append1(self,item):
       self.add(item)

    def append(self, item):
        temp = Node(item)
        last_n = self.head
        while last_n.getNext() != None:
            last_n = last_n.getNext()
        last_n.setNext(temp)

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

        return last_n


    def index(self, item):
        next_n = self.head
        n = 0
        while next_n:
            if next_n.getData() == item:
                return n
            next_n = next_n.getNext()
            n += 1
        return None


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


    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while current.next is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())



    def __repr__(self):
        next_n = self.head
        res = ""
        while next_n:
            res += str(next_n.getData()) + " -> "
            next_n = next_n.getNext()
        return res




    def slice(self, start, stop):
        data = []
        copy_list = UnorderedList()
        next_n = self.head
        i = 1
        while next_n:
            if i >= start and i < stop:
                data.insert(0,next_n.getData())
            next_n = next_n.getNext()
            i += 1
        for v in data:
            copy_list.add(v)
        return copy_list





mylist = UnorderedList()
mylist.add(53)
mylist.add(28)
mylist.add(40) #3
mylist.add(719)
mylist.add(153)
mylist.add(228)
mylist.add(340)
mylist.add(779)
mylist.add(3) #9
mylist.add(8)
mylist.add(45)
mylist.add(789)
# mylist.append(1)

# print(mylist.index(799))
print(mylist)
# print(mylist.slice(3, 10))
# # mylist.insert(0,15300)
# mylist.pop(3)
# print(mylist)
