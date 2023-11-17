from colorama import Fore, init 
import subprocess

init()

while True:
    print("WELCOME")

    print()
    print(Fore.GREEN + "1. netwworking tool")
    print("2. calculadora")
    print("3. salir")

    print("seleccione una opcion")
    opcion = input(">>> ")

    if opcion == "1":
        subprocess.call(["python", "networking/escaneo_de_puertos.py"])

    elif opcion == "2":
        subprocess.call(["python", "calculadora/calculadora.py"])

    elif opcion == "3":
        break

