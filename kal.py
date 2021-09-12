import random
import string
print("ora giochiamo a saltar per aria, quando trovi la bomba vinci e sta attento a ricordarti dove hai già guardato perchè non sarò certo io ad aiutarti. ")
print("dopo aver scelto il livello potrai dtentare di idovinare digitando i numeri corrispodenti a righe e colonne che andranno da 0 al massimo di casellle disponibili")
print("buona fortuna")
start=int(input("premi 1 per iniziare"))
if start==1:

 n=int(input("scegli un livello che può andare da -2 fio al numero positivo che più preferisci"))
 liv=(n+3)*n

 o=random.randint(0,n+3)
 v=random.randint(0,n+3)
 
 for y in range(n+3):
       for x in range(n+3):
         
           print("[ ]", end = "")
       print()
 for i in range(liv):
  horizontal=int(input("scegli la riga"))
  vertical=int(input("scegli la colonna"))
  if vertical==1:
   zup=n-vertical-2
  elif vertical==1:
   zup=n-vertical-3
  else:
    zup=n-vertical-1
  zip=n-1
  if (horizontal==o) and (vertical==v):
    
    print ("HAI VINTO SEI SALTATO PER ARIA")
    break
  
  else:
    
     for y in range(n+3):
       for x in range(n+3):
         if x == vertical and y == horizontal:
             print("[+]", end = "")
             if n==0:
              for i in range (zip):
                 print("[ ]", end = "")
             else:
               for i in range (zup):
                 print("[ ]", end = "")
             
         else: 
           print("[ ]", end = "")
       print()
     print("ritenta sarai più fortunato")
