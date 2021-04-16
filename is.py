from Pyfhel import Pyfhel,PyCtxt,PyPtxt
import numpy as np
import time
he=Pyfhel()
he.contextGen(p=1179649,m=32768,flagBatching=True,fracDigits=20)
he.keyGen()
a=PyCtxt()
b=PyCtxt()
q=0
qq=[]
pp=[]
#加密文件
def PPctxt(name):
    fil=open(name,mode='r',encoding='UTF-8')
    lines=fil.readlines()
    strr=''.join(lines)
    
    isde=strr.isdecimal()#判断是否全为数字
    isalp=strr.isalpha()#是否全为字母
    isaln=strr.isalnum()#是否只含有数字或字母
    isup=strr.isupper()#是否全为大写字母
    islo=strr.islower()#是否全为小写字母
    isti=strr.istitle()#是否符合title()
    iside=strr.isidentifier()#是否符合命名规则
    global sz,zm,szzm,dx,xx,tt,ide
    #print(type(int(isde)))
    sz=he.encryptInt(int(isde))
    #print(he.decryptInt(sz))
    zm=he.encryptInt(int(isalp))
    szzm=he.encryptInt(int(isaln))
    dx=he.encryptInt(int(isup))
    xx=he.encryptInt(int(islo))
    tt=he.encryptInt(int(isti))
    ide=he.encryptInt(int(iside))
PPctxt('2.txt')
def isdecimal():
    return sz
def isalpha():
    return zm
def isalnum():
    return szzm
def isupper():
    return dx
def islower():
    return xx
def istitle():
    return tt
def isidentifier():
    return ide
#p=isdecimal()
#print(he.decryptInt(p))
