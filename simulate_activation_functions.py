import math

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def simulate_activation_functions():
    alpha = 0.01
    #input x
    x = input('Input x = ')
    #check if x is a number
    if not is_number(x):
        print('x must be a number!')
        return
    #convert to float
    x = float(x)
    #input activation function
    act_func = input('Input activation function (sigmoid|relu|elu): ')
    if act_func == 'sigmoid':
        print(f"sigmoid f({x}) = {1/(1+math.exp(-x))}")
    elif act_func == 'relu':
        if x > 0:
            print(f"relu f({x}) = {x}")
        else:
            print(f"relu f({x}) = 0")
    elif act_func == 'elu':
        if x > 0:
            print(f"elu f({x}) = {x}")
        else:
            print(f"elu f({x}) = {alpha*(math.exp(x)-1)}")
    else:
        print(f"{act_func} is not supported! Please input sigmoid|relu|elu")

simulate_activation_functions()