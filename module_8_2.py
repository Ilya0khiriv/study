def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        try:
            result += number
        except:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {number}")

    return result, incorrect_data


def calculate_average(numbers):
    def actual_calculation(data):
        try:
            total, garbage, elements = data
        except:
            print("В numbers записан некорректный тип данных")
            return

        actual_elements = elements - garbage
        try:
            average = total / actual_elements
        except:
            average = 0
        return average

    def resolve_data_type(numbers):
        if isinstance(numbers, str):
            numbers = tuple(numbers)

        if isinstance(numbers, (list, tuple, set)):
            total, garbage = personal_sum(numbers)
            return total, garbage, len(numbers)

    return actual_calculation(resolve_data_type(numbers))


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
