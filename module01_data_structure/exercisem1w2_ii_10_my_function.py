# -*- coding: utf-8 -*-
"""ExerciseM1W2_II.10.my_function.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kHLfY4xRBa9h0Q0B-HCG4CyxMUNi6Etg
"""

#Cau hoi trac nghiem - Cau hoi 10
def my_function (integers, number = 1) :
    #return any(# Your code here : Thuc hien duyet tung phan tu trong integers , so sanh tung phan tu voi number , neu bang nhau tra ve True , khac nhau tra ve false
    #vi du: integers = [1 , 2 , 3] , number = 2 , ban se tao ra list [False , True , False ] )
    return any([True if x == number else False for x in integers])

my_list = [1, 3, 9, 4]
assert my_function(my_list, -1) == False

my_list = [1 , 2 , 3 , 4]
print(my_function(my_list, 2) )

# Đáp án là a) 1.0