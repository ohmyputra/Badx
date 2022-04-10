
# Import Module
try:

	import os as root
	import time as jeda
	import requests as req
	from colorama import Fore, Back, Style
	from rich.console import Console
	from rich.table import Table
	
except ImportError as e:
	print("Gagal Import Module, Install modulenya : ", e)

console = Console()


# Variable Warna

mer = Fore.RED
hij = Fore.GREEN
kun = Fore.YELLOW

# Variable Warna Background

bmer = Back.RED
bhij = Back.GREEN
bkun = Back.YELLOW

# Reset All Style Warna

reset = Style.RESET_ALL
	
# Banner

banner = """
 {}_______                   __  __    __ 
/       \                 /  |/  |  /  |
$$$$$$$  |  ______    ____$$ |$$ |  $$ |
$$ |__$$ | /      \  /    $$ |$$  \/$$/ 
$$    $$<  $$$$$$  |/$$$$$$$ | $$  $$<  
$$$$$$$  | /    $$ |$$ |  $$ |  $$$$  \ 
$$ |__$$ |/$$$$$$$ |$$ \__$$ | $$ /$$  |
$$    $$/ $$    $$ |$$    $$ |$$ |  $$ |
$$$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/     
   
{}{}( ! ) BadX Tools | Exploit 4Fun!
{}""".format(hij,bkun,mer,reset)


# Fungsi Clear Layar
def bersih():
	linux = 'clear'
	windows = 'cls'
	
	root.system([linux,windows][root.name == 'nt'])

# Fungsi Banner

def slog():
	bersih()
	print(banner)
	
def mainmenus():
	slog()
	# table 1
	table = Table(title="Domain Tools", show_header=True, header_style="bold green")
	table.add_column("No.", style="dim", width=12)
	table.add_column("Tools")
	
	# rows table 1
	
	table.add_row("1","Domain To IP")
	table.add_row("2","Reverse IP")
	table.add_row("3","Subdomain Enumerate")
	table.add_row("4","Open Port Check")
	table.add_row("5","Admin Finder")
	
	console.print(table)
	
	
	pilih = str(input("{}Select Tools -> {}".format(mer,reset)))
	
	if pilih == "1":
		root.system("cd toip/;python toip.py")
	elif pilih == "2":
		root.system("cd revip/;python revip.py")
	elif pilih == "3":
		root.system("cd subdo/;python subdo.py")
	elif pilih == "4":
		root.system("cd opport/;python openport.py")
	elif pilih == "5":
		root.system("cd admin/;python admin.py")
	
mainmenus()
