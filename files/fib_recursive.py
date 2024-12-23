import sys
import time


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


n = int(sys.argv[1])
start = time.perf_counter()
result = fib(n)
end = time.perf_counter()

print(f"fib(n) = {result} \nTime: {end - start:.6f} c.")

