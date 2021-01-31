class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

    def get_max(self):
        if not self.items:
            return None
        return max(self.items)

s = Stack()
s.push(1)
s.push(3)
s.push(2)
s.push(4)
s.push(5)
print(s.pop())
print(s.peek())
print(s.get_max())
