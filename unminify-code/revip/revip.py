try:
	import requests as meq
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
	
	{}{}( ! ) REVERSE IP
	{}""".format(hij,bkun,mer,reset)
	print(banner)
	
	
def GetResults(site):
	site = i.strip()
	try:
		if 'http://' or 'https://' or '/' not in site:
			getdomain = meq.get('https://api.hackertarget.com/reverseiplookup/?q='+str(site)).text
			if '.' in getdomain:
				print(Fore.GREEN+f"{site} : OK")
				open("resultrev.txt", 'a').write(getdomain + "\n")
			elif 'error check your search parameter' in getdomain:
				print(Fore.RED+f"{site} : error check your search parameter")
			elif 'No DNS A records found' in getdomain:
				print(Fore.RED+f"{site} : No DNS A records found")
			else:
				print(Fore.RED+f"{site} API count exceeded - Increase Quota with Membership")
	except:
		pass
ngocok()
list = str(input("IP OR DOMAIN List -> "))
try:
	with open(list) as f:
		for i in f:
			GetResults(i)
			
except IOError as err:
	print("Error Brader " + str(err))
