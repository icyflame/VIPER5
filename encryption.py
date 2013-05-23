##File number 4
##
##This file consists of the two main functions that will help to encrypt
##and decrypt the data at the start and at the end of the program.
##
##This is a part of the program in Python Tkinter
##
##created on 20th May, 2013

from Crypto.Cipher import *

global encryptor
global decryptor

key1 = 'siddharth kannan. this is a long key'

encryptor = ARC4.new(key1)
decryptor = ARC4.new(key1)

al = []

def decryptAll():

    filin = open('viper','r')
    filout = open('temp','w')

    for i in filin:

        if not i == '':

            while i[-1] == '\n' or i[-1] == '\r':

                i = i[:-1]

        print decryptor.decrypt(i) 

        filout.write(decryptor.decrypt(i) + '\n')


    filin.close()

    filout.close()

    import os
    os.remove('viper')
    os.rename('temp','viper')

    return True

def encryptAll():
    
    filin = open('viper','r')
    filout = open('temp','w')

    for i in filin:

        if not i == '':

            while i[-1] == '\n' or i[-1] == '\r':

                i = i[:-1]

        print i
        al.append(encryptor.encrypt(i))

        print
        print

        filout.write(encryptor.encrypt(i) + '\n')


    filin.close()

    filout.close()

    import os
    os.remove('viper')
    os.rename('temp','viper')

    return True
