#Ja specifikacija ir pieminets viss vajadzigais cena,funkcijas viss.
#Nekāda papild informacija ir vajadzīga.
#Nav nekādu jautājumi. 
import time


skaits = int(input("Cik daudz kreklu jūs pirksiet?"))
def tkrekli():
    cena = 0
    _ = skaits+1
    for _ in range(skaits):
        print("Kādu tipu {} kreklu jūs gribat?".format(_+1))
        print("1.Tekstu")
        print("2.Foto")
        print("3.Zime")
        a = int(input("Rakstiet ciparu šeit: "))
        if a == 1:
            cena += 5
        elif a == 2:
            cena += 20
        elif a == 3:
            cena += 7
    return cena
cena = tkrekli()
piegade = input("Vai jums ir vajadzīga piegāde. Atbildiet ar tikai Jā vai Nē. ")
if piegade == "Jā":
    if cena >= 100:
        print("Tādēļ ka jūsu prece ir virs 100 Eiro, jums ir 5% atlaide")
        time.sleep(0.5)
        print("Jums jāmaksā ir",cena* 0.95)
        exit()
    if cena <= 50:
        print("Tādēļ ka jūsu prece ir zem 50 Eiro, jums jāmaksā klāt ir 15 Eiro" )
        time.sleep(1)
        print("Kopa tas maksās",cena+15,"Eiro")
        exit()
    else:
        print("Jums viss kopa maksās",cena,"EIRO")
        exit()
else:
    print("Jums viss kopa maksās",cena,"Eiro")
#turpinajums kjip 
#Ja specifikacija ir pieminets viss vajadzigais cena,funkcijas viss.

#Nekāda papild informacija ir vajadzīga.

#Nav nekādu jautājumi.

import time

def tkrekli():

    cena = 0

    _ = skaits + 1

    for _ in range(skaits):

        print("Kādu dizainu uz {} kreklu jūs gribat?".format(_+1))

        time.sleep (0.3)

        print("1.Tekstu")

        time.sleep (0.3)

        print("2.Foto")

        time.sleep (0.3)

        print("3.Zime")

        time.sleep (0.3)

        a = int(input("Rakstiet ciparu šeit: "))

        if a == 1:

            cena += 5

        elif a == 2:

            cena += 20

        elif a == 3:

            cena += 7

            dizains = input("Vai jūs vēlaties pievienot vēlvienu dizainu {} kreklam? Atbildiet ar Jā vai Nē. ".format(_+1))

            if dizains == 'Nē':

                break

            elif dizains == "Jā":

                for _ in range(skaits):

                    print("Kādu dizainu jūs velaties pievienot? ")

                    time.sleep (0.3)

                    print("1.Tekstu")

                    time.sleep (0.3)

                    print("2.Foto")  

                    time.sleep (0.3)  

                    print("3.Zime")

                    time.sleep (0.3)

                    b = int(input("Rakstiet ciparu šeit: "))

                    if b == 1:

                        cena+=5

                    elif b == 2:

                        cena += 20

                    elif b == 3:

                        cena += 7

    return cena

skaits = int(input("Cik daudz kreklu jūs pirksiet?"))

cena = tkrekli()

piegade = input("Vai jums ir vajadzīga piegāde. Atbildiet ar tikai Jā vai Nē. ")

if piegade == "Jā":

    if cena >= 100:

        print("Tādēļ ka jūsu prece ir virs 100 Eiro, jums ir 5% atlaide")

        time.sleep(0.5)

        print("Jums jāmaksā ir",cena* 0.95)

        exit()

    elif cena <= 50:

        print("Tādēļ ka jūsu prece ir zem 50 Eiro, jums jāmaksā klāt ir 15 Eiro" )

        time.sleep(1)

        print("Kopa tas maksās",cena+15,"Eiro")

        exit()

    else:

        print("Jums viss kopa maksās",cena,"EIRO")

        exit()

else:

    print("Jums viss kopa maksās",cena,"Eiro")
