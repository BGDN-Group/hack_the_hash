#!/usr/bin/python3

from hashlib import sha3_256, sha3_384, sha3_512
from hashlib import sha256,sha384,sha512
from os.path import exists
from random import choice
import platform as pfm
from os import system
from sys import argv

def clear_console():
	if pfm.system() == 'Linux':
		system("clear")
	else:
		system("cls")

def brute_force_sha256():
	file_to_hash = str(input("Enter path to hash : "))
	clear_console()

	data_hash = open(file_to_hash, "r").read()

	i = 1
	while True:
		n = ''
		for x in range(length_psw):
			generate_psw = choice(mask_psw)
			n = n + str( generate_psw )

		if data_hash == sha256(n.encode("utf-8")).hexdigest():
			print("Match Found! -->",n)
			raise SystemExit
		else:
			print("Match not found! -->",i)
			i = i + 1

def brute_force_sha384():
	file_to_hash = str(input("Enter path to hash : "))
	clear_console()

	data_hash = open(file_to_hash, "r").read()

	i = 1
	while True:
		n = ''
		for x in range(length_psw):
			generate_psw = choice(mask_psw)
			n = n + str( generate_psw )

		if data_hash == sha384(n.encode("utf-8")).hexdigest():
			print("Match Found! -->",n)
			raise SystemExit
		else:
			print("Match not found! -->",i)
			i = i + 1

def brute_force_sha512():
	file_to_hash = str(input("Enter path to hash : "))
	clear_console()

	data_hash = open(file_to_hash, "r").read()

	i = 1
	while True:
		n = ''
		for x in range(length_psw):
			generate_psw = choice(mask_psw)
			n = n + str( generate_psw )

		if data_hash == sha512(n.encode("utf-8")).hexdigest():
			print("Match Found! -->",n)
			raise SystemExit
		else:
			print("Match not found! -->",i)
			i = i + 1

def brute_force_sha3_256():
	file_to_hash = str(input("Enter path to hash : "))
	clear_console()

	data_hash = open(file_to_hash, "r").read()

	i = 1
	while True:
		n = ''
		for x in range(length_psw):
			generate_psw = choice(mask_psw)
			n = n + str( generate_psw )

		if data_hash == sha3_256(n.encode("utf-8")).hexdigest():
			print("Match Found! -->",n)
			raise SystemExit
		else:
			print("Match not found! -->",i)
			i = i + 1

def brute_force_sha3_384():
	file_to_hash = str(input("Enter path to hash : "))
	clear_console()

	data_hash = open(file_to_hash, "r").read()

	i = 1
	while True:
		n = ''
		for x in range(length_psw):
			generate_psw = choice(mask_psw)
			n = n + str( generate_psw )

		if data_hash == sha3_384(n.encode("utf-8")).hexdigest():
			print("Match Found! -->",n)
			raise SystemExit
		else:
			print("Match not found! -->",i)
			i = i + 1

def brute_force_sha3_512():
	file_to_hash = str(input("Enter path to hash : "))
	clear_console()

	data_hash = open(file_to_hash, "r").read()

	i = 1
	while True:
		n = ''
		for x in range(length_psw):
			generate_psw = choice(mask_psw)
			n = n + str( generate_psw )

		if data_hash == sha3_512(n.encode("utf-8")).hexdigest():
			print("Match Found! -->",n)
			raise SystemExit
		else:
			print("Match not found! -->",i)
			i = i + 1

def get_info():

	global length_psw
	global mask_psw

	hash_funcs = ['sha256', 'sha384', 'sha512', 'sha3_256', 'sha3_384', 'sha3_512']

	type_hash = str(input('Enter hash : '))
	if not type_hash:
		print("No command! --> Exit")
		raise SystemExit
	else:
		if type_hash == argv[0]:
			print(type_hash+" not the hash function --> Exit")
			raise SystemExit
		else:
			if type_hash in hash_funcs:
				try:
					length_psw = int(input("Enter length of password : "))
				except:
					print("Value Error! --> Exit")
					raise SystemExit
				mask_psw = str(input("Input symbols which must include password : "))
				if not mask_psw:
					print("No command! --> Exit")
					raise SystemExit
				else:
					if mask_psw == argv[0]:
						print(mask_psw+" not the symbols password! --> Exit")
						raise SystemExit
					else:
						if type_hash == "sha256":
							brute_force_sha256()
						elif type_hash == "sha384":
							brute_force_sha384()
						elif type_hash == "sha512":
							brute_force_sha512()
						elif type_hash == "sha3_256":
							brute_force_sha3_256()
						elif type_hash == "sha3_384":
							brute_force_sha3_384()
						elif type_hash == "sha3_512":
							brute_force_sha3_512()
						else:
							raise SystemExit
			else:
				print("Function not found! --> Exit")

clear_console()

try:
	get_info()
except KeyboardInterrupt:
	print("Password Recovery has been stopped!")
	raise SystemExit

# BGDN-Group
# IMO +993 62632281
