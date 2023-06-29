### 1_DECLARANDO UNA FUNCION SIMPLE

def mi_primera_funcion():
    print("Esta es primera funcion")

mi_primera_funcion()

### 2_DECLARANDO UNA FUNCION Y UTILIZANDO LISTAS

def concatenar(lista1,lista2):
        return lista1+lista2


lista1 = [1,2,3]
lista2 = [4,5,6]

#concatenar()

print(concatenar(lista1,lista2))

### 3_DECLARANDO UNA FUNCION MULTIPLICACCION pasando parametros

def multiplicacion (num1,num2):
      return num1*num2

#multiplicacion()
print(multiplicacion(10,2))


### 4_FUNCIONES SUMA Y RESTA (POR TECLADO)

def suma(a,b):
      return a + b

def resta(a,b):
      return a - b

a=int(input("ingrese valor de a= "))
b=int(input("ingrese valor de b= "))

#se llama a la funcion suma
resultado = suma(a,b)
print("la suma es de:",resultado)

#se llama funcion resta
resultado2 = resta(a,b)
print("la resta es de:",resultado2)