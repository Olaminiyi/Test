class linkedListNode: 
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

# node1 = linkedListNode("3")
# node2 = linkedListNode("7")
# node3 = linkedListNode("10")
# node4 = linkedListNode("11")

# node1.nextNode = node2
# node2.nextNode = node3
# node3.nextNode = node4

# currentNode = node1
# while True:
#     print (currentNode.value, "->", end="")
#     if currentNode.nextNode is None:
#         print ("None")
#         break
#     currentNode = currentNode.nextNode


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def insert_at_end(self, value):
        if self.head is None:
            self.head = linkedListNode(value, None)
            return
        
        currentNode = self.head
        while currentNode.nextNode:
            currentNode = currentNode.nextNode
        
        currentNode.nextNode = linkedListNode(value, None)
    
    def insert_at_begining(self, value):
        currentNode = linkedListNode(value, self.head)
        self.head = currentNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print (currentNode.value, "->", end="")
            currentNode = currentNode.nextNode
        print("None")
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        currentNode = self.head
        while currentNode:
            count += 1
            currentNode = currentNode.nextNode

        
        return count
        
    
    def remove_at(self, index):
        if index<0 or index >= self.get_length():
            raise Exception("invalid index")
        
        if index==0:
            self.head = self.head.nextNode
            return
        
        count = 0
        currentNode = self.head
        while currentNode:
            if count == index -1 :
                currentNode.nextNode = currentNode.nextNode.nextNode
                break

            currentNode = currentNode.nextNode
            count += 1




ll = linkedList()
ll.insert_values(["banan", "mango", "grapes", "orange"])
ll.printLinkedList()
print(ll.get_length())
ll.remove_at(3)
ll.printLinkedList()
# ll.insert("44")
# ll.printLinkedList()
# ll.insert("55")
# ll.printLinkedList()
# ll.insert_at_end("90")
# ll.printLinkedList()
# ll.insert_at_begining("32")
# ll.printLinkedList()

