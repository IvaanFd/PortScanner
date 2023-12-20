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

    ip = input(
        "\nEnter the IP address on which you want the scan to be performed: ")

    print("\n" + Fore.GREEN + "[+] Escanenado... " + Fore.RESET)
    
    nm = nmap.PortScanner()
    
    # Slower and slient scan => -p- -T2 -sS -Pn -f
    nm.scan(hosts=ip, arguments="-p- --open --min-rate 5000 -T4 -sS -Pn -n -v")

    print("\n" + Fore.BLUE + "Host: " +
          Fore.LIGHTRED_EX + ip + Fore.RESET)
    print(Fore.BLUE + "State: " +
          Fore.LIGHTRED_EX + nm[ip].state() + Fore.RESET)

    opened_ports = []
    for protocol in nm[ip].all_protocols():

        print("\n----------------------------------------------------------------")
        print(Fore.BLUE + "Protocol: " +
              Fore.LIGHTRED_EX + protocol + Fore.RESET)

        lport = nm[ip][protocol].keys()
        sorted(lport)

        for port in lport:
            print("\n\t Port: %s \t State: %s \n" %
                  (port, nm[ip][protocol][port]["state"]))

            if nm[ip][protocol][port]["state"] == "open":
                opened_ports.append(str(port))

    # Indicate a command for obtening more info about only the opened ports and safe the scan on a file
    if len(opened_ports) > 0:
        print("\n Use the next command for more information about the opened ports: nmap -sC -sV --min-rate 5000 -vvv -n -p%s %s -oN scan.txt" %
              (",".join(opened_ports), ip))
    else:
    	print("The machine %s does not have any port open" % (ip))

    print("\n")


def main():

    clear_terminal()

    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + fig.renderText("Port Scanning") +
          "\n--------------- Code By @IvanFdez2001 ---------------" + Fore.RESET)

    scan()


main()
