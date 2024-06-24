# Phần trắc nghiệm - Câu hỏi 12
class MyQueue():
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if not self.is_full():
            self.__queue.append(value)

    def front(self):
        return self.__queue[0]

queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.front())

# Đáp án là d) 1