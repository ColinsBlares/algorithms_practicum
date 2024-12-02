import time


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


n = 30
start = time.time()
result = fib(n)
end = time.time()

print(f"fib(n) = {result} \n Таймер: {end - start:.6f} с.")

