from os import system
from funciones import *
from mensajes import *
from colorama import Fore
init(autoreset=True) # garantiza que los colores no se propaguen de una línea a otra por error.

def principal(): #Función principal del programa
    while True:
        system("cls")
        aux = 0
        imprimir_mensaje("Plant - Planner") #Imprime el encabezado del programa
        op = imprimir_menu()
        if op == "1": #Si la opción seleccionada es 1, se llama a la función crear_tarea
            system("cls")
            crear_tarea()   
        elif op == "2": #Si la opción seleccionada es 2, se llama a la función ver_tareas
            system("cls")
            aux = ver_tareas()
        elif op == "3": #Si la opción seleccionada es 3, se llama a la función editar_tarea
            system("cls")
            aux = editar_tarea()
        elif op == "4": #Si la opción seleccionada es 4, se llama a la función eliminar_tarea
            system("cls")
            aux = eliminar_tarea()
        elif op == "5":
            system("cls")
            reporte_de_tareas_()
        elif op == "6": #Si la opción seleccionada es 6, se cierra el programa
            system("cls")
            imprimir_mensaje("Gracias por usar Plant - Planner")
            break
        while aux != "":
            aux = input(Fore.MAGENTA + "Presione enter para continuar...")
        

if __name__ == "__main__": #Si el archivo es el principal, se llama a la función principal
    principal()