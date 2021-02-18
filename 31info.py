nord = int(input("fatturato del nord "))
centro = int(input("fatturato del centro "))
sud = int(input("fatturato del sud "))
isole = int(input("fatturato delle isole "))

fatturati = {'nord': nord, 'centro': centro, 'sud': sud, 'isole': isole}

totale=nord+centro+sud+isole

perc_n=nord*100/totale
perc_s=sud*100/totale
perc_c=centro*100/totale
perc_i=isole*100/totale

n=str(perc_n) + "%"
s=str(perc_s) + "%"
i=str(perc_i) + "%"
c=str(perc_c) + "%"

percentuali = {'nord': n, 'centro': c, 'sud': s, 'isole': i}

print ("il totale è ", totale)
print ("le percentuali delle vendite nelle quattro zone rispetto al totale sono:", percentuali )