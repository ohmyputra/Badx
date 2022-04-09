M=open
D=str
C=print
try:import requests as H,os as E;from colorama import Fore as A,Style,Back as B
except ImportError as F:C('Import error brader '+D(F))
def I():D='clear';F='cls';E.system([D,F][E.name=='nt']);G=A.RED;H=A.GREEN;L=A.YELLOW;M=B.RED;N=B.GREEN;I=B.YELLOW;J=Style.RESET_ALL;K='\n\t{}_______                   __  __    __ \n\t/       \\                 /  |/  |  /  |\n\t$$$$$$$  |  ______    ____$$ |$$ |  $$ |\n\t$$ |__$$ | /      \\  /    $$ |$$  \\/$$/ \n\t$$    $$<  $$$$$$  |/$$$$$$$ | $$  $$<  \n\t$$$$$$$  | /    $$ |$$ |  $$ |  $$$$  \\ \n\t$$ |__$$ |/$$$$$$$ |$$ \\__$$ | $$ /$$  |\n\t$$    $$/ $$    $$ |$$    $$ |$$ |  $$ |\n\t$$$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/     \n\t\n\t{}{}( ! ) ADMIN FINDER, MULTI PATH!\n\t{}'.format(H,I,G,J);C(K)
def J(site):
	K='https://';J='http://';B=site;B=G.strip()
	try:
		I=['/admin','/panel','/admin/login.php','/administrator']
		if J or K in B:
			for E in I:
				F=H.get(B+E)
				if'200'in D(F.status_code):C(A.GREEN+B+E+' 200 FOUND');M('result.txt','a').write(B+E+'\n');continue
				elif'404'in D(F.status_code):C(A.RED+B+E+' 404 NOT FOUND')
				elif'403'in D(F.status_code):C(A.RED+B+E+' 403 FORBBIDEN')
		elif not J or K:C(A.RED+'ADD HTTP/HTTPS IN URL')
	except:pass
I()
list=D(input('Domain List -> '))
try:
	with M(list)as K:
		for G in K:J(G)
except IOError as L:C('Error Brader '+D(L))
