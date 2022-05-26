class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
 
class ListaDoblementeEnlazada:
    
    def __init__(self):
        self.head = None
 
    def reverse(self):
        temp = None
        current = self.head
 
    
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
 
        
        if temp is not None:
            self.head = temp.prev
 
    
    def push(self, new_data):
 
        new_node = Node(new_data)
        new_node.next = self.head
 
        if self.head is not None:
            self.head.prev = new_node
 
        self.head = new_node
 
    def printList(self, node):
        while(node is not None):
            print(node.data,end=' ')
            node = node.next


listElementos = ListaDoblementeEnlazada()
for x in range(5):
    elemento=str(input("Ingrese el elemento: "))
    listElementos.push(elemento)


print ("\n Lista invertida")
listElementos.printList(listElementos.head)
listElementos.reverse()

print ("\n Lista original")
listElementos.printList(listElementos.head)

 

