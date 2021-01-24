nazioni = ["italia", "francia", "germania", "albania", "brasile", "cina", "croazia", "estonia", "georgia"]
capitali = ["roma", "parigi", "berlino", "tirana", "brasilia", "pechino", "zagabria", "tallinn", "tiblisi" ] 

dictionary = {}

#dictionary[key] = value

for i in range(len(nazioni)):
    dictionary[capitali[i]] = nazioni[i]


capitale = input("inserisci capitale")
exist = False

for e in dictionary:
    if capitale == e:
        exist = True

if exist:
    print(dictionary[capitale])

else:
    print("errore")