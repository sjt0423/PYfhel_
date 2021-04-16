from Pyfhel import Pyfhel,PyCtxt,PyPtxt
import numpy as np
import time
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
  fil=open(name)
  lines=fil.readlines()
  strr=''.join(lines)
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
  global l
  l=len(strr)
PPctxt('1.txt')
#搜索（单字母）
def count(name,zm,l1=None):
    global c
    c=None
    global zmm
    zmm=zm
    if(len(zm)<2):
        a.load(name,encoding='array')
        b=np.zeros((l,),dtype=int)
        d=ord(zm)
        for i in range(l1,l):
            #print(l1,l)
            b[i]=d
        #print(b)
        b=he.encryptBatch(b)
        c=he.sub(a,b)
        result=c
    else:
        print('Error: Does not conform to be rule,the parameter size should be 1')
    print(c)
    return c
count('1.txt','iss',1)
def DecryptCount(name,n):
    while(name==panduan and len(zmm)<2):
        a=he.decryptBatch(c)
        ii=0
        a=a[:l]
        for i in a:
            if i==0:
                ii=ii+1
        print(zmm,':',ii,'次')
        break
    else:
        print('Error:The name or the length of the input string is not corret and cannot be decrypt correctly')
DecryptCount('1.txt',1)
