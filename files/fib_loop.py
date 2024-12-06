import sys
import time


def fib(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


n = int(sys.argv[1])
start = time.perf_counter()
result = fib(n)
end = time.perf_counter()

print(f"fib(n) = {result} \nTime {end - start:.6f} c.")
