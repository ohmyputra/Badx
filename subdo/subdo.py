N=open
E=str
C=print
try:import requests as H,os as D;from colorama import Fore as A,Style as F,Back as B
except ImportError as I:C('Import error brader '+E(I))
O=B.YELLOW
P=F.RESET_ALL
def J():E='clear';G='cls';D.system([E,G][D.name=='nt']);H=A.RED;I=A.GREEN;M=A.YELLOW;N=B.RED;O=B.GREEN;J=B.YELLOW;K=F.RESET_ALL;L='\n\t{}_______                   __  __    __ \n\t/       \\                 /  |/  |  /  |\n\t$$$$$$$  |  ______    ____$$ |$$ |  $$ |\n\t$$ |__$$ | /      \\  /    $$ |$$  \\/$$/ \n\t$$    $$<  $$$$$$  |/$$$$$$$ | $$  $$<  \n\t$$$$$$$  | /    $$ |$$ |  $$ |  $$$$  \\ \n\t$$ |__$$ |/$$$$$$$ |$$ \\__$$ | $$ /$$  |\n\t$$    $$/ $$    $$ |$$    $$ |$$ |  $$ |\n\t$$$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/     \n\t\n\t{}{}( ! ) SUBDOMAIN ENUMERATION\n\t{}'.format(I,J,H,K);C(L)
def K(site):
	B=site;B=G.strip()
	try:
		if'http://'or'https://'or'/'not in B:
			D=H.get('https://sonar.omnisint.io/subdomains/'+E(B)).text
			if'["'in D:C(A.GREEN+f"{B} : FOUND");N('resultsubdo.txt','a').write(D+'\n')
			elif'{"error":"no results found"}'in D:C(A.RED+f"{B} {'error':'no results found'}")
			elif'[]'in D:C(A.RED+f"{B} ['null']")
			else:C(A.RED+f"{B}")
	except:pass
J()
list=E(input('Domain List -> '))
try:
	with N(list)as L:
		for G in L:K(G)
except IOError as M:C('Error Brader '+E(M))
