import sys
from itertools import product

try:
    resultado = int(sys.argv[1])
except:
    print("Tés que indicar qual tem que ser o resultado")
    sys.exit(1)

lista = list(product([12,10,8,7,6,5], repeat=5))
lista2 = []

for a in lista:
    if sum(a) == resultado:
        ordenado = sorted(list(a),reverse=True)
        if ordenado not in lista2:
            lista2.append(ordenado)

if lista2:
    for e in lista2:
        print(e)
else:
    print("Nenguma combinaçom dá a suma")
