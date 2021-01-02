a = float(input("Inserisci il valore di a "))
b = float(input("Inserisci il valore di b "))
quoziente_negativo = - (b / a)
if a == 0 and b == 0:
    print ("L' equazione è indeterminata")
elif a == 0 and b != 0:
    print ("L' equazione è impossibile")
elif a != 0 and b == 0:
    print ("L' equazione risulta x = 0 ")
elif a != 0 and b != 0:
    print ("L' equazione risulta x = ", quoziente_negativo )