import time
import mouse
spe = 60/(50*int(input("How many wpm?")))
while True:
    text = input("What shall be typed in morse?").lower()
    mct=""
    for letter in text:
        if letter == "a":mct+=".- "
        elif letter == "b":mct+="-... "
        elif letter == "c":mct+="-.-. "
        elif letter == "d":mct+="-.. "
        elif letter == "e":mct+=". "
        elif letter == "f":mct+="..-. "
        elif letter == "g":mct+="--. "
        elif letter == "h":mct+=".... "
        elif letter == "i":mct+=".. "
        elif letter == "j":mct+=".--- "
        elif letter == "k":mct+="-.- "
        elif letter == "l":mct+=".-.. "
        elif letter == "m":mct+="-- "
        elif letter == "n":mct+="-. "
        elif letter == "o":mct+="--- "
        elif letter == "p":mct+=".--. "
        elif letter == "q":mct+="--.- "
        elif letter == "r":mct+=".-. "
        elif letter == "s":mct+="... "
        elif letter == "t":mct+="- "
        elif letter == "u":mct+="..- "
        elif letter == "v":mct+="...- "
        elif letter == "w":mct+=".-- "
        elif letter == "x":mct+="-..- "
        elif letter == "y":mct+="-.-- "
        elif letter == "z":mct+="--.. "
        elif letter == "0":mct+="----- "
        elif letter == "1":mct+=".---- "
        elif letter == "2":mct+="..--- "
        elif letter == "3":mct+="...-- "
        elif letter == "4":mct+="....- "
        elif letter == "5":mct+="..... "
        elif letter == "6":mct+="-.... "
        elif letter == "7":mct+="--... "
        elif letter == "8":mct+="---.. "
        elif letter == "9":mct+="----. "
        elif letter == ".":mct+=".-.-.- "
        elif letter == ",":mct+="--..-- "
        elif letter == ":":mct+="---... "
        elif letter == ")":mct+="-.--.- "
        elif letter == "(":mct+="-.--. "
        elif letter == "'":mct+=".----. "
        elif letter == '"':mct+=".-..-. "
        elif letter == "!":mct+="-.-.-- "
        elif letter == "/":mct+="-..-. "
        elif letter == ";":mct+="-.-.-. "
        elif letter == "=":mct+="-...- "
        elif letter == "-":mct+="-....- "
        elif letter == "_":mct+="..--.- "
        elif letter == "+":mct+=".-.-. "
        elif letter == "@":mct+=".--.-. "
        elif letter == " ":mct+="/"
        else: mct+="..--.. "
    for symbol in mct:
        if symbol==".":
            mouse.hold()
            time.sleep(spe*0.1)
            mouse.release()
            time.sleep(spe*0.1)
        elif symbol=="-":
            mouse.hold()
            time.sleep(spe*3.15)
            mouse.release()
            time.sleep(spe*0.1)
        elif symbol==" ":time.sleep(spe*3.15)
        elif symbol=="/":time.sleep(spe*7)