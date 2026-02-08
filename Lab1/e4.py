def sum_1(n):
    if n == 1:
        return 1
    return 1/(n*n) + sum_1(n-1)

def sum_2(n,m):
    if m == 1:
        return 1
    return m**n + sum_2(n,m-1)

def select_operation(n):
    if n == 1:
        return sum_1
    if n == 2:
        return sum_2

print(select_operation(1))
print(select_operation(2))