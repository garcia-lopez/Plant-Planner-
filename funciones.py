import time
from tabulate import tabulate
from datos import _task
from os import system
from datos import * #importar la clase tarea y taskTracker
from validaciones import * #importar las funciones de validacion
from menu import * #importar las funciones de impresion de menu
from mensajes import * #importar las funciones de impresion de mensajes
from colorama import Fore, Back, Style, init
init(autoreset=True) # garantiza que los colores no se propaguen de una línea a otra por error.   
            
def obtener_tarea(): #Funcion para obtener el nombre de la tarea
    while True:
        _tarea = input("Tarea nueva => ").strip() #El método strip() se utiliza para eliminar espacios en blanco al principio y al final del input del usuario.
        if _tarea and not _tarea.isspace() and not _task.verificar_tarea(_tarea):  # Verifica que no esté vacío y no solo contenga espacios, y que no exista una tarea con el mismo nombre o conenido
             #La expresión condicional if verifica que _tarea no esté vacía (_tarea es considerada verdadera si tiene contenido), 
             #que no solo consista en espacios en blanco (isspace() verifica si _tarea contiene solo espacios en blanco)
            return _tarea #Retorna el nombre de la tarea si se cumplen las condiciones de la validacion
        else:
            error("La tarea no puede estar vacía o ya ha sido registrada") #Imprime un mensaje de error si no se cumplen las condiciones de la validacion
          
def estado_tarea(): #Funcion para obtener el estado de la tarea
    while True:
        estados = ["Pendiente", "En proceso", "Terminada"]
        encabezado = "Seleccione el estado de la tarea"
        print(tabulate(enumerate(estados, 1), headers=[encabezado], tablefmt="fancy_grid"))
        op = input("=> ")
        if validar_opcion(op) and int(op) in range(1, 4):
          return estados[int(op)-1]
        else:
            error("Opción no valida, seleccione un numero en el rango de 1 a 3")

def categoria_tarea():
    while True:
        categorias = ["Personal", "Trabajo", "Estudio","Otros"]
        encabezado = "Seleccione la categoria de la tarea"
        print(tabulate(enumerate(categorias, 1), headers=[encabezado], tablefmt="fancy_grid"))
        op = input("=> ")
        if validar_opcion(op) and int(op) in range(1, 5):
          return categorias[int(op)-1]
        else:
            error("Opción no valida, seleccione un numero en el rango de 1 a 4")
        
def crear_tarea(): #Funcion para crear una tarea
    imprimir_mensaje("Crear tarea") #Imprime el mensaje "Crear tarea"
    clase = categoria_tarea() #Pide la categoria de la tarea
    print(Fore.MAGENTA + "-"*52) 
    _nombre = obtener_tarea() #Pide el nombre de la tarea
    print(Fore.MAGENTA +"-"*52)
    estado = "Pendiente"
    _tarea = Tarea(clase, _nombre, estado) #Crea un objeto de la clase Tarea para agregarlo a la lista de tareas
    imprimir_mensaje(_task.agregar_tarea(_tarea)) #Imprime el mensaje que retorna el metodo agregar_tarea de la clase taskTracker
    
        
def editar_tarea(): #Funcion para editar una tarea
    while True:
        system("cls")
        lista = imprimir_menu_tareas() #Imprime el menu para seleccionar las tareas en que estado se van a editar, que retorna una lista de tareas, segun la opcion escogida
        if validar_lista_vacia(lista):
            return ""
        elif lista == "3":
            return ""
        else:       
            num = input("Numero de la tarea a editar => ")
            system("cls")
            if validar_opcion(num) and (int(num)-1) in range(len(lista)): #se le resta un uno pq el indice que se le presenta al usuario empieza en 1
                tarea = lista[int(num)-1] #se le resta un uno pq el indice que se le presenta al usuario empieza en 1, y las listas en python empiezan en 0, esto con el objetivo de evitar "index error out of range"
                imprimir_una_tarea([tarea])
                op_edicion = menu_editar_tarea() #Imprime el menu para seleccionar la tarea a editar
                if op_edicion == "1": #Si la opcion es 1, modifica la categoria de la tarea
                    _categoria = categoria_tarea() #Pide la categoria de la tarea para cambiarla
                    _task.cambiar_categoria(tarea[1], _categoria) #Cambia la categoria de la tarea
                elif op_edicion == "2":  #Si la opcion es 2, modifica el nombre de la tarea
                    print("-" * 52)
                    _nombre = obtener_tarea() #Pide el nombre de la tarea o la tarea en si, para cambiarlo
                    _task.modificar_tarea(tarea[1], _nombre) #Cambia el nombre de la tarea, la funcion para modificar recibe como argumentos, el nombre de la tarea y el parametro a cambiar
                elif op_edicion == "3": #Si la opcion es 3, modifica el estado de la tarea
                    _estado = estado_tarea() #Pide el estado de la tarea para cambiarlo
                    _task.cambiar_estado(tarea[1], _estado) #Cambia el estado de la tarea
                elif op_edicion == "4":
                    return ""
                else:
                    error("Opción no valida, seleccione un numero en el rango de 1 a 3")
            else:
                error("Opción no valida")      

def ver_tareas(): #Funcion para ver las tareas y que el usario seleccione como quiere verlas si por estado o categoria
    while True:
        op = print_tareas_estado_categoria()
        if op == "1":
            system("cls")
            aux = ver_tareas_estado() #llama a la funcion ver_tareas_estado
            return aux
        elif op == "2":
            system("cls")
            aux = ver_tareas_categoria() #llama a la funcion ver_tareas_categoria
            return aux
        elif op == "3":
            system("cls")
            Task_list = _task.mostrar_tareas()
            if validar_lista_vacia(Task_list):
              error("No hay tareas")
              return ""
            imprimir_tareas(Task_list)
            break
        elif op == "4":
            return ""
        else:
            error("Opción no válida, seleccione un número en el rango de 1 a 3")
            
def ver_tareas_categoria():  #Funcion para ver las tareas por categoria
    while True:
        op = imprimir_menu_ver_tareas_categoria() #Imprime el menu para seleccionar la categoria de las tareas
        if op == "1":
            system("cls")
            Task_list = _task.mostrar_tareas_categoria("Personal") #Muestra las tareas de la categoria "Personal" que vienen en una lista, que retorna mostrar_tareas_categoria
            if validar_lista_vacia(Task_list):
              error("No hay tareas")
              return ""
            imprimir_tareas(Task_list)
            break
        elif op == "2":
            system("cls")
            Task_list = _task.mostrar_tareas_categoria("Trabajo") #Muestra las tareas de la categoria "Trabajo" que vienen en una lista, que retorna mostrar_tareas_categoria
            if validar_lista_vacia(Task_list): #Si la lista esta vacia, imprime un mensaje de error
              error("No hay tareas")
              return ""
            imprimir_tareas(Task_list)
            break
        elif op == "3":
            system("cls")
            Task_list = _task.mostrar_tareas_categoria("Estudio") #Muestra las tareas de la categoria "Estudio" que vienen en una lista, que retorna mostrar_tareas_categoria
            if validar_lista_vacia(Task_list):
              error("No hay tareas")
              return ""
            imprimir_tareas(Task_list)
            break
        elif op == "4":
            system("cls")
            Task_list = _task.mostrar_tareas_categoria("Otros") #Muestra las tareas de la categoria "Otros" que vienen en una lista, que retorna mostrar_tareas_categoria
            if validar_lista_vacia(Task_list):
              error("No hay tareas")
              return ""
            imprimir_tareas(Task_list)
            break
        elif op == "5":
            return ""
        else:
            error("Opción no válida, seleccione un número en el rango de 1 a 5")
        
def ver_tareas_estado(): #Funcion para ver las tareas por estado
    while True:
        op = imprimir_menu_ver_tareas_estado()
        if op == "1":
            system("cls")
            Task_list = _task.mostrar_tareas_estado("Pendiente")
            if validar_lista_vacia(Task_list): #Si la lista esta vacia, imprime un mensaje de error
              error("No hay tareas")
              return "" #retorna un string vacio para que el ciclo principal continue
            imprimir_tareas(Task_list) #Si la lista no esta vacia imprime las tareas
            break
        elif op == "2":
            system("cls")
            Task_list = _task.mostrar_tareas_estado("En proceso")
            if validar_lista_vacia(Task_list): #Si la lista esta vacia, imprime un mensaje de error
              error("No hay tareas")
              return "" #retorna un string vacio para que el ciclo principal continue
            imprimir_tareas(Task_list)
            break
        elif op == "3":
            system("cls")
            Task_list = _task.mostrar_tareas_estado("Terminada")
            if validar_lista_vacia(Task_list):
              error("No hay tareas")
              return "" #retorna un string vacio para que el ciclo principal continue
            imprimir_tareas(Task_list)
            break
        elif op == "4":
            return "" #retorna un string vacio para volver a mostrar el menu principal
        else:
            error("Opción no válida, seleccione un número en el rango de 1 a 4")

#Funcion para eliminar una tarea
def eliminar_tarea(): 
    op = imprimir_menu_eliminar()
    #Funcion para eliminar una tarea
    while True:
        if op == "1":
            system("cls")
            lista = _task.mostrar_tareas() #Muestra las todas las tareas que vienen en una lista, que retorna mostrar_tareas
            if not validar_lista_vacia(lista): #Si la lista no esta vacia, imprime las tareas
                imprimir_tareas(lista)
                num = input("Numero de la tarea a eliminar => ") #Pide el numero de la tarea a eliminar
                if validar_opcion(num)and (int(num) -1) in range(len(lista)): #se le resta un uno pq el indice que se le presenta al usuario empieza en 1
                    tarea = lista[int(num)-1] #se le resta un uno pq el indice que se le presenta al usuario empieza en 1, y las listas en python empiezan en 0, esto con el objetivo de evitar "index error out of range"
                    _task.eliminar_tarea(tarea[1]) #Elimina la tarea de la lista de tareas
                    return "" #retorna un string vacio para volver a mostrar el menu principal
                else:
                    error("Opción no valida")
            else:
                error("No hay tareas")
                return "" #retorna un string vacio para volver a mostrar el menu principal
        else:
            return "" #retorna un string vacio para volver a mostrar el menu principal

#Funcion para imprimir el reporte de tareas
def reporte_de_tareas_():
    imprimir_mensaje("Reporte de tareas")
    terminada = _task.mostrar_tareas_estado("Terminada") #Muestra las tareas en estado "Terminada" que vienen en una lista, que retorna mostrar_tareas_estado
    pendiente = _task.mostrar_tareas_estado("Pendiente") #Muestra las tareas en estado "Pendiente" que vienen en una lista, que retorna mostrar_tareas_estado
    en_proceso = _task.mostrar_tareas_estado("En proceso") #Muestra las tareas en estado "En proceso" que vienen en una lista, que retorna mostrar_tareas_estado

    fin = len(terminada) if terminada else 0 #se utiliza para asignar el valor de la longitud de la lista terminada a la variable fin.
    proceso = len(en_proceso) if en_proceso else 0
    pendientes = len(pendiente) if pendiente else 0
    total_tareas = fin + proceso + pendientes
    
    #se utiliza para asignar el valor de la longitud de la lista terminada a la variable fin. 
    # Si la lista terminada tiene elementos (es decir, si no es None o está vacía), 
    # se asigna la longitud de la lista a fin. De lo contrario, se asigna 0.
    # Crear una lista de listas para los datos de la tabla
    tabla_datos = [
        ["Terminada", fin],
        ["En proceso", proceso],
        ["Pendiente", pendientes],
        ["Total", total_tareas]
    ]

    # Imprimir la tabla utilizando tabulate
    print(tabulate(tabla_datos, headers=["Estado de la tarea", "Total de tareas"],tablefmt="fancy_grid"))

  
