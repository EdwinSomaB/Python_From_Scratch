nom_per = "Armando"
ape_per = 'Ruiz'
edad_per = 48
sue_per = 1200.985666 #float
act_per = True
total_prod = "1900"
cantidad_prod=8

#Conversion de datos
total_pagar =int(total_prod)*cantidad_prod  #convertir = CAST
cadena_dos=str(sue_per)
tipo_dato=type(cadena_dos)

#print(total_pagar)

#Concatenacion y formateo de datos
cadena_unos= nom_per + str(edad_per)
#print(nom_per,sue_per)
#print(f"El Nombre de la persona es {nom_per} y su sueldo es {round(sue_per,3)}")


nuevo_sueldo=f"{sue_per:.2f}"
print(nuevo_sueldo)





