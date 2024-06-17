# *************Exercise2***********
import math


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True
# is_number('a')


def calc_sig(x):
    result = 1/(1+math.e**(-x))
    return result
# calc_sig(2)


def calc_relu(x):
    if x < 0:
        result = 0
    else:
        result = x
    return result
# calc_relu(2)


def calc_elu(x):
    alpha = 0.01
    if x < 0:
        result = alpha*(math.e**x-1)
    else:
        result = x
    return result
# calc_elu(-4)


def calc_activation_func(x, act_name):
    result = None
    if act_name == "sigmoid":
        result = calc_sig(x)
    elif act_name == "relu":
        result = calc_relu(x)
    elif act_name == "elu":
        result = calc_elu(x)
    return result
# calc_activation_func(-2,"relu")


def exercise2():
    x = input('Input x =')

    if is_number(x) == False:
        print('x must be a number')
        return

    act_name_list = ["sigoid", "relu", "elu"]
    act_name = input('activation function name: ')

    # Check if the string is in the list of activation function name

    if act_name in act_name_list:
        x = float(x)
        result = calc_activation_func(x, act_name)
        print(f"{act_name}({x}) = {result}")
    else:
        print(f"'{act_name}' is not supported")


# Check the Result of Excercise 2
exercise2()
