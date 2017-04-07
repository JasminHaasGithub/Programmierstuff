summe = 0

n = 1
m = 1

#while n < 4000000:
while m < 4000000:
    n = n + m
    m = n + m
    if n % 2 == 0:
        summe = summe + n
    if m % 2 == 0:
        summe = summe + m
   # print(n)
        
print(summe)            
