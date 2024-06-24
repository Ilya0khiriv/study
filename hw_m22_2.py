numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in numbers:

    r = -1
    for j in range(i):
        if str(i/(j+1))[::-1][0:2] == "0.":
            r+=1

    if r == 1: primes.append(i)
    elif r > 1  and i != 1: not_primes.append(i)

print(primes)
print(not_primes)

