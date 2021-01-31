numero=int(input("quanti partecipanti saranno al convento?"))
nomi=[]
inviate=[]
for n in range (numero):
    nome = (input("nome: "))
    nomi.append(nome)
print ("le persone a cui bisogna inviare una lettera diconferma sono: ", nomi)
for i in range(numero):
    risposta= input("per inviare l'email scirvi: invia ")
    if risposta == "invia":

     print("invio email a ", nomi[0])
     inviate.append(nomi[0])
     nomi.remove(nomi[0])
     

     print("bisogna inviare ancora la email di conferma a:", nomi)
     print("la mail di conferma è stata già inviata a:", inviate)
     if nomi==[]:
         print("fatto")

    else:
        print("ti ho detto di scrivere invia, riprova")
        break


