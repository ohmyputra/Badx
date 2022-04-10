try:
	import os
	import socket
	import os as root
	from colorama import Fore, Back, Style
	import time
except ModuleError as e:
	print("Module Error :",e)
	
	
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
	
	{}{}( ! ) OPEN PORT SCANNER. Default Port : 80, Edit Manual Port On Source Code !
	{}""".format(hij,bkun,mer,reset)
	print(banner)
	
	
def balik():
	root.system('python openport.py')

def cek(ip,port=80): # Edit Port
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(2) #2 Second Timeout
		result = sock.connect_ex((ip,port))
		if result == 0:
			root.system('clear')
			print(Fore.YELLOW+'CHECKING PORT.....\n')
			time.sleep(2)
			print(Fore.GREEN+'STATUS PORT : OPEN\n')
			while True:
				back = input("Cek Lagi? Y/N : ")
				if back == 'Y':
					balik()
				elif back == 'N':
					break
				
		else:
			root.system('clear')
			print(Fore.YELLOW+'CHECKING PORT.....\n')
			time.sleep(2)
			print(Fore.RED+'port CLOSED, connect_ex returned: '+str(result))
			while True:
				back = input("Cek Lagi? Y/N : ")
				if back == 'Y':
					balik()
				elif back == 'N':
					break

	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	ngocok()
	ip = input("Enter IP : ")
	cek(ip)
