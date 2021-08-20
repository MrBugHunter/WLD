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

Telegram  ID 1 : @bug_hunter_us
Telegram  ID 2 : @Mr_Bug_HunTer
Instagram ID   : mr_bug_hunter
""")
eventlogs = ['Security' , 'Application' , 'System' , 'Setup', 'Internet Explorer']
for event in eventlogs:
    try:
        check_output(["wevtutil.exe" , "cl" , event.strip("\r")])
        print(Fore.GREEN + "[+] {} Logs Deleted .".format(event))
    except:
        print(Fore.RED + "[-] {} Logs Not Deleted .".format(event))
input(Fore.GREEN + "[+] " + Fore.WHITE + "Press ENTER To Exit ")
