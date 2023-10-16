
def fibonacci(n):
    f0 = 0
    f1 = 1
    while f0 <= n:
        print(f0)
        f = f1 + f0
        f0 = f1
        f1 = f

