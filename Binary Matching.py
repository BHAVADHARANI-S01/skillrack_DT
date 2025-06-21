x, n = map(int, input().split())
numbers = list(map(int, input().split()))  # corrected the variable name
b_x = bin(x)[2:]
c = 0
for num in numbers:
    b_n = bin(num)[2:]
    if b_x[-len(b_n):] == b_n:
        c += 1
print(c)
