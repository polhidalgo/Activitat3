
abecedari = list("abcdefghijklmnopqrstuvwxyz")


abecedari_filtrat = [lletra for i, lletra in enumerate(abecedari, start=1) if i % 3 != 0]


abecedari_tupla = tuple(abecedari_filtrat)


print("Llista resultat:", abecedari_filtrat)
print("Tupla resultat:", abecedari_tupla)
