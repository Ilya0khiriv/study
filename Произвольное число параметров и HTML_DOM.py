def get_multiplied_digits(number):
    number = str(number)
    digit = int(number[0])
    
    if len(number) == 1: return digit
    
    stripped_number = number[1:]
    
    return digit * get_multiplied_digits(stripped_number)


print(get_multiplied_digits(2222))


# def test(a, *args,  str_ = "Wow", **dict):
#     print(a, str_, args, dict)

# test("dsf", 2, 3 ,4,  str_ = "Smiling face emoji", fgf= "run", g = "fly")


# def compute_factorial(n):

#     if n == 1:
#         return n

#     else:
#         return n * compute_factorial(n - 1)

# r = compute_factorial(5)
# print(r)

