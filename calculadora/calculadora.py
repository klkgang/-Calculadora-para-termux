from colorama import Fore, Back, Style, init
import os
import sys

#llamado a la funcion de colorama
init()

#Limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


#banner de el menu principal
def banner_principal():
    banner = """""

    ██████╗░░█████╗░░█████╗░███╗░░░███╗
    ██╔══██╗██╔══██╗██╔══██╗████╗░████║
    ██████╦╝██║░░██║██║░░██║██╔████╔██║
    ██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║
    ██████╦╝╚█████╔╝╚█████╔╝██║░╚═╝░██║
    ╚═════╝░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝

    Calculadora premium
         By Destro

               """""
    print (Fore.GREEN + banner)


#funcion para sumar
def  calculadora():
    while True:
        try:
            limpiar_pantalla()
            banner_principal()
            
            print()
            print(Fore.YELLOW + "Escriba 'help' para ayuda")
            print()
            print(Fore.GREEN + "Escriba 'exit' para salir")
            print()
            operacion = input(Fore.GREEN + "Ingrese su operacion:")

            if operacion == 'exit':
                sys.exit()


            elif operacion == "help":
                with open('help.txt', 'r') as archivo:
                    limpiar_pantalla()
                    print(archivo.read())

                    print()
                    input(Fore.RED + "Presione enter para continuar")
                    continue


            resultado = eval(operacion)

            if resultado:
                limpiar_pantalla()
                print(Fore.GREEN + "El resultado es: " + str(resultado))
                print()
                input(Fore.RED + "Presione enter para continuar")
                continue

        except Exception:
            input(Fore.RED + "Operacion invalida, presione enter para continuar")
            continue
        


    
    

if __name__ == "__main__":
    calculadora()
