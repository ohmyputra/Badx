try:
	import requests as meq
	import os as root
	from colorama import Fore, Style, Back
	
except ImportError as e:
	print("Import error brader " + str(e))
	
BACKYELLOW = Back.YELLOW
RESET = Style.RESET_ALL

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
	
	{}{}( ! ) SUBDOMAIN ENUMERATION
	{}""".format(hij,bkun,mer,reset)
	print(banner)
	
	
def GetSubdo(site):
	site = i.strip()
	try:
		if 'http://' or 'https://' or '/' not in site:
			getsubdo = meq.get('https://sonar.omnisint.io/subdomains/'+str(site)).text
			if '["' in getsubdo:
				print(Fore.GREEN+f"{site} : FOUND")
				open("resultsubdo.txt", 'a').write(getsubdo + '\n')
			elif '{"error":"no results found"}' in getsubdo:
				print(Fore.RED+f"{site} {'error':'no results found'}")
			elif '[]' in getsubdo:
				print(Fore.RED+f"{site} ['null']")
			else:
				print(Fore.RED+f"{site}")
	except:
		pass
ngocok()
list = str(input("Domain List -> "))
try:
	with open(list) as f:
		for i in f:
			GetSubdo(i)
			
except IOError as err:
	print("Error Brader " + str(err))
