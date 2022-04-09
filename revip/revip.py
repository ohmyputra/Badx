M=open
E=str
C=print
try:import requests as G,os as D;from colorama import Fore as A,Style,Back as B
except ImportError as H:C('Import error brader '+E(H))
def I():E='clear';F='cls';D.system([E,F][D.name=='nt']);G=A.RED;H=A.GREEN;L=A.YELLOW;M=B.RED;N=B.GREEN;I=B.YELLOW;J=Style.RESET_ALL;K='\n\t{}_______                   __  __    __ \n\t/       \\                 /  |/  |  /  |\n\t$$$$$$$  |  ______    ____$$ |$$ |  $$ |\n\t$$ |__$$ | /      \\  /    $$ |$$  \\/$$/ \n\t$$    $$<  $$$$$$  |/$$$$$$$ | $$  $$<  \n\t$$$$$$$  | /    $$ |$$ |  $$ |  $$$$  \\ \n\t$$ |__$$ |/$$$$$$$ |$$ \\__$$ | $$ /$$  |\n\t$$    $$/ $$    $$ |$$    $$ |$$ |  $$ |\n\t$$$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/     \n\t\n\t{}{}( ! ) REVERSE IP\n\t{}'.format(H,I,G,J);C(K)
def J(site):
	B=site;B=F.strip()
	try:
		if'http://'or'https://'or'/'not in B:
			D=G.get('https://api.hackertarget.com/reverseiplookup/?q='+E(B)).text
			if'.'in D:C(A.GREEN+f"{B} : OK");M('resultrev.txt','a').write(D+'\n')
			elif'error check your search parameter'in D:C(A.RED+f"{B} : error check your search parameter")
			elif'No DNS A records found'in D:C(A.RED+f"{B} : No DNS A records found")
			else:C(A.RED+f"{B} API count exceeded - Increase Quota with Membership")
	except:pass
I()
list=E(input('IP OR DOMAIN List -> '))
try:
	with M(list)as K:
		for F in K:J(F)
except IOError as L:C('Error Brader '+E(L))
