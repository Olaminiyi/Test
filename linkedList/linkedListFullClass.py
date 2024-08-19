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

    def insert_at(self, index, value):
        if index<0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_begining(value)
            return
        
        count = 0
        currentNode = self.head
        while currentNode:
            if count == index - 1:
                node = linkedListNode(value, currentNode.nextNode)
                currentNode.nextNode = node
                break

            currentNode = currentNode.nextNode
            count += 1
        
    def insert_after_value (self, data_after, data_to_insert):
        
        currentNode = self.head
        while currentNode:

            if currentNode.value == data_after:
                newNode = linkedListNode(data_to_insert)
                newNode.nextNode = currentNode.nextNode
                currentNode.nextNode = newNode
                break

            currentNode = currentNode.nextNode

        #raise ValueError(f"Value {data_after} not found in the list")  



ll = linkedList()
ll.insert_values(["banana", "mango", "grapes", "orange","tangerine"])
ll.printLinkedList()
print(ll.get_length())
ll.insert_after_value("mango","agbalumo")
ll.printLinkedList()

# ll.remove_at(3)
# ll.printLinkedList()
# ll.insert_at(2, "temi")
# ll.printLinkedList()
# ll.insert("55")
# ll.printLinkedList()
# ll.insert_at_end("90")
# ll.printLinkedList()
# ll.insert_at_begining("32")
# ll.printLinkedList()

