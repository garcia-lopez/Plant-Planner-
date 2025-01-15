

class Tarea(): #Clase tarea
    def __init__(self, categoria, nombre, estado):
        self.categoria = categoria
        self.nombre = nombre
        self.estado = estado

class Task_Traker(): #Clase TaskTracker para manejar las tareas
    def __init__(self):
        self.lista_tareas = []
        
    def verificar_tarea(self, nombre):  # Metodo de la clase tarea para verificar si la tarea ya existe
       for tarea in self.lista_tareas: #Recorre la lista de tareas
         if tarea.nombre.upper() == nombre.upper(): #Si el nombre de la tarea es igual al nombre ingresado
                return True #Retorna True, que significa que la tarea ya existe
       return False #Si no encuentra la tarea retorna False, que significa que la tarea no existe

    def agregar_tarea(self, nueva_tarea): #Metodo de la clase tarea para agregar una nueva tarea
      self.lista_tareas.append(nueva_tarea) #Agrega la tarea a la lista de tareas
      return "Tarea agregada con exito"
    
    def obtener_tarea(self, nombre): #Metodo de la clase tarea para obtener una tarea
        for tarea in self.lista_tareas: #Recorre la lista de tareas
            if tarea.nombre == nombre:  #Si el nombre de la tarea es igual al nombre ingresado
                return True, tarea #Retorna True y la tarea
        return None #Si no encuentra la tarea retorna None
    
    def mostrar_tareas(self): #Metodo de la clase tarea para mostrar todas las tareas
        task_list = [] #Lista vacia
        for tarea in self.lista_tareas: #Recorre la lista de tareas
            task_list.append([tarea.categoria,tarea.nombre,tarea.estado]) #Agrega la tarea a la lista
        if task_list != []:
            return task_list #Retorna la lista de tareas, es una lista de listas con las tareas, en lugar de mandar un objeto de la clase tarea
        #esto, pq tabulate me resulta mas comodo usarlo asi
        else:
            return None
     
    def mostrar_tareas_estado(self, estado): #Metodo de la clase tarea para mostrar las tareas por estado, recibe como argumento, el estado de la tarea que se desee mostrar
        task_list = []
        for tarea in self.lista_tareas: #Recorre la lista de tareas
            if tarea.estado == estado: #Si el estado de la tarea coincide con el estado ingresado
                task_list.append([tarea.categoria,tarea.nombre,tarea.estado]) #Agrega la tarea a la lista
        if task_list != []:
            return task_list
        else:
            return None
        
#Metodo de la clase tarea para mostrar las tareas por categoria       
    def mostrar_tareas_categoria(self, categoria):  #Recibe como argumento, la categoria de la tarea que se desee mostrar
        task_list = []
        for tarea in self.lista_tareas:
            if tarea.categoria == categoria:
                task_list.append([tarea.categoria,tarea.nombre,tarea.estado])
        if task_list != []:
            return task_list
        else:   
            return None
                
#Metodos para modificar tareas
    def cambiar_estado(self, nombre_tarea, estado): #Metodo de la clase TaskTracker  para cambiar el estado de una tarea
        for tarea in self.lista_tareas:
            if tarea.nombre == nombre_tarea:
                tarea.estado = estado
                
    def cambiar_categoria(self, nombre_tarea, categoria): #Metodo de la clase TaskTracker para cambiar la categoria de una tarea
        for tarea in self.lista_tareas:
            if tarea.nombre.replace(" ", "") == nombre_tarea.replace(" ", ""):
                tarea.categoria = categoria
                
    def modificar_tarea(self, nombre_tarea, nueva_tarea):
        for tarea in self.lista_tareas:
            if tarea.nombre.replace(" ", "") == nombre_tarea.replace(" ", ""):
                tarea.nombre = nueva_tarea
             
#Metodo para eliminar tareas   
    def eliminar_tarea(self, nombre_tarea):
        for tarea in self.lista_tareas:
            if tarea.nombre == nombre_tarea:
                self.lista_tareas.remove(tarea)
                return True
        return False
                
_task = Task_Traker()
