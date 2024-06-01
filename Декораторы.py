from cprint import cprint


def is_prime(func): #decorator

    def wrapper(*args):
        devided_by = []
        sum_ = sum(args)

        result = func(*args)

        for i in range(1, sum_ + 1):
            if float((sum_ / i)) == int((sum_ / i)):
                devided_by.append(i)
        if len(devided_by) == 2 and (1 in devided_by):
            print("Простое")
        else:
            print ("Составное")
        return result
    return wrapper


@is_prime
def sum_three(*args):
    if len(args) != 3:
        cprint.err("Make sure you have only 3 params!")
        exit()
    return sum(args)



result = sum_three(2, 3, 6)
print(result)
