"""
001.-Calcular el Precio Total de un Producto co IGV

#PRECIO_SIN_IGV=100
#IGV=0.18
#precio_con_igv=PRECIO_SIN_IGV*(1+IGV)
#print(f"Precio con Igv: {precio_con_igv:.2f}")


nombre_producto=input("Ingrese el Nombre del producto:")
precio_producto=float(input("Ingrese el Precio del Producto:"))
cantidad_producto=int(input("Ingrese la cantidad del producto:"))
total_a_pagar=precio_producto*cantidad_producto
igv_a_pagar=total_a_pagar*0.18
total_neto=total_a_pagar+igv_a_pagar
print(f"El Total a Pagar por el producto es: {total_neto:.2f} el IGV es: {igv_a_pagar:.2f}")

"""

"""
002.-Calcular el Salario Semanal

nombre_trabajador=input("Ingrese el Nombre del Trabajador:")
horas_trab=int(input("Ingrese las Horas Trabajadas:"))
tarifa_hora=float(input("Ingrese la Tarifa Por Hora:"))
salario_diario=tarifa_hora*horas_trab
print(f"El Salario del Trabajador {nombre_trabajador} es {salario_diario}")
"""

"""
003-Calcular el Promedio de Notas de un Alumno

nota_uno=float(input("Ingresar la Nota Uno:"))
nota_dos=float(input("Ingresar la Nota Dos:"))
nota_tres=float(input("Ingresar la Nota Tres:"))
promedio_final=(nota_uno+nota_dos+nota_tres)/3
if promedio_final>=10:
    print(f"El Alumno Aprobo el Curso  con promedio {promedio_final}")
else:
    print(f"El Alumno No Aprobo el Curso con promedio {promedio_final}")    
#print(f"El Promedio Obtenido por el Alumnmo es {promedio_final}")
"""
"""
004-Convertir de Dolares a euros

cant_dol=float(input("Ingrese la cantidad de dolares a convertir:"))
tipo_cambio=float(input("Ingrese el Tipo de cambio:"))
total_euros=cant_dol*tipo_cambio
print(f"Total en Euos es {total_euros:.2f}")
"""

"""
005-Convertir Segundos a Horas, Minutos y segundos

total_segundos=int(input("Ingresar la cantidad de Segundos:"))
total_horas=total_segundos // 3600
minutos=(total_segundos % 3600) //60
segundos_restantes= total_segundos % 60
print(f"{total_horas} Horas , {minutos} Minutos , {segundos_restantes} Segundos")

"""













