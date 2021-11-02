lista = []

while True:
    nombre = input("nombre: ")
    if nombre == "fin":
        break
    numero_telefono = input("numero de telefono: ")
    línea = {}
    línea["nombre"] = nombre
    línea["numero de telefono"] = numero_telefono
    lista.append(línea)
    for línea in lista:
        print("lista:\n",línea)