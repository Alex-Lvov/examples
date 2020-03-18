u = [4 ** i for i in range(1, 15)]
print(*u, sep=" ")
u = [2 ** i for i in range(1, 15)]
# u = [i for i in range(4,40)]
# u = [4**i for i in range(1,15)]

print(*u, sep=" ")

# Power of two
for n in u:
    if not 2 ** n % n:
        print(n)

# Power of four
for n in u:
    if not n / (n ** (1 / 2)) % 2:
        print(n)
