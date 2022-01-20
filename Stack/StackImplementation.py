class Stack:
    def __init__(self, value=[]):
        self.value = value

    def isEmpty(self):
        if not self.value:
            return "Stack is Empty"

    def push(self, value):
        self.value.append(value)

    def pop(self):
        return self.value.pop()

    def peek(self):
        return self.value[-1]

    def print(self):
        for val in self.value:
            print(val, end=" ")


newStack = Stack()
print(f"Checking if the stack is empty : {newStack.isEmpty()}")
print("Pushing new values in the stack")
newStack.push(5)
newStack.push(-18)
newStack.push(75)
print(f"\nPrinting stack :{newStack.print()}")
print(f"Peeking in the stack : {newStack.peek()}")
print(f"Popping values from the stack : {newStack.pop()}")
print(f"Popping values from the stack : {newStack.pop()}")
print(f"Popping values from the stack : {newStack.pop()}")
print(f"Checking if the stack is empty : {newStack.isEmpty()}")
