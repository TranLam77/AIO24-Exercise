# class MyStack
class MyStack:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    def is_empty(self):
        return True if len(self.items) == 0 else False

    def is_full(self):
        return True if len(self.items) == self.capacity else False

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(-1)

    def push(self, item):
        if self.is_full():
            return None
        self.items.append(item)
        return self.items

    def top(self):
        if self.is_empty():
            return None
        return self.items[-1]

# test MyStack
stack1 = MyStack(5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
print(stack1.items)