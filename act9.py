
assignatures = ["Matemàtiques", "Història", "Llengua", "Ciències", "Anglès", "Educació Física"]

notes = []

for assignatura in assignatures:
    nota = float(input(f"Introdueix la nota de {assignatura}: "))
    notes.append(nota)


for i in range(len(assignatures)):
    print(f"A {assignatures[i]} ha tret {notes[i]}")


notes_assignatures = {}

for assignatura in ["Matemàtiques", "Història", "Llengua", "Ciències", "Anglès", "Educació Física"]:
    nota = float(input(f"Introdueix la nota de {assignatura}: "))
    notes_assignatures[assignatura] = nota

for assignatura, nota in notes_assignatures.items():
    print(f"A {assignatura} ha tret {nota}")
