#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
import os

#глобальные переменные
inputFileName = sys.argv[1]
outputFileName = sys.argv[2]
key = sys.argv[3]
mode = sys.argv[4]

#функция разбора аргументов из командной строки
def checkStartLine():
	argFile = re.compile('\w+\.txt')
	argKey = re.compile('\w+')
	
	if len (sys.argv) != 5:
		print "Ошибка, неверное количество аргументов"
		return 1
		
	if not argFile.match(inputFileName):
		print "Ошибка, неверный формат первого аргумента"
		return 1
	
	if not argFile.match(outputFileName):
		print "Ошибка, неверный формат второго аргумента"
		return 1
	
	if not argKey.match(key):
		print "Ошибка, неверный формат ключа. Только символы и цифры латинского алфавита "+sys.argv[3]
		return 1
		
	if not (sys.argv[4] == '-c' or sys.argv[4] == '-d'):
		print "Ошибка, неверный формат последнего аргумента"
		return 1
		
	return 0


#проверка на существование файла
def isThisFile(fName):
	if os.path.exists(fName):
		if os.path.isfile(fName):
			return 0
		else:
			print "Входного файла не существует"
			return 1
	else:
		print "Входного файла не существует"
		return 1

#функция кодирования содержимого файла
def encode(inText, key):
	result = ''
	index = 0
	for char in inText:
		result += chr( (ord(char)+(ord(key[index])) )%255)
		index += 1
		
		if index == len (key):
			index = 0
	return result
	
#функция декодирования содержимого файла	
def decode(inText, key):
	result = ''
	index = 0
	for char in inText:
		result += chr( (ord(char)-(ord(key[index])) + 255 )%255)
		index += 1
		
		if index == len (key):
			index = 0
	
	return result
	
	
	
if __name__ == "__main__":
	
	#проверка параметров командной строки
	if checkStartLine():
		sys.exit(1)
		
	#проверка на существование входного файла
	if isThisFile(inputFileName):
		sys.exit(1)
	
	#открытие файла и чтение из него
	inF = open(inputFileName, "r")
	inText = inF.read()
	inF.close()
	
	if mode == "-c":
		result = encode(inText, key)
		outF = open(outputFileName, "w")
		outF.write(result)
		outF.close()
		print "End of encoding\n"
		
	if mode == "-d":
		result = decode(inText, key)
		outF = open(outputFileName, "w")
		outF.write(result)
		outF.close()
		print "End of decoding\n"
	

















