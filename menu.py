from datos import _task
from validaciones import * #importar las funciones de validacion
from tabulate import tabulate
from mensajes import * #importar las funciones de impresion de mensajes
from colorama import Fore, Back, Style, init
init(autoreset=True) # garantiza que los colores no se propaguen de una línea a otra por error.

def imprimir_tareas(lista_tareas): #imprime las tareas junto con el indice que le corresponde en la lista
    if lista_tareas != None:
        lista_con_indices = [(i + 1, *tarea) for i, tarea in enumerate(lista_tareas)]
        #genera una lista de tuplas donde cada tupla contiene el índice de la tarea más 1 (índices empezando desde 1) 
        # seguido de los elementos de la tarea misma, para cada tarea en lista_tareas
        print(tabulate(lista_con_indices, headers=[" ", "Categoria", "Tarea", "Estado"], tablefmt="fancy_grid"))
        
def imprimir_una_tarea(tarea_lista): #Imprime una tarea, luego de ser selccionada, sin su indice 
    if tarea_lista != None:
        print(tabulate(tarea_lista, headers=["Categoria", "Tarea", "Estado"], tablefmt="fancy_grid"))
        
def imprimir_menu(): #Imprimir menu principal del programa
    print(Fore.MAGENTA + "1."+ Fore.WHITE +"Crear tarea".rjust(50,"."))
    print(Fore.GREEN + "2."+ Fore.WHITE +"Ver tareas".rjust(50,"."))
    print(Fore.MAGENTA + "3."+ Fore.WHITE+"Modificar tarea".rjust(50,"."))
    print(Fore.GREEN + "4."+ Fore.WHITE+"Eliminar tarea".rjust(50,"."))
    print(Fore.MAGENTA + "5."+ Fore.WHITE+"Reporte de tareas".rjust(50,"."))
    print(Fore.GREEN+ "6."+ Fore.WHITE+"Salir".rjust(50,"."))
    print(Fore.MAGENTA + "-"*52)
    opcion = input("Ingrese la opción: ")
    if validar_opcion_menu(opcion):
        return opcion
    else:
        error("Opción no valida, seleccione un numero en el rango de 1 a 6")
        
#Menu de funcion Ver tareas
#Menu para seleccionar si se van a ver las tareas por estado o por categoria
def print_tareas_estado_categoria():
    while True:
        imprimir_mensaje("Ver tareas")
        print(Fore.MAGENTA + "1."+ Fore.WHITE +"Por estado".rjust(50, "."))
        print(Fore.GREEN + "2."+ Fore.WHITE +"Por categoria".rjust(50, "."))
        print(Fore.MAGENTA + "3."+ Fore.WHITE +"Todas las tareas".rjust(50, "."))
        print(Fore.GREEN + "4."+ Fore.WHITE +" <= Regresar".rjust(50, "."))
        print(Fore.MAGENTA + "-"*52)
        opcion = input("Ingrese la opción => ")
        if validar_opcion(opcion):
            if opcion in ["1", "2", "3", "4"]:
                return opcion #Retorna la opcion seleccionada
            else:
                error("Opción no válida, seleccione un número en el rango de 1 a 4")
        else:
            error("Opción no válida, seleccione un número en el rango de 1 a 4")
                        
def imprimir_menu_ver_tareas_estado(): #Imprimir menu para seleccionar que tareas se van a ver de acuerdo a su estado
    while True:
        imprimir_mensaje("Ver tareas")
        print(Fore.MAGENTA + "1."+ Fore.WHITE +"Tareas pendientes".rjust(50, "."))
        print(Fore.GREEN + "2."+ Fore.WHITE +"Tareas en proceso".rjust(50, "."))
        print(Fore.MAGENTA + "3."+ Fore.WHITE +"Tareas terminadas".rjust(50, "."))       
        print(Fore.GREEN + "4."+ Fore.WHITE +" <= Regresar".rjust(50, "."))
        print(Fore.MAGENTA + "-"*52)
        opcion = input("Ingrese la opción => ")
        if validar_opcion(opcion):
            if opcion in ["1", "2", "3", "4"]:
                return opcion
            else:
                error("Opción no válida, seleccione un número en el rango de 1 a 4")
        else:
            error("Opción no válida, seleccione un número en el rango de 1 a 4")

def imprimir_menu_ver_tareas_categoria(): #Imprimir menu para seleccionar que tareas se van a ver de acuerdo a su categoria
    while True:
        imprimir_mensaje("Ver tareas")
        print(Fore.MAGENTA + "1."+ Fore.WHITE +"Personal".rjust(50, "."))
        print(Fore.GREEN + "2."+ Fore.WHITE +"Trabajo".rjust(50, "."))
        print(Fore.MAGENTA + "3."+ Fore.WHITE +"Estudio".rjust(50, "."))
        print(Fore.GREEN + "4."+ Fore.WHITE +"Otros".rjust(50, "."))              
        print(Fore.MAGENTA + "5."+ Fore.WHITE +" <= Regresar".rjust(50, "."))
        print(Fore.MAGENTA + "-"*52)
        opcion = input("Ingrese la opción => ")
        if validar_opcion(opcion):
            if opcion in ["1", "2", "3", "4", "5"]:
                return opcion
            else:
                error("Opción no válida, seleccione un número en el rango de 1 a 5")
        else:
            error("Opción no válida, seleccione un número en el rango de 1 a 5")
                
#Imprimir menu para editar una tarea
def imprimir_menu_tareas(): #Imprimir menu para seleccionar las tareas en que estado se van a editar de acuerdo a su estado
    while True: 
        Task_list = [] #Lista vacia
        imprimir_mensaje("Modificar tarea")
        print(Fore.MAGENTA + "1."+ Fore.WHITE +"Tarea Pendiente".rjust(50, "."))
        print(Fore.GREEN + "2."+ Fore.WHITE +"Tarea en Proceso".rjust(50, "."))
        print(Fore.MAGENTA + "3."+ Fore.WHITE+" <= Regresar".rjust(50, "."))
        print(Fore.MAGENTA + "-"*52)
        opcion = input("Ingrese la opción => ")
        if validar_opcion(opcion):
            if opcion == "1":
                system("cls")
                Task_list = _task.mostrar_tareas_estado("Pendiente") #Muestra las tareas en estado "Pendiente" que vienen en una lista, que retorna mostrar_tareas_estado
                imprimir_tareas(Task_list) #Imprime las tareas, junto con los indices para poder acceder a ellas
                return Task_list
            if opcion == "2":
                system("cls")
                Task_list = _task.mostrar_tareas_estado("En proceso")
                imprimir_tareas(Task_list)
                return Task_list
            if opcion == "3":
                return "3"
            else:
                error("Opción no válida, seleccione un número en el rango de 1 a 3")
        else:
            error("Opción no válida, seleccione un número en el rango de 1 a 3")
            
def menu_editar_tarea(): #Imprimir menu para seleccionar que se va a editar de la tarea
    while True:
        imprimir_mensaje("Editar tarea")
        print(Fore.MAGENTA + "1."+ Fore.WHITE + "Modificar categoria".rjust(50, ".")) #Imprime las opciones para editar la tarea
        print(Fore.GREEN + "2."+ Fore.WHITE +"Modificar tarea".rjust(50, "."))
        print(Fore.MAGENTA + "3." + Fore.WHITE + "Modificar estado".rjust(50, "."))
        print(Fore.GREEN + "4."+ Fore.WHITE + " <= Regresar".rjust(50, "."))
        print(Fore.MAGENTA + "-"*52)
        opcion = input("Ingrese la opción => ")
        if validar_opcion(opcion): #Valida que la opcion sea un numero
            if opcion in ["1", "2", "3", "4"]:
                system("cls")
                return opcion
            else:
                error("Opción no válida, seleccione un número en el rango de 1 a 4") #Si la opcion no es valida, imprime un mensaje de error
        else:
            error("Ocurrió un error") #Si la opcion no es valida, imprime un mensaje de error
            
#Imprimir menu para seleccionar la tarea a eliminar o regresar al menu principal
def imprimir_menu_eliminar(): #Imprimir menu para seleccionar la tarea a eliminar 
    while True:
        Task_list = []
        imprimir_mensaje("Eliminar tarea")
        print(Fore.MAGENTA + "1."+"Eliminar tarea".rjust(50,"."))
        print(Fore.GREEN + "2."+" <= Regresar".rjust(50,"."))
        print(Fore.MAGENTA + "-"*52)
        opcion = input("Ingrese la opción => ")
        if validar_opcion(opcion):
            if opcion in ["1", "2"]: #Si la opcion es 1 o 2
                return opcion #Retorna la opcion
            else:
                error("Opción no valida, seleccione un numero en el rango de 1 a 2") #Si la opcion no es 1 o 2, imprime un mensaje de error
        else:
            error("Opción no valida, seleccione un numero en el rango de 1 a 2") #Si la opcion no es valida, imprime un mensaje de error


            

            
