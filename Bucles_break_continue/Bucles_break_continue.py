"""
break .- Se utiliza para salir inmediatamente de un bucle.
continue:_Omitir el resto del codigo
"""

# for i in range(10):
#     if i==5:
#         break
#     print(i)
    
# contador=0
# while True:
#     if contador>=5:
#         break
#     print(contador)    
#     contador +=1
    
# for i in range(10):
#     if i%2==0:
#         continue #saltar cunado el numero sea par   
#     print(i)
    

contador=0
while contador<10:
    contador +=1
    if contador %2==0:
        continue
    print(contador)    
    