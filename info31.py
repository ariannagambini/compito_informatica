numero = int(input("Inserire il numero decimale da trasformare"))
n = numero
binario = []
quoziente = 1
while True:
    if numero == 0 or quoziente == 0:
        break
    elif quoziente <= numero:
        quoziente = round(numero / 2)
        resto =numero%2
        binario.append(resto)
        numero = quoziente
    else: 
        numero = round(quoziente / 2)
        resto = quoziente%2
        binario.append(resto)
        quoziente = numero
binario.reverse()
print(binario) 
bin = int(input("Puoi riscrivere il numero binario che e risulato?"))
controllo = int(str(bin), base=2)
print(controllo)
if n == controllo:
    print("Il programma funziona")
    print("Il numero", bin)
else:
    print("I numeri non coincidono")