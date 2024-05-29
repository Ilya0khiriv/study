

def all_variants(string):
    length = len(string)


    for i in range(length):
        for j in range(length + 1):
            if string[i:j] != "":
                yield string[i:j]


a = all_variants("abc")
for i in a:
     print(i)