numero_nazioni = int(input("Quante nazioni desidera inserire? "))
capitali = []
nazioni = []
contatore = 0
while True:
    nazione = input("Inserire il nome della nazione: ")
    nazioni.append(nazione)
    capitale = input("Inserire il nome della capitale: ")
    capitali.appen(capitale)
    contatore += 1
    if contatore == numero_nazioni:
        break
nazione = input("Inserire il nome della nazione della quale si vuole conoscere la capitale: ")
if nazione in nazioni:
    indice = nazioni.index(nazione)
    print("La capitale di questa nazione e", capitale[indice])
else:
    print("La nazione non c'e")