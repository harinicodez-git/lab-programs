def int_sqrt(n):
    i = 0
    while i * i <= n:
        i += 1
    return i - 1

print(int_sqrt(20))