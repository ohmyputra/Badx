I='clear'
H=input
B=print
try:import os,socket as E,os as C;from colorama import Fore as A,Back as D,Style;import time as F
except ModuleError as J:B('Module Error :',J)
def K():E=I;F='cls';C.system([E,F][C.name=='nt']);G=A.RED;H=A.GREEN;M=A.YELLOW;N=D.RED;O=D.GREEN;J=D.YELLOW;K=Style.RESET_ALL;L='\n\t{}_______                   __  __    __ \n\t/       \\                 /  |/  |  /  |\n\t$$$$$$$  |  ______    ____$$ |$$ |  $$ |\n\t$$ |__$$ | /      \\  /    $$ |$$  \\/$$/ \n\t$$    $$<  $$$$$$  |/$$$$$$$ | $$  $$<  \n\t$$$$$$$  | /    $$ |$$ |  $$ |  $$$$  \\ \n\t$$ |__$$ |/$$$$$$$ |$$ \\__$$ | $$ /$$  |\n\t$$    $$/ $$    $$ |$$    $$ |$$ |  $$ |\n\t$$$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/     \n\t\n\t{}{}( ! ) OPEN PORT SCANNER. Default Port : 80, Edit Manual Port On Source Code !\n\t{}'.format(H,J,G,K);B(L)
def G():C.system('python openport.py')
def L(ip,port=80):
	Q='N';P='Y';O='Cek Lagi? Y/N : ';N=True;M='CHECKING PORT.....\n'
	try:
		J=E.socket(E.AF_INET,E.SOCK_STREAM);J.settimeout(2);K=J.connect_ex((ip,port))
		if K==0:
			C.system(I);B(A.YELLOW+M);F.sleep(2);B(A.GREEN+'STATUS PORT : OPEN\n')
			while N:
				D=H(O)
				if D==P:G()
				elif D==Q:break
		else:
			C.system(I);B(A.YELLOW+M);F.sleep(2);B(A.RED+'port CLOSED, connect_ex returned: '+str(K))
			while N:
				D=H(O)
				if D==P:G()
				elif D==Q:break
	except Exception as L:B(L)
if __name__=='__main__':K();M=H('Enter IP : ');L(M)
