from os import system
import time
from colorama import Fore, Back, Style, init
init(autoreset=True) # garantiza que los colores no se propaguen de una línea a otra por error.

def error(mensajer_error): #Función para imprimir mensajes de error en pantalla
    print(Fore.YELLOW + "=" * 60)
    print(Fore.RED + mensajer_error.center(60))
    print(Fore.YELLOW + "=" * 60)
    time.sleep(2)
    system("cls")
    
def imprimir_mensaje(mensaje): #Función para imprimir mensajes y encabezados
    print(Fore.MAGENTA + "✿ " * 26)
    print( Fore.GREEN +mensaje.center(52))
    print(Fore.MAGENTA + "✿ " * 26)