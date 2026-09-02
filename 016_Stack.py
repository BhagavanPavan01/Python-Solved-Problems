

# =====================Stack============================


class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,element):
        self.stack.append(element)
        print(f"element {element} is added/pushed in the stack")
        
    def peak(self):
        
        if not self.is_empty():
            print(f"Peak element is {self.stack[-1]}")
        
    def is_empty(self):
        return len(self.stack) == 0


    def pop(self):
        last_el = self.stack.pop()
        print(f"the element {last_el} is remove from stack")

s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.peak()
s.pop()
s.peak()