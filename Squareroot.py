import math
sqrtqm = int(input("Welche Zahl soll ich prüfen?"))
if math.sqrt(sqrtqm) % 1 == 0: print('Ja, das ist eine Quadratzahl (Wurzel:',math.sqrt(sqrtqm),")")
else: print('Nein, das ist keine Quadratzahl (Wurzel:',math.sqrt(sqrtqm),")")
input()
