class Stack:
    def __init__(self):
        self.stack=[];
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if(self.stack == 0):
            return "Stack empty"
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def display(self):
        print(self.stack)
        
s = Stack()

s.push("hasnain")
s.push("john")
s.push("tim")

s.display()

print("Top removed ", s.pop() , "\n")

print("Peek Element ", s.peek())

dict_stack  = {
    "Name": "hasnain",
    "Age": 56
}

dict_stack