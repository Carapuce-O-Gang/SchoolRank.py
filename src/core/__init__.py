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
	for row in [
		"  {}_____      _                 _   _____             _{}".format(Colors.yellow, Colors.end),
		" {}/ ____|    | |               | | |  __ \           | |{}".format(Colors.yellow, Colors.end),
		"{}| (___   ___| |__   ___   ___ | | | |__) |__ _ _ __ | | __{}".format(Colors.yellow, Colors.end),
		" {}\___ \ / __| '_ \ / _ \ / _ \| | |  _  // _` | '_ \| |/ /\t{} {}{}".format(Colors.yellow, Colors.red, info["version"], Colors.end),
		" {}____) | (__| | | | (_) | (_) | | | | \ \ (_| | | | |   <\t{} by {}{}".format(Colors.yellow, Colors.purple, info["author"], Colors.end),
		"{}|_____/ \___|_| |_|\___/ \___/|_| |_|  \_\__,_|_| |_|_|\_\{}\n".format(Colors.yellow, Colors.end)
	]:
		print(row)
		sleep(.05)
