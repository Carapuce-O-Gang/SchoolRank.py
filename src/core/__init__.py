from os import system as prompt
from platform import system
from time import sleep

class Colors: # Module de coloration pour les système Linux/Unix
	if(system() == "Linux"):
		bold	= str("\033[1m")
		italic	= str("\033[3m")

		red		= str("\033[31m")
		green	= str("\033[32m")
		yellow	= str("\033[33m")
		blue	= str("\033[34m")
		purple	= str("\033[35m")
		cyan	= str("\033[36m")
		white	= str("\033[37m")

		end		= str("\033[0m")

	else:
		bold = italic = end = str("")
		red = green = yellow = blue = purple = cyan = white = str("")

class Icons: # Module d'icône ascii
	warn = str(f" {Colors.bold}{Colors.red}[!]{Colors.end} - ")
	info = str(f" {Colors.bold}{Colors.blue}(i){Colors.end} - ")
	tips = str(f" {Colors.bold}{Colors.green}(?){Colors.end} - ")
	play = str(f" {Colors.bold}{Colors.green}(>){Colors.end} - ")

def splash(info): # Splash Screen
	prompt('clear' if(system() == "Linux") else 'cls')
	for row in [
		" {}_____ _ _____          _ _   _        ____       _ ____  _       _     _{}".format(Colors.yellow, Colors.end),
		"{}| ____| |_   _|_      _(_) |_| |_ ___ |  _ \  ___| |  _ \(_) __ _| |__ | | ___{}".format(Colors.yellow, Colors.end),
		"{}|  _| | | | | \ \ /\ / / | __| __/ _ \| | | |/ _ \ | | | | |/ _` | '_ \| |/ _ \{}".format(Colors.yellow, Colors.end),
		"{}| |___| | | |  \ V  V /| | |_| || (_) | |_| |  __/ | |_| | | (_| | |_) | | (_) |\t{} {}{}".format(Colors.yellow, Colors.red, info["version"], Colors.end),
		"{}|_____|_| |_|   \_/\_/ |_|\__|\__\___/|____/ \___|_|____/|_|\__,_|_.__/|_|\___/\t{} by {}{}\n".format(Colors.yellow, Colors.purple, info["author"], Colors.end)
	]:
		print(row)
		sleep(.05)
