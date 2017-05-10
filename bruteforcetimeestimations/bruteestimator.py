import sys
import time
from passlib.hash import md5_crypt
from passlib.hash import sha256_crypt
import numpy as np


STIME = time.time()
MIN_LEN = 6
MAX_LEN = 10
CHAR_LIST = ['0','1','2','3','4','5','6','7','8','9',
             'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
             'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F',
             'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
             'W','X','Y','Z']
#CHAR_LIST = ['0','1','2','3','4','5','6','7','8','9']
#temp charlist

def runpass(pwd, pwdsha, pwdmd5, raw, sha, md5, type_test):
    if type_test == 0:
        if "".join(pwd) == "".join(raw):
            print ''.join(pwd) + " Raw Value Match " + str(time.time()-STIME)
    if type_test == 1:
        pwdsha = sha256_crypt.using(salt='ab').hash(''.join(pwd))
        if pwdsha == sha:
            print ''.pwd + " SHA Value Match " + (STIME - time.time())
    if type_test == 2:    
        pwdmd5 = md5_crypt.using(salt='ab').hash(''.join(pwd))
        if pwdmd5 == md5:
            print ''.pwd + " MD5 Value Match " + (STIME - time.time())

def strdone(string):
    t = True
    for i in range(len(string)):
        if string[i] != CHAR_LIST[-1]:
            t = False
        if not t:
            return t
    return t

def nextstr(string):
    i = len(string)-1
    i_exit = -1
    while i >= 0:
        if string[i] == CHAR_LIST[len(CHAR_LIST)-1]:
            string[i] = CHAR_LIST[0]
            i = i-1
        else:
            string[i] = CHAR_LIST[CHAR_LIST.index(string[i])+1]
            i = i_exit

def main():
    if len(sys.argv) != 3:
        print "incorrect args"
        exit()
    
    enc_input = sys.argv[1]
    typetest = int(sys.argv[2])
    if not typetest == 0 and not typetest == 1 and not typetest == 2:
        print "bad test"
        exit()
    if typetest == 0:
        print "Raw value scan"
    if typetest == 1:
        print "SHA Hashing"
    if typetest == 2:
        print "MD5 Hashing"
    
    file = open(enc_input, 'r')
    pwds = file.readlines()

    pset = [[]]
    x = 0
    for line in pwds:
        k = list(line)
        del k[-1]
        del k[-1]
        if x % 3 == 0 and not x==0:
            pset.append([])
        pset[x/3].append(k)
        x = x+1

    shortpass = [CHAR_LIST[0]]
    if typetest == 2:
        spm = md5_crypt.using(salt='ab').hash(''.join(shortpass))
    else:
        spm = ""
    if typetest == 1:
        ss256 = sha256_crypt.using(salt='ab').hash(''.join(shortpass))
    else:
        ss256 = ""
    for pwd in pset:
        runpass(shortpass, ss256, spm, pwd[0], pwd[1], pwd[2], typetest)
    while not strdone(shortpass):
        nextstr(shortpass)
        if typetest == 2:
            spm = md5_crypt.using(salt='ab').hash(''.join(shortpass))
        else:
            spm = ""
        if typetest == 1:
            ss256 = sha256_crypt.using(salt='ab').hash(''.join(shortpass))
        else:
            ss256 = ""
        for pwd in pset:
            runpass(shortpass, ss256, spm,  pwd[0], pwd[1], pwd[2], typetest)

    avgtime = (time.time()-STIME)/(len(CHAR_LIST))
    if avgtime == 0.0:
        avgtime = 0.00001
    print "Average time per brute-value test: " + str(avgtime) + "s"

    sum = 0.0
    for x in range(MIN_LEN, MAX_LEN+1):
        for y in range(1,x+1):
            sum += float(len(CHAR_LIST)**y)
    print "Number of brute-values tested: " + str(sum)
    print "Approximate time to completion (worst case) " + str(sum*avgtime) + "s"

    
    
if __name__ == "__main__":
    main()
