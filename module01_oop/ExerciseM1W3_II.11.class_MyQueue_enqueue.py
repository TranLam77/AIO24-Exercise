# Phần trắc nghiệm - Câu hỏi 11
class MyQueue():
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if not self.is_full():
            self.__queue.append(value)

queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.is_full())

# Đáp án là a) False