try:
	import requests as req
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
	
	{}{}( ! ) ADMIN FINDER, MULTI PATH!
	{}""".format(hij,bkun,mer,reset)
	print(banner)
	
	
def CekAdmin(site):

	site = i.strip()
	
	try:
		path = ["/admin", "/panel", "/admin/login.php", "/administrator"] # tambahin sendiri
		if 'http://' or 'https://' in site:
			for cok in path:
				cek_status = req.get(site+cok)
				if '200' in str(cek_status.status_code):
					print(Fore.GREEN+site+cok+' 200 FOUND')
					open("result.txt", 'a').write(site+cok+"\n")
					continue
				elif '404' in str(cek_status.status_code):
					print(Fore.RED+site+cok+' 404 NOT FOUND')
				elif '403' in str(cek_status.status_code):
					print(Fore.RED+site+cok+' 403 FORBBIDEN')
		elif not 'http://' or 'https://':
			print(Fore.RED+'ADD HTTP/HTTPS IN URL')
	except:
		pass

ngocok()
list = str(input("Domain List -> "))

try:
	with open(list) as f:
		for i in f:
			CekAdmin(i)
			
except IOError as err:
	print("Error Brader " + str(err))
