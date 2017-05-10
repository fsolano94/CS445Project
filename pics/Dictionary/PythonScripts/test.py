#!/usr/bin/python
# -*- coding: utf-8 -*-

#Chad Sprong
#version 1
#cracks the passwords from the password file using the dictionary attack
import time


def testPass(password):
    start = time.time()
    dictFile = open('passwordDict.txt', 'r')
    for word in dictFile.readlines():
        if password == word:
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
        testPass(password)
                    



if __name__ == '__main__':
    main()
