

# # ================= Singly Linked List ==================

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class SinglyLinkedList:
    
#     def __init__(self):
#         self.head = None
        
#     def display(self):
#         temp = self.head
#         result = []
#         while temp :
#             result.append(temp.data)
#             temp = temp.next
        
#         print("Linked List ---> ", result)
        
#     def insert(self,data):
#         new_node = Node(data)
        
#         if not self.head:
#             self.head = new_node
#             return

#         temp = self.head
        
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node
    
    
#     def delete(self,key):
#         temp = self.head
        
#         if temp and temp.data == key:
#             self.head = temp.next
#             temp = None
#             return
        
#         prev = None
        
#         while temp and temp.data != key:
#             prev = temp
#             temp = temp.next
            
#         if temp is None:
#             return
        
#         prev.next = temp.next
#         temp = None
    
    
    
# #  === Object Creation ===
# LiLs = SinglyLinkedList()

# # ==== object call ====
# LiLs.display()

# #  ==== Insert elements in linked list ===
# LiLs.insert(6)
# LiLs.insert(10)
# LiLs.insert(99)
# LiLs.insert(2)
# LiLs.insert(3)
# LiLs.insert(6)
# LiLs.insert(7)
# LiLs.insert(10)
# LiLs.insert(10)

# LiLs.display()
# LiLs.delete(10)
# LiLs.delete(99)
# LiLs.delete(999)
# LiLs.display()


        
        


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print("Linked List --> ",result)
        
    def insert(self,data):
        new_data = Node(data)
        if not self.head:
            self.head = new_data
            return
        temp = self.head
        
        while temp.next:
            temp = temp.next
        temp.next = new_data
        
        
Lil  = SinglyLinkedList()
Lil.display()
Lil.insert(0)
Lil.insert(1)
Lil.insert(2)
Lil.insert(3)
Lil.display()
    