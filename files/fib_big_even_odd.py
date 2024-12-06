import sys
import time


def fib_eo(n):
    if n < 1 or n > 10 ** 6:
        raise ValueError("n должно быть в пределах 1 ≤ n ≤ 10⁶")

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10
    return "even" if b % 2 == 0 else "odd"


n = int(sys.argv[1])
start = time.perf_counter()
result = fib_eo(n)
end = time.perf_counter()

print(f"fib(n) = {fib_eo(n)} \nTime {end - start:.6f} c.")

