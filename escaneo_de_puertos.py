from colorama import Fore, init
import nmap
import os

init()

def limpiar_panatalla():
    os.system('cls' if os.name == 'nt' else 'clear')

nmap = nmap.PortScanner()

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


def get_host():
    while True:
        limpiar_panatalla()
        banner()
        print()

        host = input(Fore.GREEN + "Ingrese la ip o el host a escanear: ")
        try:
            nmap.scan(host, arguments='-sn')
            return host
        except nmap.PortScannerError:
            print(Fore.RED + "Host no valido intentelo de nuevo")
            input(Fore.RED + "Presione enter para continuar")
            continue
        if host:
            main(host)


def main(host):
    print(Fore.GREEN + f"{host}")
    





def quick_scan():
    limpiar_panatalla()
    banner()
    print()


get_host()