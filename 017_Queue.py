

#  ============================== Queue ==================

class  Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self,val):
        self.queue.append(val)
        print(f"{val} is added to the queue")
        
    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)
            print(f"{removed} is removed form queue")
        else:
            print("Queue is Empty")
        
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def display(self):
        if not self.is_empty():
            print(self.queue)
            
    def front(self):
        if not self.is_empty():
            print(f"first element is {self.queue[0]}")
        else:
            print("Queue is empty")
            
            

obj = Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
obj.enqueue(50)
obj.display()
obj.front()
obj.dequeue()

obj.display()


