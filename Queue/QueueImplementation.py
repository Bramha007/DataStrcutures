class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def isEmpty(self):
        if len(self.queue) > 0:
            return False
        return True

    def peek(self):
        return self.queue[0]

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)
    


