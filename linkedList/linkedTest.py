from linkedListFullClass import linkedListNode, linkedList

def insert_after_value (self, data_after, data_to_insert):
    node = linkedListNode(self, data_after, data_to_insert)
    if data_after < 0 or data_after > linkedList.get_length():
        raise Exception ("Invalid parameter")
    
    if data_after == 0:
        linkedList.insert_at_begining(data_to_insert)
        return
    
    count = 0
    currentNode = self.head
    while currentNode:
        if currentNode == data_after:
            currentNode.nextNode = data_to_insert
            break
        currentNode = currentNode.nextNode


ll = linkedList()
ll.insert_values(["banana", "mango", "grapes", "orange", "tangerine"])
ll.printLinkedList()
ll.
    