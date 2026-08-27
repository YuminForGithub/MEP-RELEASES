import sys
import time

sys.set_int_max_str_digits(100_000_000)

def fib(n):
    if n == 0:
        return 0, 1

    a, b = fib(n // 2)

    c = a * (2 * b - a)
    d = a * a + b * b

    if n & 1:
        return d, c + d
    else:
        return c, d


n = int(input("n-th Fibonacci to find? "))

start = time.perf_counter()

result = fib(n)[0]

calc_end = time.perf_counter()

lo = str(result)

convert_end = time.perf_counter()

print(f"F_{n} has {len(lo)} digits.")
print(f"Calculation: {calc_end - start:.3f} seconds")
print(f"Conversion:  {convert_end - calc_end:.3f} seconds")

with open("e.txt", "w") as file:
    file.write(lo)

write_end = time.perf_counter()

print(f"Writing:     {write_end - convert_end:.3f} seconds")
print(f"TOTAL:       {write_end - start:.3f} seconds")