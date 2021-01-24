nazioni = ["italia", "francia", "germania", "albania", "brasile", "cina", "croazia", "estonia", "georgia"]
capitali = ["roma", "parigi", "berlino", "tirana", "brasilia", "pechino", "zagabria", "tallinn", "tiblisi" ] 

dictionary = {}

#dictionary[key] = value

for i in range(len(nazioni)):
    dictionary[nazioni[i]] = capitali[i]


nazione = input("inserisci nazione")
exist = False

for e in dictionary:
    if nazione == e:
        exist = True

if exist:
    print(dictionary[nazione])

else:
    print("errore")