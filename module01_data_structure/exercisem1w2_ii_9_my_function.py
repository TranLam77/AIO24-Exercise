# -*- coding: utf-8 -*-
"""ExerciseM1W2_II.9.my_function.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wun7H28Erq93Q7SMfEUcXi-kUmA0tR6m
"""

#Cau hoi trac nghiem - Cau hoi 9
def my_function(n):
    # Your code here
    return max(n)

my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001

my_list = [1, 9, 9, 0]
print(my_function(my_list))

# Đáp án là c) -1