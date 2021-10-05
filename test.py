import time
name=input("Wie lautet ihr name:\n")
while len(name)<=0:
    name = input("Bitte geben Sie erneut Ihren Namen ein: ")
    
alter=input("Wie alt sind Sie?\n")
while len(alter)<=0:
    alter=input("Bitte geben Sie erneut Ihre Alter ein:")
else:
    print(alter,"Ist schon sehr alt, aber ich freue mich das du da bist", name)
import time
time.sleep(2)
bereit=input("Als nächstes darfst du nur mit Ja/Nein antworten, Verstanden?:\n")
if bereit.lower() == "ja":print("Dann fangen wir mal an!")
else:
        print("dann bist du nicht gemacht hierfür.")
        exit()

bereit=input("Magst du Programmieren?\n")
if bereit.lower()== "ja":print("Super! dann kannst du dich gut um mich kümmern.")
else:
    print("Schade :(\n")
    time.sleep(1)
print( "Hast du wenigsten spaß mit mir zu schreiben?\n")
if bereit.lower()=="ja":print("ich schreib auch gerne mit dir, auch wenn du bisschen Stinkst :)")
else:
    print("okay schade... wir machen trotzdem mal weiter!")
    time.sleep(1)
    
bereit=input("Hast du Haustiere?\n")
if bereit.lower()=="ja":print("ich liebe Haustiere. Ich habe",name,"als Haustier.")


     
