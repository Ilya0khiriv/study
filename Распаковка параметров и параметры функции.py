


def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(1, 2, 3)
print_params(2)
# print_params(1, 2, 3, 4, 5) # слишком много аргументов
# print_params(b = 25) # не сработает, ожидается строка, а не число
# print_params(c = [1,2,3]) # не сработает, ожидается булевое значение, а не лист

values_list = [2, "string", False]

values_dict = {
    "a": 2,
    "b": "string",
    "c": False
}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, {2}]
print_params(*values_list_2, 42)