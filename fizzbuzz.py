anzahl = int(input("Bitte gib die Lönge ein."))
for n in range(1,anzahl+1):
    if n % 3 == 0 or n % 5 == 0:
        if n % 3 == 0 and n % 5 == 0:
            print("Buzz")
        else:
            print("Fizz")
    else:
        print(n)

