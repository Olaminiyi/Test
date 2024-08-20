class doublelinkedList:
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.nextNode = nextNode
        self.prevNode = prevNode

class linkedlist:
    def __init__(self, head=None):
        self.head = head

    def insert (self,value):
        node = doublelinkedList(value)

        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head
        while currentNode.nextNode:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def insert_at_back (self,values):
        node = doublelinkedList(values, None)
        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head
        while currentNode.nextNode:
            currentNode = currentNode.nextNode

        currentNode.nextNode = doublelinkedList(values, None)
    
    def insert_at_begining (self, value):
        node = doublelinkedList(value, self.head)
        self.head = node

    def insert_values (self,values):
        self.head = None
        for value in values:
            self.insert_at_back(value)

    def remove_by_value (self, index):
        #node = doublelinkedList(values, index)    
        if self.head.value == index:
            self.head = self.head.nextNode
        
        currentNode = self.head
        count = 0
        while currentNode:
            if currentNode.nextNode.value == index:
                
                currentNode.nextNode = currentNode.nextNode.nextNode
               
               # currentNode.nextNode = currentNode.nextNode.nextNode
                break
            currentNode = currentNode.nextNode
            





    def get_length(self):
        currentNode = self.head

        count = 0
        while currentNode is not None:
            count += 1
            currentNode = currentNode.nextNode
            
        return count
        

    def print (self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "->", end="")
            currentNode = currentNode.nextNode
        print("none")


ll = linkedlist()
ll.insert_values(["ade","yemi","tunji","femi","laide","semilore"])
ll.print()
ll.insert_at_begining("ifemi")
ll.print()
print(ll.get_length())
ll.remove_by_value("yemi")
ll.print()
