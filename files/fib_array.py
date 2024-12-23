import sys
import time


def fib(n):
    fib_array = [0, 1]

    if n < len(fib_array):
        return fib_array[:n + 1]

    for i in range(2, n + 1):
        fib_array.append(fib_array[i - 1] + fib_array[i - 2])

    return fib_array


n = int(sys.argv[1])
start = time.perf_counter()
result = fib(n)
end = time.perf_counter()

print(f"fib(n) = {fib(n)} \nTime {end - start:.6f} c.")
