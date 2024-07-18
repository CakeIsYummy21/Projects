import math
print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
obnu=int(round(int(input("From where shall I begin?"))/2,0)*2)-1
primes = [2]
while True:
    obnu = obnu + 2
    sqrtobnu=int(math.sqrt(obnu))
    for a in range(3,sqrtobnu,2):
        if obnu % a == 0:
            break
    else:
        primes.append(obnu)
        print(obnu, end=(","))