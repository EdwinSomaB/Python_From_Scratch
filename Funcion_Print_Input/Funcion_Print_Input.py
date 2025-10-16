"""
Funcion Print
"""

nombre_curso="Python"
precio_curso=200.20
horas_curso=56
estado_curso=True
#print("Hola Mundo desde Python")
#print('Mi Nombre es Armando Ruiz')

cadena=f"El Curso es {nombre_curso} el precio es {precio_curso} y las horas es {horas_curso}"

#print(nombre_curso)
#print(cadena)
#print(f"El Nombre del producto ingresado es {nombre_producto} y su precio es {precio_producto}")
#print(f"El Tipo de datos del nombre {type(nombre_producto)}")
#print(f"El Tipo de datos del precio {type(precio_producto)}")

"""
Funcion Input

nombre_producto=input("Ingrese el nombre del producto:")
precio_producto=float(input("Ingrese el precio del producto:"))
cant_prod=int(input("Ingrese la cantidad del producto:"))
total=precio_producto*cant_prod
print(f"El Total a pagar es {total}")
"""

"""
Funcion Format
sintaxis:
"cadena de texto {}".format(valor)
"""

nombre_usuario="Armando"
saludo = "Hola , {}".format(nombre_usuario)
print(saludo)


pi=3.14159
formated_pi="El Valor de pi es {:.2f}".format(pi)
print(formated_pi)

nombre_persona="Alice"
saludo=f"Hola , {nombre_persona}"
print(saludo)






