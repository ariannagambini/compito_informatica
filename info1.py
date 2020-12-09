parola=input ("scrivere la parola da processare:")
parola_1 =parola [::-1] #gira la stringa
if parola == parola_1:
 print(parola, "è un polindromo")
else:
 print(parola, "non è un palindromo")