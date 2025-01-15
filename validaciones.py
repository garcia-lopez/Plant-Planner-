from os import system
from mensajes import error
import time
      
def validar_opcion_menu(op): #Función para validar la opción seleccionada en el menú
    if op.isdigit(): #Valida si la opción es un número
        if int(op) in range(1, 7): #Valida si la opción está en el rango de 1 a 6 para el menu principal
            return True #Retorna True si la opción está en el rango de 1 a 6
    return False #Retorna False si la opción no está en el rango de 1 a 6

def validar_opcion(op): #Función para validar la opción seleccionada en el menú
    if op.isdigit(): #Valida si la opción es un número
        return True #Retorna True si la opción es un número
    return False #Retorna False si la opción no es un número
    
def validar_lista_vacia(Task_list): #Función para validar si la lista de tareas está vacía
    if Task_list == None: #Valida si la lista de tareas está vacía
        error("No hay tareas") #Imprime mensaje de error si la lista esta vacia
        return True #Retorna True si la lista está vacía
    else: 
        return False #Retorna False si la lista no está vacía