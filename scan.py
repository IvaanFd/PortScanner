import os
import colorama
from colorama import Fore, Style
from pyfiglet import Figlet
import nmap

fig = Figlet(font='small')

colorama.init()


def clear_terminal():

    if os.name == 'posix':  # Linux
        os.system('clear')

    elif os.name == 'nt':  # Windows
        os.system('cls')

    else:
        print("The operating system could not be determined")


def scan():
    pass


def main():

    clear_terminal()

    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + fig.renderText("Port Scanning") +
          "\n--------------- Code By @IvanFdez2001 ---------------" + Fore.RESET)
    print("\n")

    ip = input("Enter the IP address on which you want the scan to be performed: ")

    nm = nmap.PortScanner()
    r = nm.scan(hosts=ip, arguments="-p- -sS -sC -sV --min-rate 5000 -vvv -n")

    print("\n" + Fore.BLUE + "Host: " +
          Fore.LIGHTRED_EX + ip + Fore.RESET)
    print(Fore.BLUE + "State: " +
          Fore.LIGHTRED_EX + nm[ip].state() + Fore.RESET)

    for protocol in nm[ip].all_protocols():

        print("\n----------------------------------------------------------------")
        print(Fore.BLUE + "Protocol: " +
              Fore.LIGHTRED_EX + protocol + Fore.RESET)

        lport = nm[ip][protocol].keys()
        sorted(lport)

        for port in lport:
            print("\t Port: %s \t State: %s \t Service: %s" %
                  (port, nm[ip][protocol][port]["state"], nm[ip][protocol][port]["name"]))

    print()


main()
