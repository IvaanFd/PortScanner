import os
import sys
import colorama
from colorama import Fore, Style
from pyfiglet import Figlet
import nmap

opened_ports = []

fig = Figlet(font='small')

colorama.init()


def clear_terminal():

    if os.name == 'posix':  # Linux
        os.system('clear')

    elif os.name == 'nt':  # Windows
        os.system('cls')

    else:
        print("The operating system could not be determined")


def scan(only_port, ip, command):

    global opened_ports

    if only_port == True:
        opened_ports.clear()

    nm = nmap.PortScanner()

    print("\n" + Fore.GREEN + "[+] Scanning... " + Fore.RESET)

    nm.scan(hosts=ip, arguments=command)

    print("\n" + Fore.BLUE + "Host: " +
          Fore.LIGHTRED_EX + ip + Fore.RESET)

    try:
        print(Fore.BLUE + "State: " +
              Fore.LIGHTRED_EX + nm[ip].state() + Fore.RESET)

        if only_port == True:

            for protocol in nm[ip].all_protocols():

                print(
                    "\n----------------------------------------------------------------")
                print(Fore.BLUE + "Protocol: " +
                      Fore.LIGHTRED_EX + protocol + Fore.RESET)

                lport = nm[ip][protocol].keys()
                sorted(lport)

                for port in lport:
                    print("\n\t Port: %s \t State: %s \n" %
                          (port, nm[ip][protocol][port]["state"]))

                    if nm[ip][protocol][port]["state"] == "open":
                        opened_ports.append(str(port))

        else:

            opened_ports.clear()

            print("\n" + Fore.GREEN +
                  "The scan report can be found in the file called scan.txt" + Fore.RESET)

    except:
        print(Fore.BLUE + "State: " +
              Fore.LIGHTRED_EX + "down or no opened ports" + Fore.RESET)


def port_scanning(target_ip):

    while True:

        print("\n" + Fore.CYAN + "Port scanning menu:")
        print("1. Perform silent but slow scanning")
        print("2. Perform noisy but fast scanning")
        print("3. Perform normal scanning")
        print("4. Exit")

        try:
            option = int(input("Select an option (1-4): " + Fore.RESET))

            if option == 1:
                scan(True, target_ip, "-p- --open -T2 -sS -Pn -f")

                continue_scan = input(
                    "The port scan is over, would you like to perform a more complete scan? [y/n]: " + Fore.RESET)
                if str.lower(continue_scan) == "y":
                    port_version_scanning(target_ip)
                else:
                    break

            elif option == 2:
                scan(True, target_ip, "-p- --open -min-rate 5000 -T4 -sS -Pn")

                continue_scan = input(
                    "The port scan is over, would you like to perform a more complete scan? [y/n]: " + Fore.RESET)
                if str.lower(continue_scan) == "y":
                    port_version_scanning(target_ip)
                else:
                    break

            elif option == 3:
                scan(True, target_ip, "-p- --open")

                continue_scan = input(
                    "The port scan is over, would you like to perform a more complete scan? [y/n]: " + Fore.RESET)
                if str.lower(continue_scan) == "y":
                    port_version_scanning(target_ip)
                else:
                    break

            elif option == 4:
                print("\n" + Fore.BLUE +
                      "Leaving port scanning menu" + Fore.RESET)
                break
            else:
                print(
                    "\n" + Fore.LIGHTRED_EX + "Invalid option. Please choose an option from 1 to 4" + Fore.RESET)

        except ValueError:
            print("\n" + Fore.LIGHTRED_EX +
                  "Error: Enter a whole number" + Fore.RESET)


def port_version_scanning(target_ip):

    global opened_ports

    while True:

        print("\n" + Fore.CYAN + "Port and version scanning menu:")
        print("1. Perform silent but slow scanning")
        print("2. Perform noisy but fast scanning")
        print("3. Perform normal scanning")
        print("4. Exit")

        try:
            option = int(input("Select an option (1-4): " + Fore.RESET))

            if option == 1:
                if (len(opened_ports) == 0):
                    scan(False, target_ip,
                         "-p- --open -T2 -sS -sC -sV -Pn -f -oN scan.txt")
                else:
                    ports = ",".join(opened_ports)
                    scan(False, target_ip,
                         f"-p{ports} -T2 -sS -sC -sV -Pn -f -oN scan.txt")
                    break
            elif option == 2:
                if (len(opened_ports) == 0):
                    scan(False, target_ip,
                         "-p- --open -min-rate 5000 -T4 -sS -sC -sV -Pn -oN scan.txt")
                else:
                    ports = ",".join(opened_ports)
                    scan(False, target_ip,
                         f"-p{ports} -min-rate 5000 -T4 -sS -sC -sV -Pn -oN scan.txt")
                    break
            elif option == 3:
                if (len(opened_ports) == 0):
                    scan(False, target_ip,
                         "-p- --open -sC -sV -oN scan.txt")
                else:
                    ports = ",".join(opened_ports)
                    scan(False, target_ip,
                         f"-p{ports} -sC -sV -oN scan.txt")
                    break
            elif option == 4:
                print("\n" + Fore.BLUE +
                      "Leaving port scanning menu" + Fore.RESET)
                break
            else:
                print(
                    "\n" + Fore.LIGHTRED_EX + "Invalid option. Please choose an option from 1 to 4" + Fore.RESET)

        except ValueError:
            print("\n" + Fore.LIGHTRED_EX +
                  "Error: Enter a whole number" + Fore.RESET)


def main():

    clear_terminal()

    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + fig.renderText("Port Scanning") +
          "\n--------------- Code By @IvaanFd ---------------" + Fore.RESET)

    if len(sys.argv) != 2:
        print("\n" + Fore.LIGHTRED_EX +
              "Usage: python3 scan.py <target>" + Fore.RESET)
        sys.exit(1)

    target_ip = sys.argv[1]

    while True:

        print("\n" + Fore.YELLOW + "Menu:")
        print("1. Port Scanning")
        print("2. Port and Version Scanning")
        print("3. Exit")

        try:
            option = int(input("Select an option (1-3): " + Fore.RESET))

            if option == 1:
                port_scanning(target_ip)
            elif option == 2:
                port_version_scanning(target_ip)
            elif option == 3:
                print("\n" + Fore.BLUE +
                      "Leaving the program, see you later!" + Fore.RESET)
                break
            else:
                print(
                    "\n" + Fore.LIGHTRED_EX + "Invalid option. Please choose an option from 1 to 3" + Fore.RESET)

        except ValueError:
            print("\n" + Fore.LIGHTRED_EX +
                  "Error: Enter a whole number" + Fore.RESET)


main()
