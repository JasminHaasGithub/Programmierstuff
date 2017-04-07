for i in range(1,10001):
    while i > 1:
        if i % 2 == 0:
            i = i/2
        else:
            i = 3*i + 1

print(i)
