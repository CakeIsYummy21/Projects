import random
import time
print("Hello.")
time.sleep(1)
print("Today we're doing a luck test.")
time.sleep(2)
print("We will define the range in which your number is to be searched, e.g. from 1 to 100.")
time.sleep(3.5)
f = input("From?")
t = input("To?")
a = input("Which number(from "+f+"-"+t+")?")
f = int(f)
t = int(t)
x = 1.010102220213
b = int(0)
a = int(a)
while a != x:
    x = random.randint(f, t)
    b = int(b+1)
    print(b, round((t-(f-1))/b, 5), x)
print(x)
print("it took ",b," attempts. Your luck rate:",(t-(f-1))/b)
time.sleep(1000)
