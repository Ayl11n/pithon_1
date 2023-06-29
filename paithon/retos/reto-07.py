
def diccionario(frase):
    return frase(input("Escriba una frase: "))


frase={
    "Palabras":print(diccionario),
    "Longitud palabras":len(diccionario("frase"))
    }

print("El resultado es: ",frase)