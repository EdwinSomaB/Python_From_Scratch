"""
Utilice el bucle FOR cuando conozca las veces que se repetira el proceso

"""

# for num in range(5,11):
#     print(f"{num }-Bienvenido al curso de Python")
# print("fin del bucle")    

# frutas=["manzana","banana","cereza"]
# for fruta in frutas:
#     print(fruta)
    
# mensaje="Bienvenido al curso de Python"    
# for letra in mensaje:
#     print(letra)

suma_numeros=0
cont_num=0
for x in range(1,6):
    numeros_ing=int(input("Ingrese un Numero:"))
    suma_numeros=suma_numeros+numeros_ing
    cont_num=cont_num+1
print(f"La Suma total es {suma_numeros} y el numero de vueltas {cont_num}")    
    