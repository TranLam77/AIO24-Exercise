import math
import numpy

def calculate_regression_loss_functions():
    #input number of samples
    num_samples = input('Input number of samples (integer number) which are generated: ')
    #check if number of samples is an integer number
    if num_samples.isnumeric() == False:
        print('number of samples must be an integer number')
        return
    #input loss name
    loss_name = input('Input loss name (MAE|MSE|RMSE): ')
    #check if loss name is supported
    if loss_name != 'MSE' and loss_name != 'MAE' and loss_name != 'RMSE':
        print('loss name is not supported! Please input MAE|MSE|RMSE')
        return
    #loop to calculate loss
    final = 0
    for sample in range(int(num_samples)):
        target = numpy.random.uniform(0,10)
        predict = numpy.random.uniform(0,10)

        if loss_name == 'MAE':
            loss = abs(target - predict)
        elif loss_name == 'MSE':
            loss = (target - predict)**2
        elif loss_name == 'RMSE':
            loss = (target - predict)**2

        print(f"loss name: {loss_name}, sample: {sample}, pred: {predict}, target: {target}, loss: {loss}")
        final += loss

    if loss_name == 'MAE' or loss_name == 'MSE':
        final = final/int(num_samples)
    else:
        final = math.sqrt(final/int(num_samples))

    print(f'final loss ({loss_name}) = {final}')

calculate_regression_loss_functions()