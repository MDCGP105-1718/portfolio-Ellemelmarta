#fibbonacci sequence is x = (x-1 + x-2)

def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

for n in range(21):
    print (fib(n))
