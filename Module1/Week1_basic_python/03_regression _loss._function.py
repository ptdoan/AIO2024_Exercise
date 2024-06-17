# *************Exercise3 ***********
import random
import math


def calc_ae(y, y_hat):
    result = abs(y-y_hat)
    return result


def calc_se(y, y_hat):
    result = (y-y_hat)**2
    return result


def mean(n):
    mean = 0
    # Loop from 0 to N-1
    for i in range(n):
        mean += i
    mean /= n
    return mean


def exercise3():
    num_samples = input('Input num_samples =')

    if num_samples.isnumeric():
        num_samples = int(num_samples)
    else:
        print('number of samples must be an integer number')
        return

    loss_name_list = ["MAE", "MSE", "RMSE"]
    loss_name = input('Input loss name: ')

    if loss_name not in loss_name_list:
        print(f"'{loss_name}' is not supported")
        return

    final_loss = 0
    for i in range(num_samples):
        sample = i
        pred_sample = random.uniform(0, 10)
        target_sample = random.uniform(0, 10)

        if loss_name == "MAE":
            loss = calc_ae(sample, target_sample)
        elif loss_name == "MSE" or loss_name == "RMSE":
            loss = calc_se(sample, target_sample)

        final_loss += loss
        print(f"loss_name: {loss_name}, sample: {sample}: pred: {pred_sample} \
    target: {target_sample} loss: {loss}")

    final_loss /= num_samples
    if loss_name == "RMSE":
        final_loss = math.sqrt(final_loss)

    print(f"final_loss: {final_loss}")


# Check the Result of Excercise 3
exercise3()
