H=open
G=str
C=print
try:import socket as D,os as E;from colorama import Fore as A,Style,Back as B
except ImportError as I:C('Import error brader '+G(I))
def J():D='clear';F='cls';E.system([D,F][E.name=='nt']);G=A.RED;H=A.GREEN;L=A.YELLOW;M=B.RED;N=B.GREEN;I=B.YELLOW;J=Style.RESET_ALL;K='\n\t{}_______                   __  __    __ \n\t/       \\                 /  |/  |  /  |\n\t$$$$$$$  |  ______    ____$$ |$$ |  $$ |\n\t$$ |__$$ | /      \\  /    $$ |$$  \\/$$/ \n\t$$    $$<  $$$$$$  |/$$$$$$$ | $$  $$<  \n\t$$$$$$$  | /    $$ |$$ |  $$ |  $$$$  \\ \n\t$$ |__$$ |/$$$$$$$ |$$ \\__$$ | $$ /$$  |\n\t$$    $$/ $$    $$ |$$    $$ |$$ |  $$ |\n\t$$$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/     \n\t\n\t{}{}( ! ) DOMAIN TO IP!\n\t{}'.format(H,I,G,J);C(K)
def K(site):
	O='https://';N='\n';M='a';L='result.txt';J='';I='http://';B=site;B=F.strip()
	try:
		if I not in B:E=D.gethostbyname(B);C(A.GREEN+f"IP :",E);H(L,M).write(E+N)
		elif I or O in B:K=B.replace(I,J).replace(O,J).replace('/',J);G=D.gethostbyname(K);C(A.GREEN+f"IP :",G);H(L,M).write(G+N)
	except:pass
J()
list=G(input('Domain List -> '))
try:
	with H(list)as L:
		for F in L:K(F)
except IOError as M:C('Error Brader '+G(M))
