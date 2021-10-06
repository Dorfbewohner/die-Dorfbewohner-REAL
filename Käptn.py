from random import randint

number=randint(1,100)
tries=6

while tries>0:
    print ("Du hast noch",tries,"Versuche")
    guess=input("Wähle eine Zahl zwischen 1-100\n")
    if int(guess)<number:
        print("Zu niedrig du Holzbein!\n")
        tries-=1
    elif int(guess)>100:
        print("ich sagte 1-100 du Landratte!\n")
        break
    elif int(guess)>number:
        print("zu hoch mein Sohnemann.\n")
        tries-=1
    elif int(guess)==number: 
        print("DU HAST DIE BEUTE ERLANGT!!! ARRRGGGGGHHH")
        break
if tries ==0:
    print("Du hast keine Versuche mehr! Verloren, du Jammerlappen!")
