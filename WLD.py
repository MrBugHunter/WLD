from os import system
from colorama import Fore
from subprocess import check_output
system('cls')
print(Fore.GREEN + """
░██╗░░░░░░░██╗░░░░░░██╗░░░░░░░░░░░██████╗░
░██║░░██╗░░██║░░░░░░██║░░░░░░░░░░░██╔══██╗
░╚██╗████╗██╔╝█████╗██║░░░░░█████╗██║░░██║
░░████╔═████║░╚════╝██║░░░░░╚════╝██║░░██║
░░╚██╔╝░╚██╔╝░░░░░░░███████╗░░░░░░██████╔╝
░░░╚═╝░░░╚═╝░░░░░░░░╚══════╝░░░░░░╚═════╝░
Windows Log Deleter

Created By : Mr.Bug Hunter
""")
eventlogs = ['Security' , 'Application' , 'System' , 'Setup', 'Internet Explorer']
for event in eventlogs:
    try:
        check_output(["wevtutil.exe" , "cl" , event.strip("\r")])
        print(Fore.GREEN + "[+] {} Logs Deleted .".format(event))
    except:
        print(Fore.RED + "[-] {} Logs Not Deleted .".format(event))
input(Fore.GREEN + "[+] " + Fore.WHITE + "Press ENTER To Exit ")
