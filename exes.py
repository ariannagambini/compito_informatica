conti_bancari = {"1": 100,
                 "2": 1000,
                 "3": 10000,
                 "4": 100000,
                 "5": 1000000,
}

numero_conto = input("Immettere il numero del conto corrente per visualizzare il proprio saldo: ")

if numero_conto not in conti_bancari:
    print("Spiacenti, il conto: ", numero_conto, " non si trova nella mappa")
else:
    print("Il saldo del conto ", numero_conto, " e di ", conti_bancari[numero_conto], " euro.")