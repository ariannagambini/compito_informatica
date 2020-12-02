nome = []
lanci = []
contatore = 1
while True:
    nome_candidato=input("Inserire il nome dello studente " + str(contatore))
    lanci_candidato= input("Inserire il numero di lanci di "+ nome_candidato)
    nome.append (nome_candidato)
    lanci.append(lanci_candidato)
    contatore += 1
    domanda= int(input("Vuoi inserire un nuovo candidato? Se si digita 1 senno digita 0"))
    if domanda == 0:
        break
    else:
        continue
print(max(lanci))