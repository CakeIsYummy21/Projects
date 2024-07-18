obnu=int(1)
primes = [2]
print("Die 1. Primzahl ist 2.")
while True:
    obnu=obnu+2
    for test in primes:
        if obnu % test== 0:
            break
    else:
        primes.append(obnu)
        print("Die ",len(primes),". Primzahl ist ",obnu, ".", end=("\n"),sep="")