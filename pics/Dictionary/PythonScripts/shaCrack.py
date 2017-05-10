#!/usr/bin/python
# -*- coding: utf-8 -*-

#Chad Sprong
#version 1
#cracks the passwords from the password file using the dictionary attack
#passwords are encrypted using SHA-256
import time
from passlib.hash import sha256_crypt

def testPass(password):
    start = time.time()
    dictFile = open('passwordDict.txt', 'r')
    for word in dictFile.readlines():
        hash = sha256_crypt.using(salt='ab').hash(word)
        if password == hash:
            print '[+] Found Password: ' + word + '\n'
            end = time.time()
            print end - start
            return
    print '[-] Password Not Found.\n'
    end = time.time()
    print end - start
    return


def main():
    wordFile = open('originalPassword.txt')
    for password in wordFile.readlines():
        print '[*] Looking For: ' + password
        hash = sha256_crypt.using(salt='ab').hash(password)
        testPass(hash)


if __name__ == '__main__':
    main()
