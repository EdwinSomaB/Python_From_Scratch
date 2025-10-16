"""
AMBITO LOCAL
"""

global_var=20 #Variable globales

def my_funcion():
    local_var=10 #Variable Local
    print(local_var)
    
    
def my_funcion_dos():
    print(global_var)    
    

#my_funcion_dos()    

"""
AMBITO GLOBAL
"""

COUNT= 0

def incremento_valor():
    global COUNT
    COUNT +=1
    
    
incremento_valor()
print(COUNT)    



