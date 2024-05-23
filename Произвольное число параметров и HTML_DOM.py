

def test(a, *args,  str_ = "Wow", **dict):
    print(a, str_, args, dict)

test("dsf", 2, 3 ,4,  str_ = "Smiling face emoji", fgf= "run", g = "fly")


def compute_factorial(n):

    if n == 1:
        return n

    else:
        return n * compute_factorial(n - 1)

r = compute_factorial(5)
print(r)

