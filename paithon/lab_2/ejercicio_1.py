n1=[]
n2=[]

for i in range (2,30,3):
    print(i)
    if i%5==0:
        n1.append(i)
    if i%2!=0:
        n2.append(i)

print("Los numeros divisibles por 5 son:",n1)
print("La suma es",sum(n1))
print("Los numeros impares",n2)
print("Y la suma es",sum(n2))