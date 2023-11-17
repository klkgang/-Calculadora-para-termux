from colorama import Fore, init
import nmap
import os

init()

def limpiar_panatalla():
    os.system('cls' if os.name == 'nt' else 'clear')

scanner = nmap.PortScanner()

def banner():
    banner = """
    
  ██████  ▒█████    █████▒██▓ ▄▄▄      
▒██    ▒ ▒██▒  ██▒▓██   ▒▓██▒▒████▄    
░ ▓██▄   ▒██░  ██▒▒████ ░▒██▒▒██  ▀█▄  
  ▒   ██▒▒██   ██░░▓█▒  ░░██░░██▄▄▄▄██ 
▒██████▒▒░ ████▓▒░░▒█░   ░██░ ▓█   ▓██▒
▒ ▒▓▒ ▒ ░░ ▒░▒░▒░  ▒ ░   ░▓   ▒▒   ▓▒█░
░ ░▒  ░ ░  ░ ▒ ▒░  ░      ▒ ░  ▒   ▒▒ ░
░  ░  ░  ░ ░ ░ ▒   ░ ░    ▒ ░  ░   ▒   
      ░      ░ ░          ░        ░  ░
                                       

    """
    print(Fore.GREEN + banner)

def main_menu(host):
    while True:
        limpiar_panatalla()
        print(f"{Fore.YELLOW}Host: {Fore.GREEN}{host}\n")
        print(Fore.YELLOW + "Selecciona una opcion: ")
        print(Fore.GREEN + "[1] Escanear puertos")
        print(Fore.GREEN + "[2] Salir\n")

        option = input(Fore.GREEN + ">>> ")
        if option == "1":
            scan_ports(host)
        elif option == "2":
            exit()
        else:
            print(Fore.RED + "Opcion invalida. Por favor, selecciona una opcion valida.")
            input(Fore.YELLOW + "Presiona enter para continuar")

# Escanear puertos
def scan_ports(host):
    try:
        limpiar_panatalla()
        banner()
        print(Fore.YELLOW + f"Escanenado puertos para el host: {host}")
        resultado = scanner.scan(host, arguments='-p-')  # Remove 'host='
        print(Fore.GREEN + "Resultado:")
        for protocol in resultado[host].all_protocols():
            print(Fore.YELLOW + f"Protocolo : {protocol}")
            lport = resultado[host][protocol].keys()
            for port in lport:
                print (Fore.GREEN + f"Port : {port}, State : {resultado[host][protocol][port]['state']}")
        input(Fore.YELLOW + "Presiona enter para continuar")
        main_menu(host)
    except nmap.PortScannerError:  # Remove 'scanner.'
        print(Fore.RED + "Error al intentar escanear puertos")
        input(Fore.YELLOW + "Presiona enter para continuar")
        main_menu(host)

# Obtener el host del usuario
def get_host():
    while True:
        try:
            limpiar_panatalla()
            banner()
            print(Fore.YELLOW + "Ingresa la IP del host a escanear: ")
            host = input(Fore.GREEN + ">>> ")
            resultado = scanner.scan(host, arguments='-sn')
            if 'error' in resultado['nmap']['scaninfo']:
                print(Fore.RED + "Error al intentar conectar con el host")
                print(Fore.RED + "Verifica que la IP o host sea correcta")
                input(Fore.YELLOW + "Presiona enter para continuar")
            else:
                print(Fore.GREEN + "Host encontrado!")
                input(Fore.YELLOW + "Presiona enter para continuar")
                return host
        except nmap.PortScannerError:
            print(Fore.RED + "Error al intentar conectar con el host")
            print(Fore.RED + "Verifica que la IP o host sea correcta")
            input(Fore.YELLOW + "Presiona enter para continuar")

if __name__ == "__main__":
    host = get_host()
    main_menu(host)