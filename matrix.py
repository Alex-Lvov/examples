from random import randint

exit()

USE_STDIO = False

size = 5 if not USE_STDIO else int(input("Matrix size"))
matrix = [[randint(1, 10) for i in range(size)] for j in range(size)]

print(*matrix, sep="\n")

def sum_main(matrix, size):
    ret = 0
    for i in range(size):
        ret += matrix[i][i]
    return ret

def sum_add(matrix, size):
    ret = 0
    for i in range(size):
        # print(f"{[i]}{[size-i-1]} {matrix[i][size-1-i]}")
        ret += matrix[i][size-i-1]
    return ret

def sum_under_main():
    ret = 0
    for i in range(size):
        ret += matrix[i][i]
        for j in range(i, size):
            ret += matrix[i]
    return ret


print(sum_main(matrix, size))
print(sum_add(matrix, size))



