O=print
try:import os as B,time as P,requests as Q;from colorama import Fore as A,Back as C,Style;from rich.console import Console as F;from rich.table import Table
except ImportError as G:O('Gagal Import Module, Install modulenya : ',G)
H=F()
D=A.RED
I=A.GREEN
R=A.YELLOW
S=C.RED
T=C.GREEN
J=C.YELLOW
E=Style.RESET_ALL
K='\n {}_______                   __  __    __ \n/       \\                 /  |/  |  /  |\n$$$$$$$  |  ______    ____$$ |$$ |  $$ |\n$$ |__$$ | /      \\  /    $$ |$$  \\/$$/ \n$$    $$<  $$$$$$  |/$$$$$$$ | $$  $$<  \n$$$$$$$  | /    $$ |$$ |  $$ |  $$$$  \\ \n$$ |__$$ |/$$$$$$$ |$$ \\__$$ | $$ /$$  |\n$$    $$/ $$    $$ |$$    $$ |$$ |  $$ |\n$$$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/     \n   \n{}{}( ! ) BadX Tools | Exploit 4Fun!\n{}'.format(I,J,D,E)
def L():A='clear';C='cls';B.system([A,C][B.name=='nt'])
def M():L();O(K)
def N():
	K='5';J='4';I='3';G='2';F='1';M();A=Table(title='Domain Tools',show_header=True,header_style='bold green');A.add_column('No.',style='dim',width=12);A.add_column('Tools');A.add_row(F,'Domain To IP');A.add_row(G,'Reverse IP');A.add_row(I,'Subdomain Enumerate');A.add_row(J,'Open Port Check');A.add_row(K,'Admin Finder');H.print(A);C=str(input('{}Select Tools -> {}'.format(D,E)))
	if C==F:B.system('cd toip/;python toip.py')
	elif C==G:B.system('cd revip/;python revip.py')
	elif C==I:B.system('cd subdo/;python subdo.py')
	elif C==J:B.system('cd opport/;python openport.py')
	elif C==K:B.system('cd admin/;python admin.py')
N()
