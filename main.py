#!/usr/bin/python
# -*- coding: utf8 -*-

# Vérification de l'éxecution du script avec Python3
from sys import argv, version_info
if(version_info.major < 3):
	print("/!\ - Program must be run with Python 3")
	exit()

# Importation des dépendances
from core import splash
from core.api import Api

def arg(info):
	args = {
		"prefix": (
			(("-h", "--help"), ""),
			(("-v", "--version"), "")
		),
		"descriptions": (
			"\t\tDisplays the help menu",
			"\t\tDisplays the version of the program\n"
		)
	}

	if(argv[1] in args["prefix"][-2][0]):
		print(" {} {} par {}".format(info["name"], info["version"], info["author"]))
		print(" Launch: python main.py <arg>\n")
		print(" Arguments:")

		for i in range(0, len(args["prefix"])):
			print(f' {args["prefix"][i][0][0]}, {args["prefix"][i][0][1]} {args["prefix"][i][1]}\t{args["descriptions"][i]}')

	elif(argv[1] in args["prefix"][-1][0]):
		print(" {} {} - {}\n".format(info["name"], info["version"], info["author"]))

def main(info):
	splash(info)

	api = Api()

if(__name__ == "__main__"):
	info = {
		"name": "ElTwittoDelDiablo",
		"version": "1.0",
		"author": "Carapuce O Gang"
	}

	if(len(argv) > 1):
		arg(info)

	else:
		main(info)
