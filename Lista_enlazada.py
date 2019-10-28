class Nodo:
    def __init__(self,value,siguiente = None):
        self.data = value
        self.next = siguiente

#ADT Linked_List

class Linked_List:
    def __init__ (self):
        self.head = None


    def is_empty (self):
        return self.head == None

    def get_tail (self):
        cur_node = self.head
        while cur_node.next!= None:
            cur_node = cur_node.next
        return cur_node

    def append (self,value):
        if self.is_empty():
            self.head = Nodo(value)
        else:
            self.get_tail().next = Nodo(value)
      

    def prepend (self,value):
        self.head = Nodo (value, self.head)
       

    def add_before (self,ref_value,value):
        if ref_value == self.head.data:
            new_node = Nodo(value)
            new_node.next = self.head
            self.head = new_node
            return

        cur_node = self.head
        while cur_node != None:
            if cur_node.data == ref_value:
                break
            cur_node = cur_node.next
        if cur_node is None:
            self.append(value)
        else:
            new_node = Nodo(value)
            new_node.next = cur_node.next
            cur_node.next = new_node
        
        
    def add_after (self,ref_value,value):
        cur_node= self.head
        while cur_node != None:
            if cur_node.data == ref_value:
                break
            cur_node = cur_node.next
        if cur_node is None:
            self.append(value)
        else:
            new_node = Nodo(value)
            new_node.next = cur_node.next
            cur_node.next = new_node
    
    def remove (self,value):
        cur_node = self.head
        prev = None
        while cur_node and cur_node.data != value:
            prev = cur_node
            cur_node = cur_node.next
        if prev is None:
            self.head = cur_node.next
        elif cur_node:
            prev.next = cur_node.next
            cur_node.next = None


    def transversal (self):
        cur_node = self.head
        while cur_node.next!= None:
            print(cur_node.data,"->",end=" ")
            cur_node = cur_node.next
        print(cur_node.data)
