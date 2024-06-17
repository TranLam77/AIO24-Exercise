import numpy
import math

def isnumber(s):
    try:
        float(s)
    except ValueError:
        return False
    return True

def giai_thua(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def approx_sin(x,n):
    result = 0
    for i in range(n):
        result += (-1)**i*x**(2*i+1)/giai_thua(2*i+1)
    return result

def approx_cos(x,n):
    result = 0
    for i in range(n):
        result += (-1)**i*x**(2*i)/giai_thua(2*i)
    return result

def approx_sinh(x,n):
    result = 0
    for i in range(n):
        result += x**(2*i+1)/giai_thua(2*i+1)
    return result

def approx_cosh(x,n):
    result = 0
    for i in range(n):
        result += x**(2*i)/giai_thua(2*i)
    return result

def approximate_04_functions():
    x = input ("Nhập số muốn tính toán (radian): ")
    if not isnumber(x):
        print("Phải nhập số")
        return

    n = input ("Nhập số lần lặp muốn xấp xỉ: ")
    if not n.isnumeric():
      print("Phải nhập số int")
      return

    x = float(x)
    n = int(n)

    print(f"approx_sin(x={x}, n={n}) >> {approx_sin(x,n+1)}")
    print(f"approx_cos(x={x}, n={n}) >> {approx_cos(x,n+1)}")
    print(f"approx_sinh(x={x}, n={n}) >> {approx_sinh(x,n+1)}")
    print(f"approx_cosh(x={x}, n={n}) >> {approx_cosh(x,n+1)}")

approximate_04_functions()