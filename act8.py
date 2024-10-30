# Demanar a l’usuari que posi 10 números separats per espais. Afegir aquests números a una llista.
# Calcular la suma de tots els números i la seva mitjana i afegir aquests 2 números a la llista. Mostrar per pantalla la llista.

numeros_usuari = input("Introdueix 10 numeros separats per espais: ")


numeros = list(map(int, numeros_usuari.split()))


suma_total = sum(numeros)


mitjana = suma_total / len(numeros)


numeros.append(suma_total)
numeros.append(mitjana)

print("Números de l'usuari + suma i mitjana:", numeros) 
print("Suma total:", suma_total)
print("Mitjana:", mitjana)
