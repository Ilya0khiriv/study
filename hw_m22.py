


first = 2
second = 22
third = 23
numbers = (first, second, third)

same = 0


if (first == second) and (first == third) and (third == second):
    same -= 3
    print(0)

elif (first != second) and (first != third) and (third == second):
    print(1)
    same -= 2

elif (first != second) and (first == third) and (third != second):
    print(2)
    same -= 2

elif (first == second) and (first != third) and (third != second):
    print(3)
    same -= 2
else:
    same = 0

print(same)



# old task
# x = 38
# print('дратути!')
# if x < 0:
#     print("Меньшенуля")
#     print("датвидания!")


# a, b = 10, 5
# if a > b:
#     print('a > b')
# if a > b and a > 0:
#     print ('успех')
# if (a > b) and (a > 0 or b < 1000):
#     print ('ycnex')
# if 5 > b and b < 10:
#     print("успех")

# if '34' > '123':
#     print ('успех')
# if '123' > '12':
#     print('успех')
# if [1, 2] > [1, 1]:
#     print ('успех')


# if '6' > 5:
#     print ('успех')
# if [5, 6] > 5:
#     print ('успех')
# if '6' != 5:
#     print ('успех')
