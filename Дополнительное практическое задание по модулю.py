


def calculate(num):
    answer = []
    probable_numbers = []
    for i in range(num):
        for j in range(num):
            probable_numbers.append([str(i), str(j)])
            if  i + j <= num and i != 0 and [str(i), str(j)][::-1] not in probable_numbers and num % (i+j) == 0 :
                answer.append(str(str(i) + str(j)))
    return "".join(answer), num


print(f"Possible codes for number {calculate(20)[1]} are:", calculate(20)[0])


