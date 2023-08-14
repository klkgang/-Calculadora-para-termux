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
def sumar():
    limpiar_pantalla()
    print(Fore.CYAN + "=== Opciones ===")

    print()
    print (Fore.BLUE + "1. Sumar numeros enteros")
    print (Fore.BLUE + "2. Sumar nuneros decimales")
    print (Fore.BLUE + "3. Volver a el menu principal")

    print()
    opcion = int(input(Fore.CYAN + "Seleccione una opcion: "))

    if opcion == 1:
        limpiar_pantalla()
        numero1 = int(input(Fore.BLUE + "Num1: "))
        limpiar_pantalla()
        print (Fore.BLUE + "Numero 1 =", str(numero1))

        print()
        numero2 = int(input(Fore.BLUE + "Mas: "))
        resultado = numero1 + numero2
        limpiar_pantalla()

        print (Fore.BLUE + str(numero1), "+", str(numero2), "=", str(resultado))
        input(Fore.YELLOW + "Presione Enter para continuar. ")
        sumar()

    elif opcion == 2:
        limpiar_pantalla()
        numero1= float(input(Fore.BLUE + "Num1: "))
        limpiar_pantalla()
        print (Fore.BLUE + "Numero 1 =", str(numero1))

        print()
        numero2 = float(input(Fore.BLUE + "Mas: "))
        resultado = numero1 + numero2
        limpiar_pantalla()

        print (Fore.BLUE + str(numero1), "+", str(numero2), "=",str(resultado))
        input(Fore.YELLOW + "Presione Enter para continuar. ")
        sumar()

    elif opcion == 3:
        menu_princiapal()

    else:
        print (Fore.RED + "Opcion no valida")
        input(Fore.GREEN + "Presione Enter para continuar ")
        sumar()
#funcion para restar
def restar():
    limpiar_pantalla()
    print (Fore.CYAN + "=== Opciones ===")

    print()
    print (Fore.BLUE + "1. Restar numeros enteros")
    print (Fore.BLUE + "2. Restar numeros decimales")
    print (Fore.BLUE + "3. Volver a el menu principal")

    print()
    opcion = int(input(Fore.CYAN + "Seleccione una opcion "))

    if opcion == 1:
        limpiar_pantalla()
        numero1 = int(input(Fore.BLUE + "Num1: "))
        limpiar_pantalla()
        print (Fore.BLUE +"Numero 1 =", str(numero1))

        print()
        numero2 = int(input(Fore.BLUE + "Menos: "))
        resultado = numero1 - numero2
        limpiar_pantalla()

        print (Fore.BLUE + str(numero1), "-", str(numero2), "=", str(resultado))
        input(Fore.YELLOW + "Presione Enter para continuar. ")
        restar()

    elif opcion == 2:
        limpiar_pantalla()
        numero1= float(input(Fore.BLUE + "Num1: "))
        limpiar_pantalla()
        print (Fore.BLUE + "Numero 1 =", str(numero1))

        print()
        numero2 = float(input(Fore.BLUE + "Menos: "))
        resultado = numero1 - numero2
        limpiar_pantalla()

        print (Fore.BLUE + str(numero1), "-", str(numero2), "=", str(resultado))
        input(Fore.YELLOW + "Presione Enter para continuar. ")
        restar()

    elif opcion == 3:
        menu_princiapal()

    else:
        print ("opcion no valida")
        input("Presione Enter para continuar ")
        restar()
#funcion de dividir
def dividir():
    limpiar_pantalla()
    print (Fore.CYAN + "=== Opciones ===")

    print()
    print (Fore.BLUE + "1. Dividir numeros enteros")
    print (Fore.BLUE + "2. Dividir numeros decimales")
    print (Fore.BLUE + "3. Volver a el menu principal")

    print()
    opcion = int(input(Fore.CYAN + "Seleccione una opcion: "))

    if opcion == 1:
        limpiar_pantalla()
        numero1 = int(input(Fore.BLUE + "Num1: "))
        limpiar_pantalla()
        print (Fore.BLUE + "Numero 1 =", str(numero1))

        print()
        numero2 = int(input("Dividido entre: "))
        resultado = numero1 // numero2
        limpiar_pantalla()

        print (Fore.BLUE + str(numero1), "÷", str(numero2), "=", str(resultado))
        input(Fore.YELLOW + "Presione Enter para continuar. ")
        dividir()

    elif opcion == 2:
        limpiar_pantalla()
        numero1= float(input("Num1: "))
        limpiar_pantalla()
        print (Fore.BLUE + "Numero 1 =", numero1)

        print()
        numero2 = float(input(Fore.BLUE + "Dividido entre: "))
        resultado = round(numero1 / numero2, 2)
        limpiar_pantalla()

        print (Fore.BLUE + str(numero1), "÷", str(numero2), "=", str(resultado))
        input(Fore.YELLOW + "Presione Enter para continuar. ")
        dividir()

    elif opcion == 3:
        menu_princiapal()

    else:
        print (Fore.RED + "opcion no valida")
        input(Fore.YELLOW + "Presione Enter para continuar ")
        dividir()
#funcion de multiplicar
def multiplicar():
    limpiar_pantalla()
    print (Fore.CYAN + "=== Opciones ===")

    print()
    print (Fore.BLUE + "1. Multiplicar numeros enteros")
    print (Fore.BLUE + "2. Multiplicar numeros decimales")
    print (Fore.BLUE + "3. Volver a el menu principal")

    print()
    opcion = int(input(Fore.CYAN + "Seleccione una opcion: "))


    if opcion == 1:
        limpiar_pantalla()
        numero1 = int(input(Fore.BLUE + "Num1: "))
        limpiar_pantalla()
        print (Fore.BLUE + "Numero 1 =", str(numero1))

        print()
        numero2 = int(input(Fore.BLUE + "Multiplicado por: "))
        resultado = numero1 * numero2
        limpiar_pantalla()

        print (Fore.BLUE + str(numero1), "x", str(numero2), "=", str(resultado))
        input(Fore.YELLOW + "Presione Enter para continuar. ")
        multiplicar()

    elif opcion == 2:
        limpiar_pantalla()
        numero1= float(input(Fore.BLUE + "Num1: "))
        limpiar_pantalla()
        print (Fore.BLUE + "Numero 1 =", str(numero1))

        print()
        numero2 = float(input(Fore.BLUE + "Multiplicado por: "))
        resultado = round(numero1 * numero2, 2)
        limpiar_pantalla()

        print (Fore.BLUE + str(numero1), "x", str(numero2), "=", str(resultado))
        input(Fore.YELLOW + "Presione Enter para continuar. ")
        multiplicar()

    elif opcion == 3:
        menu_princiapal()

    else:
        print (Fore.RED + "opcion no valida")
        input(Fore.YELLOW + "Presione Enter para continuar ")
        multiplicar()
#el menu principal
def menu_princiapal():
    limpiar_pantalla()
    banner_principal()

    print()
    print (Fore.BLUE + "Opciones:")
    print (Fore.BLUE + "1. Sumar")
    print (Fore.BLUE + "2. Restar")
    print (Fore.BLUE + "3. Dividir")
    print (Fore.BLUE + "4. Multiplicar")
    print (Fore.BLUE + "5. Salir")
    print()
    opcion= int(input(Fore.CYAN + "Seleccione una opcion: "))

    if opcion == 1:
        sumar()

    elif opcion == 2:
        restar()

    elif opcion == 3:
        dividir()

    elif opcion == 4:
        multiplicar()

    elif opcion == 5:
        print (Fore.RED + "Cerrando script.....")
        input(Fore.YELLOW +"Presione enter para continuar")
        sys.exit()


    else:
        print(Fore.RED + "Opcion no valida.")
        input(Fore.YELLOW + "Presione Enter para continuar ")
        limpiar_pantalla()
        menu_princiapal()



if __name__ == "__main__":
    menu_princiapal()
