parole = input("scrivere una lista di parole con la formula: parola1, parola2, .../n") #invia a capo per scrivere
lista_1= parole.split(",") #ad ogni, dividere la lista per poicontare le letteredi ogni parola
lista_2=[]
for parola in lista_1:
 lunghezza=len(parola)
 lista_2.append(lunghezza - 1) # -1 perevitare che lo spazio venga contato
print("la lunghezza delle parole è rispettivamente di", lista_2)