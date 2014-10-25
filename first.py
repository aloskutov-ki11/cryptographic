#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
import os
import operator

    
#функция разбора аргументов из командной строки
def parseArgs():    
    ''' Формат командной строки:
    first input output key {-c, -d}
    '''
    cmd = 'first inputFIleName outputFileName key {-c, -d}'
    if len (sys.argv) != 5:
        print "Ошибка, неверное количество аргументов"
        print cmd
        return None
        
    if not isThisFile(sys.argv[1]):
        print "Входного файла не существует"
        print cmd
        return None
        
    if not (sys.argv[4] == '-c' or sys.argv[4] == '-d'):
        print "Ошибка, неверный формат последнего аргумента"
        print cmd
        return None
        
    return sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] 
    

#проверка на существование файла
def isThisFile(fName):
    if os.path.exists(fName):
        if os.path.isfile(fName):
            return True
        else:
            return False
    else:
        return False

#функция кодирования содержимого файла
def encode(inText, key, func):
    result = ''
    index = 0
    for char in inText:
        result += chr((func(ord(char), ord(key[index])) + 256) % 256 )
        index += 1
        
        if index == len (key):
            index = 0
    return result
    
    
def main():
    #проверка параметров командной строки
    try:
        inputFileName, outputFileName, key, mode = parseArgs()
    except Exception as err:
        return
    
    #открытие файла и чтение из него
    inF = open(inputFileName, "r")
    inText = inF.read()
    inF.close()
    
    d = {'-c': operator.add, '-d': operator.sub}
    result = encode(inText, key, d[mode])
    outF = open(outputFileName, "w")
    outF.write(result)
    outF.close()
    print "End of encoding"

if __name__ == "__main__": 
    main()
