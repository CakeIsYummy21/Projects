import math
try:
    file = open("FoundPrimes.txt", "r")
    primes = list(eval(file.read()))
except FileNotFoundError:
    file = open("FoundPrimes.txt", "w")
    file.write("3,5")
    primes=[3,5]
except: exit()
file.close()
del file
obnu=int(primes[-1])
print('Primes are found. Previously found primes: ', len(primes), '. The search starts at: ', obnu,".",sep="")
fndndndx=int(math.sqrt(obnu))
while True:
    try:endindx=primes.index(fndndndx)+1
    except:fndndndx+=1
    else:break
del fndndndx
file = open("FoundPrimes.txt", "a")
while True:
    obnu+=2
    if primes[endindx]**2<=obnu:endindx+=1
    for tstindx in range(0,endindx):
        if obnu % primes[tstindx]==0:break
    else: 
        primes.append(obnu)
        file.write(","+str(obnu))