a = input ('Sag mal "Was?".')
if a  == "Was?":
    print('Deine Hose ist nass.')
else:
    a = input ('Bitte sag "Was?"!')
while a != "Was?":
    if a != "Was?":
        a = input ('Bitte sag "Was?"!')
        if a == "Was?":
            print('Deine Hose ist nass')
input ()