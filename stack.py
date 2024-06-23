#LIFO Data structure
my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(33)
print(my_stack)
print(my_stack.pop())

class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
        
    def __str__(self):
        return str(self.stack)
    
l_stack = Stack()
l_stack.push(3)
l_stack.push(5)
l_stack.push(7)
#l_stack.pop()
l_stack.peek()
print(l_stack)
print(l_stack.push)
#print(l_stack.pop())
print(l_stack.peek())
