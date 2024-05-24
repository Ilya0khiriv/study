
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

collect_numbers = []
def calculate_structure_sum(data, recursive = False):
    def list_(val):
        for i in val:
            calculate_structure_sum(i, recursive = True)
    def dict_(val):
        for key in val:
            calculate_structure_sum(key, recursive = True)
            calculate_structure_sum(val[key], recursive = True)

    if type(data) is int: collect_numbers.append(data)
    elif type(data) is str: collect_numbers.append(len(data))

    elif type(data) is list: list_(data)
    elif type(data) is dict: dict_(data)
    elif type(data) is tuple or set: list_(list(data))

    if recursive is False:
        print(f"Collected numbers are {collect_numbers}, Sum is {sum(collect_numbers)}")

calculate_structure_sum(data_structure)
