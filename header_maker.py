from pyfiglet import figlet_format
from termcolor import colored

def header_maker():
	header = figlet_format("PROFESOR HENRY REMAKE")
	header = colored(header, color = "cyan")
	print(header)