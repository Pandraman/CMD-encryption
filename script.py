import os
import sys

files = []
if len(sys.argv) < 2:
    print("No files provided. Drag and drop files onto the batch file.")
else:
    
    for arg in sys.argv[1:]:
        files.append(arg)
        






def string_to_int_array(input_string):
    return [ord(char) for char in input_string]

def readBytes(file):
    with open(file, "rb") as file:
        byte_list = list(file.read())
    return byte_list

def readPlain(file):
    with open(file, "r") as file:
        byte_list = eval(file.read())
    return byte_list

def writePlain(file, bytes):
    with open(file, "wb") as file:
        file.write(bytearray(bytes))

def writeBytes(file_path, byte_list):
    with open(file_path, "wb") as file:
        file.write(bytearray(byte_list))




def encrypt(file, key):
    lk = len(key)
    K = key
    file = str(file)
    newList = []
    L = readBytes(file)
    l = 0
    for i in L:
        l += 1
        M = int(i+K[l%lk])
        newList.append(M%256)
    writeBytes(file,newList)

def decrypt(file, key):
    lk = len(key)
    K = key
    file = str(file)
    newList = []
    L = readBytes(file)
    l = 0
    for i in L:
        l += 1
        M = int(i-K[l%lk])
        newList.append(M%256)
    writeBytes(file,newList)





print("En / Decryption  |  v2.0")
print("(E)ncryption oder (D)ecryption")
M = input()
while not M in ['E','e','D','d']:
    M = input()
    print("Not valid, please retry")
if M.upper() == 'E':
    print()
    print("------ ENCRYPTION -------")
    done = False
    while not done:
        a = 0

        for element in files:
            a += 1
            print(a, element)
        key = input('Key: ')
        kString = string_to_int_array(key)
        fileList = files
        
        for element in fileList:
            element.replace("\\","/")
        for filename in fileList:
            try:
                encrypt(filename,kString)
                print('Success, exiting...')
                done = True
            except:
                done = False
                print("File or Key unvalid, please retry")
if M.upper() == 'D':
    print()
    print("------ Decryption -------")
    done = False
    while not done:
        folderList = files

        a = 0
        for element in folderList:
            a += 1
            print(a, element)
        
        
        key = input('Key: ')
        kString = string_to_int_array(key)
        fileList = files
        for filename in fileList:
            try:
                decrypt(filename,kString)
                print('decrypting...')
                done = True
            except:
                done = False
                print("File or Key unvalid, please retry")