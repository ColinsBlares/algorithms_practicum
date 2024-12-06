import math
import time


def fib(n):
    if n < 1 or n > 64:
        raise ValueError("n должно быть в пределах 1 ≤ n ≤ 64")

    # const
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2

    fib_n = (phi ** n - psi ** n) / sqrt_5
    return round(fib_n)


n = 32
start = time.perf_counter()
result = fib(n)
end = time.perf_counter()

print(f"fib(n) = {fib(n)} \n Таймер {end - start:.6f} c.")
