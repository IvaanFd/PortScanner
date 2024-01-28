# PortScanner

Python script that performs a scan of open ports on a specific IP address.

Permissions must be given or the script must be run as sudo for it to work properly.

# Necessary dependences

* Nmap: pip install python-nmap
* Pyfiglet: pip install pyfiglet

# PortScanner

First, we execute the script indicating the IP address of the machine, otherwise the script will not be executed.

![1706441303190](image/README/1706441303190.png)

![1706441274727](image/README/1706441274727.png)

-----------------------------------------------

![1706441341158](image/README/1706441341158.png)

![1706441355967](image/README/1706441355967.png)


Once executed, by entering an IP address, you will be presented with a menu that will allow you to choose between two options. The first option will perform a scan of the open ports only, while the second option will perform a scan of the open ports and obtain information about the versions of the services associated with those ports.

![1706441444996](image/README/1706441444996.png)


For both options, choosing each option brings up another menu that allows you to specify whether you prefer to perform a quieter but slower scan, a faster but noisier scan, or opt for a normal scan.

![1706441548742](image/README/1706441548742.png)

![1706441563612](image/README/1706441563612.png)


As a last detail, after completing an exclusive scan of the open ports, a message appears offering the option to perform a more complete scan. If you accept this option, you will access the corresponding menu to perform the port and version scan.

![1706441720695](image/README/1706441720695.png)


If you choose to scan only the open ports, the report will be presented directly. On the other hand, if you opt for a more complete scan, the report will be saved to a file.

![1706441816723](image/README/1706441816723.png)

![1706441828819](image/README/1706441828819.png)
