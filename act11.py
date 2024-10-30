monedes = {
    "Dolar canadenc": "$",
    "Yen japonès": "¥",
    "Lliura esterlina": "£",
    "Peso mexicà": "$",
    "Franco suís": "₣",
    "Euro": "€",
}

moneda = input("Escriu una moneda (ej: Dòlar canadenc, Peso mexicà, Yen japonès): ")

if moneda in monedes:
    print(f"El símbol de {moneda} és: {monedes[moneda]}")
else:
    print("La moneda no es troba al llistat.")
