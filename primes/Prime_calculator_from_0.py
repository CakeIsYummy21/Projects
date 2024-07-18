obnu=int(1)
primes=[3]
print("2", end=";")
while True:
    obnu=obnu+4
    for test in primes:
        if obnu % test==0:
            break
    else:
        primes.append(obnu)
        print(obnu, end=(";"))
    obnu=obnu+2
    for test in primes:
        if obnu % test==0:
            break
    else:
        primes.append(obnu)
        print(obnu, end=(";"))
