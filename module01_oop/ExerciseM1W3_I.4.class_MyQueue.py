# class MyQueue
class MyQueue:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    def is_empty(self):
        return True if len(self.items) == 0 else False

    def is_full(self):
        return True if len(self.items) == self.capacity else False

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def enqueue(self, item):
        if self.is_full():
            return None
        self.items.append(item)
        return self.items

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

# test MyQueue
queue1 = MyQueue(5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
print(queue1.items)