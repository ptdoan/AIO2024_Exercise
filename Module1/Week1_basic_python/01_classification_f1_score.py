# *************Exercise1***********

# Make the function for Excercise1
def calc_f1_score(tp, fb, fn):
    check1 = isinstance(tp, int)
    check2 = isinstance(fb, int)
    check3 = isinstance(fn, int)
    check4 = (tp > 0) and (fb > 0) and (fn > 0)

    if check1 == False:
        print('tp must be in interger')
    elif check2 == False:
        print('fb must be in interger')
    elif check3 == False:
        print('fn must be in interger')
    elif check4 == False:
        print('tp and fb and fn must be greater than zero')
    else:
        precision = tp/(tp+fb)
        recall = tp/(tp+fn)
        f1_score = 2*precision*recall/(precision+recall)
        print('precision = ', precision)
        print('recall    = ', recall)
        print('f1_score  = ', f1_score)
    return f1_score


# Check the Result of Excercise 1
calc_f1_score(2, 7, 3)
