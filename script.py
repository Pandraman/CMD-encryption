import os



def list_files_in_path(path):
    file_list = []
    
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)

    return file_list

def list_folders_in_path(path=os.getcwd()):
    folder_list = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return folder_list





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
        folderList = list_folders_in_path()
        a = 0

        for element in folderList:
            a += 1
            print(a, element)
        filename = int(input('File: '))
        key = input('Key: ')
        kString = string_to_int_array(key)
        fileList = list_files_in_path(folderList[filename-1])
        
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
        folderList = list_folders_in_path()

        a = 0
        for element in folderList:
            a += 1
            print(a, element)
        
        
        filename = int(input('File: '))
        key = input('Key: ')
        kString = string_to_int_array(key)
        fileList = list_files_in_path(folderList[filename-1])
        for filename in fileList:
            try:
                decrypt(filename,kString)
                print('Success, exiting...')
                done = True
            except:
                done = False
                print("File or Key unvalid, please retry")
