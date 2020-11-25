#esercizio 1
cand1 = input("come si chiama il primo candidato?")
cand2 = input("come si chiama il secondo candidato?")
voti1 = int(input("quanti voti ha ottenuto?" + cand1 +"?"))
voti2 = int(input("quanti voti ha ottenuto?" + cand2 +"?"))
somma = voti1 + voti2
percvoti1 = (voti1*100/somma)
percvoti2 = (voti2*100/somma)
print (percvoti1, "%", cand1)
print (percvoti2, "%", cand2)
if percvoti1 > percvoti2:
    print ("ha vinto" + cand1)
elif percvoti1 < percvoti2:
    print ("ha vinto" + cand1)
else:
    print ("mhhh")

#esercizio2
lista = []
cand1= input("come si chiama il primo candidato?")
cand2= input("come si chiama il secondo candidato?")
lista.append (cand1)
lista.append (cand2)
lista.sort ()
print (lista)
voti1= int(input("quanti voti ha ottenuto" + cand1 +"?"))
voti2= int(input("quanti voti ha ottenuto" + cand2 +"?"))
voti =[]
voti.append (voti1)
voti.append (voti2)
if voti1>voti2:
    print ("ha vinto" +cand1)
elif voti1<voti2:
    print ("ha vinto" +cand2)
elif voti1==voti2:
    print ("pareggio")
voti.reverse ()
print(voti)

#esercizio3
stipendi_totale = 0
stipendi_numero = 0
while True:
    stipendio=input("inserire il valore di uno stipendio")
    if stipendio=="-1":
        break
    elif stipendio=="stop":
        stipendio=int(stipendio)
        stipendi_totale+=stipendio
        stipendi_numero+=1
media=int(stipendi_totale/stipendi_numero)
print=("la media degli stipendi è", media,)