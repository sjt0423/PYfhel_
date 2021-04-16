from Pyfhel import Pyfhel,PyCtxt,PyPtxt
import numpy as np
import time
import operator
he=Pyfhel()
he.contextGen(p=1179649,m=32768,flagBatching=True,fracDigits=20)
he.keyGen()
a=PyCtxt()
b=PyCtxt()
q=0
#加密文件
def PPctxt(name):
    global panduan
    panduan=name
    fil=open(name,mode='r',encoding='UTF-8')
    lines=fil.readlines()
    strr=''.join(lines)
    #全局化前三位密文
    global lbb
    lb=list(strr)
    lb=lb[:3]

    lbb=[]
    for i in lb:
        lbb.append(ord(i))
    lbb=np.array(lbb)
    print(lbb)
    lbb=he.encryptBatch(lbb)
    #全局化后三位密文
    global ebb,l
    eb=list(strr)
    l=len(strr)
    eb=eb[l-4:l-1]
    print(eb)
    ebb=[]
    for i in eb:
        ebb.append(ord(i))
    ebb=np.array(ebb)
    ebb=he.encryptBatch(ebb)

    #转数字+密文化+存储
    arr=[]
    for line in strr:
        for ind in line:
            arr.append(ind)
    #arr.remove('\n')
    brr=[]
    for i in arr:
        brr.append(ord(i))
    crr=np.array(brr)
    #列表数据转数组
    err=he.encryptBatch(crr)
    err.save(name)
PPctxt('1.txt')

#字符串开头判断
def startswitch(name,judge):
    while name==panduan:
        arr=list(judge)
        #print(arr)
        brr=[]
        for i in arr:
            brr.append(ord(i))
        brr=np.array(brr)
        brr=he.encryptBatch(brr)
        result=he.sub(lbb,brr)
        #以下两行测试用
        global bb
        bb=result
        break
    return result
#startswitch('1.txt','sjt')

#字符串结尾判断
def endswitch(name,judge):
    while name==panduan:
        arr=list(judge)
        brr=[]
        for i in arr:
            brr.append(ord(i))
        brr=he.encryptBatch(brr)
        result=he.sub(ebb,brr)
        #print(he.decryptBatch(result))
        #测试
        global ee
        ee=result
        break
    return result
#endswitch('1.txt','sjt')
#eq比较函数
def eq(name,eq):
    a.load(name,encoding='array')
    eq=list(eq)
    arr=[]
    for i in eq:
        arr.append(ord(i))
    arr=np.array(arr)
    arr=he.encryptBatch(arr)
    result=he.sub(a,arr)
    #ceshi
    global jg
    jg=result
    return jg
eq('1.txt','sjt')
#字符串开头、结尾判断+比较 解密函数
def DecryptJudge():
    a=he.decryptBatch(jg)
    cc=a
    a=a[:3]
    b=a[:l]
    #print(b)
    c=0
    d=0
    for i in cc:
        if i==0:
            d=1
    for i in b:
        if(i==0 or d==1):
            c=1
            #print(c)
    #print(c)
    if(a==[0,0,0] or c==1):
        print('True')
    else:
        print('Flase')
DecryptJudge()
