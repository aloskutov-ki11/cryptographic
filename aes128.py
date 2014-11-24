#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
''' функция разбора аргументов из командной строки '''
def parseArgs():    
    cmd = 'first inputFIleName outputFileName keyFile {-c,-d}'
    if len (sys.argv) != 5:
        print "Неверное количество аргументов"
        print cmd
        return None
        
    if not isThisFile(sys.argv[1]):
        print "Входного файла не существует"
        print cmd
        return None
        
    if not isThisFile(sys.argv[3]):
        print "Файла с ключом не существует"
        print cmd
        return None
        
    if not (sys.argv[4] == '-c' or sys.argv[4] == '-d'):
        print "Ошибка, неверный формат последнего аргумента"
        print cmd
        return None
        
    return sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    

''' проверка на существование файла '''
def isThisFile(fName):
    if os.path.exists(fName):
        if os.path.isfile(fName):
            return True
        else:
            return False
    else:
        return False
		

    
''' нелинейная замена одного байта '''
def SubOneBytes(byte):
    Sbox = [[0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
            [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
            [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
            [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
            [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
            [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
            [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
            [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
            [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
            [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
            [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
            [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
            [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
            [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
            [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
            [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]]
    
    return Sbox[byte//16][byte%16]

''' нелинейная замена одного байта '''
def invSubOneBytes(byte):
    Sbox = [[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
            [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
            [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
            [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
            [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
            [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
            [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
            [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
            [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
            [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
            [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
            [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
            [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
            [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
            [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
            [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]]
    

    return Sbox[byte//16][byte%16]
    
''' Нелинейная замена байтов '''    
def SubBytes(State):
    for r in range(4):
        for c in range(4):
            State[r][c] = SubOneBytes(State[r][c])
   
    return State
    
''' Нелинейная замена байтов '''
def invSubBytes(State):
    for r in range(4):
        for c in range(4):
            State[r][c] = invSubOneBytes(State[r][c])
    
    return State   
     
def ShiftRight(Mass, count):
    return Mass[-count:] + Mass[:-count]
    
def ShiftLeft(Mass, count):    
    return Mass[count:] + Mass[0:count]
    
def ShiftRows(State):
    for i in range(1,4):
        State[i] = ShiftLeft(State[i], i)
    return State
    
def invShiftRows(State):
    for i in range(1,4):
        State[i] = ShiftRight(State[i], i)
    return State
    
''' Умножение двух чисел в поле Галуа '''
def gmul(a, b):
    p = 0
    for counter in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        a &= 0xff
        if hi_bit_set:
            a ^= 0x1b
        b >>= 1
    return p

''' Умножение слобца в поле Галуа '''
def columnMix(State, i, g1, g2, g3, g4):
    mix = gmul(State[i][0], g1) ^ gmul(State[i][1], g2) ^ gmul(State[i][2], g3) ^ gmul(State[i][3], g4)
    return mix

''' Вычисляем новые столбцы, представляя их в виде многочлена в поле Галуа GF(2^8) по модулю x^4+1 c 
фиксированным многочленом 3x^3+x^2+x+2 '''
def MixColumns(State):
    for i in range(4):
        tmp = [0] * 4
        tmp[0] = columnMix(State, i, 2, 3, 1, 1)
        tmp[1] = columnMix(State, i, 1, 2, 3, 1)
        tmp[2] = columnMix(State, i, 1, 1, 2, 3)
        tmp[3] = columnMix(State, i, 3, 1, 1, 2)

        for j in range(4):
            State[i][j] = tmp[j]

    return State

''' Вычисляем новые столбцы, представляя их в виде многочлена в поле Галуа GF(2^8) по модулю x^4+1 c 
фиксированным многочленом 3x^3+x^2+x+2 '''    
def invMixColumns(State):

    for i in range(4):
        tmp = [0] * 4
        tmp[0] = columnMix(State, i, 14, 11, 13, 9)
        tmp[1] = columnMix(State, i, 9, 14, 11, 13)
        tmp[2] = columnMix(State, i, 13, 9, 14, 11)
        tmp[3] = columnMix(State, i, 11, 13, 9, 14)

        for j in range(4):
            State[i][j] = tmp[j]

    return State
''' Циклическая перестановка  '''
def ShiftWord(word):
    return word[1:] + word[:1]

def SubWord(word):
        return [SubOneBytes(byte) for byte in word] 
           
''' Формирование набора раундовых ключей  '''
def KeyExpansion(key):
    #константная таблица
    Rcon = [[0x00, 0x00, 0x00, 0x00],
        [0x01, 0x00, 0x00, 0x00],
        [0x02, 0x00, 0x00, 0x00],
        [0x04, 0x00, 0x00, 0x00],
        [0x08, 0x00, 0x00, 0x00],
        [0x10, 0x00, 0x00, 0x00],
        [0x20, 0x00, 0x00, 0x00],
        [0x40, 0x00, 0x00, 0x00],
        [0x80, 0x00, 0x00, 0x00],
        [0x1b, 0x00, 0x00, 0x00],
        [0x36, 0x00, 0x00, 0x00]]

    w = [0] * (4 * (10 + 1)) #массив раундовых ключей
     
    #заполняем первый блок раундовых ключей нашим секретным ключом 
    for i in range(4):
        w[i] = [key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3]]
        i += 1
        
    #остальные блоки заполняем с трансформированием
    for i in range(4, 4 * (10 + 1)):
        tmp = w[i - 1]
        if i % 4 == 0:
            tmp = SubWord(ShiftWord(tmp))
            tmp = [tmp[j] ^ Rcon[i // 4][j] for j in range(4)]
        w[i] = [tmp[j] ^ w[i - 4][j] for j in range(4)]
        
    return w

def AddRoundKey(State, RoundKeys):
    for i in range(4):
        for j in range(4):
            State[i][j] ^= RoundKeys[i][j]
    return State
    
''' Шифрование блока входного текста '''
def cryptBlock(Input, wKeys):

    #инициализация массва двумерного State и Sbox
    State = [0] * 4
    for i in range(4):
        State[i] = [0] * 4
   
       
    #заполняем массив State 
    for r in range(4):
        for c in range(4):
            State[r][c] = ord(Input[r+4*c])
    
   
    State = AddRoundKey(State, wKeys[0:4])

    
    for Round in range(1,10):
        State = SubBytes(State)
        State = ShiftRows(State)
        State = MixColumns(State)
        State = AddRoundKey(State, wKeys[Round*4:(Round+1)*4])  #отправляем нужный блок из раундовых ключей
        
    #последний особенный раунд
    State = SubBytes(State)
    State = ShiftRows(State)
    State = AddRoundKey(State, wKeys[10*4:(10+1)*4])
    
    return State  
      
''' Дешифрование блока входного текста '''
def decryptBlock(Input, wKeys):
    
     #инициализация массва двумерного State и Sbox
    State = [0] * 4
    for i in range(4):
        State[i] = [0] * 4
   
       
    #заполняем массив State 
    for r in range(4):
        for c in range(4):
            State[r][c] = ord(Input[r+4*c])
    
    State = AddRoundKey(State, wKeys[4*10:(10+1)*4])
    
    Round = 9
    while Round >= 1:
        State = invShiftRows(State)
        State = invSubBytes(State)
        State = AddRoundKey(State, wKeys[Round*4:(Round+1)*4])  #отправляем нужный блок из раундовых ключей
        State = invMixColumns(State)
        Round -= 1
    
    #последний особенный раунд
    State = invShiftRows(State)
    State = invSubBytes(State)
    State = AddRoundKey(State, wKeys[0*4:(0+1)*4])
        
    return State 

''' дополнение исходного текста, чтобы его длина была кратна 16-ти байтам '''
def complete(inText, d):
    count = len(inText) % d
    while len(inText) % d != 0:
        inText += chr(255)
    return inText
    
''' Удаление лишних нулей в конце строки '''   
def delZero(outText):
    i = len(outText) - 1
    while ord(outText[i]) == 255:
        outText = outText[0:i]
        i -= 1
    
    return outText   

''' Возвращает двумерный массив в виде строки '''     
def MassToText(Mass):
    text = ''
    for r in range(4):
        for c in range(4):
            text += chr(Mass[c][r])
    return text
    
''' Возвращает функцию шифования или дешифрования '''  
def retFunc(mode, State, wKeys):
    if mode == '-c':
        return cryptBlock(State, wKeys)
    if mode == '-d':
        return decryptBlock(State, wKeys)
         
def main():
    #проверка параметров командной строки
    try:
        inputFileName, outputFileName, keyFileName, mode = parseArgs()
    except Exception as err:
        return
	
	prn = {'Nk':4, 'Nr':10, 'Nb':4}
	print prn['Nk']
	#открытие файла и чтение из него
    inF = open(inputFileName, "r")
    inText = inF.read()
    inF.close()
    #inText = inText[0:len(inText)]
	
    inK = open(keyFileName, "r")
    key = inK.read()
    inK.close()
    key = key[0:len(key)-1]
	
	#Проверка длины коюча
    if len(key) != 16:
	    print "Неверная длина ключа" 
	    return


    #Дополняем текст до необходимой кратности. В конце дописываем нули
    inText = complete(inText, 16)
    
    #формируем массив раундовых ключей
    wKeys = KeyExpansion([ord(x) for x in key])

    #количество блоков по 16 байт в исходном тексте
    Nblocks = len(inText)/16
    
    #количество итераций - номер обрабатываемого блока
    _iter = 0
    
    outF = open(outputFileName, "w")
    
    outText = ''
    while _iter < Nblocks:
        State = inText[_iter*16:(_iter+1)*16]
       
        State = retFunc(mode, State, wKeys)
        outText = MassToText(State)
        
        
        if (mode == '-d') and ( _iter == Nblocks-1): outText = delZero(outText)
        
        outF.write(outText)
        outText = ''
        _iter += 1
        
    outF.close()   

if __name__ == "__main__": 
    main()
