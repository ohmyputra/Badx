try:
	import socket
	import os as root
	from colorama import Fore, Style, Back
	
except ImportError as e:
	print("Import error brader " + str(e))

def ngocok():
	linux = 'clear'
	windows = 'cls'
	
	root.system([linux,windows][root.name == 'nt'])
	
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
	
	{}{}( ! ) DOMAIN TO IP!
	{}""".format(hij,bkun,mer,reset)
	print(banner)
	
	
def GetIP(site):
	site = i.strip()
	try:
		if 'http://' not in site:
			get1 = socket.gethostbyname(site)
			print(Fore.GREEN+f"IP :", get1)
			open("result.txt", 'a').write(get1 + "\n")
		
		
		elif 'http://' or 'https://' in site:
			rep = site.replace('http://', '').replace('https://', '').replace('/', '')
			get2 = socket.gethostbyname(rep)
			print(Fore.GREEN+f"IP :", get2)
			open("result.txt", 'a').write(get2 + "\n")
			
	except:
		pass

ngocok()
list = str(input("Domain List -> "))

try:
	with open(list) as f:
		for i in f:
			GetIP(i)
			
except IOError as err:
	print("Error Brader " + str(err))
