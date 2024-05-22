


def calculate(num = None):

    if num is None:
        num = int(input("Enter a Number, Great Adventurer: "))

    if not 3 <= num <= 20:
        return "Death", num

    answer = []
    probable_numbers = []
    for i in range(num):
        for j in range(num):
            probable_numbers.append([str(i), str(j)])
            if  i + j <= num and i != 0 and [str(i), str(j)][::-1] not in probable_numbers and num % (i+j) == 0 :
                answer.append(str(str(i) + str(j)))
    return "".join(answer), num


result = calculate() # You can either put in a parameter yourself or enter it in the terminal
print(f"Possible codes for number {result[1]}:", result[0])


