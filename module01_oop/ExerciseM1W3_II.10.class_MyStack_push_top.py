# Phần trắc nghiệm - Câu hỏi 10
class MyStack():
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def is_empty(self):
        return len(self.__stack) == 0

    def push(self, value):
        if not self.is_full():
            self.__stack.append(value)

    def top(self):
        if not self.is_empty():
            return self.__stack[-1]

stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print(stack1.top())

# Đáp án là b) 2