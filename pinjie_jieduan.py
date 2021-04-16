from Pyfhel import Pyfhel,PyCtxt,PyPtxt
import numpy as np
import time
he=Pyfhel()
he.contextGen(p=1179649,m=32768,flagBatching=True,fracDigits=20)
he.keyGen()
a=PyCtxt()
b=PyCtxt()
q=0
cc=0

#加密文件
def PPctxt(name):
  fil=open(name)
  lines=fil.readlines()
  strr=''.join(lines)
  global l
  l=len(strr)
  l=l-1
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
  
  #为按行截取作准备：行数、每行字符数
  global nrr,num_zifu
  num_zifu=0
  nrr=[]
  for line in lines:
      num_zifu=num_zifu+len(line)
      nrr.append(len(line))
  #行数
  global num_h
  num_h=len(lines)
PPctxt('1.txt')

#拼接/追加
def concat(name,seq):
    global l
    a.load(name,encoding='array')
    #0数组用于追加
    b=np.zeros((l,),dtype=int)
    b=list(b)
    c=np.array(list(seq))
    #追加
    for i in c:
        b.append(ord(i))
    b=np.array(b)
    b=he.encryptBatch(b)
    #拼接
    d=he.add(a,b)
    #存储
    d.save(name)
    
    l=l+len(c)
    #print(he.decryptBatch(d))
#concat('1.txt','sjt')

#截断(按字符)
def cut_off(name,n):
    global l
    a.load(name,encoding='array')
    b=np.zeros((l,),dtype=int)
    for i in range(n):
        b[i]=1
    b=he.encryptBatch(b)
    c=he.multiply(a,b)
    c.save(name)
    l=n
#cut_off('1.txt',2)
#截断(按行)
def h_cut_off(name,n):
    num=0
    global l
    if(n<num_h):
        for i in range(n):
            num=num+nrr[i]
    a.load(name,encoding='array')
    b=np.zeros((l,),dtype=int)
    for i in range(num):
        b[i]=1
    b=he.encryptBatch(b)
    c=he.multiply(a,b)
    c.save(name)
    l=num
h_cut_off('1.txt',2)
#解密
def Decrypt(name):
  #global q
  a.load(name,encoding='array')
  b=he.decryptBatch(a)
  b=b[:l]
  #print(b)
  brr=[]
  for i in b:
    brr.append(chr(i))
  print(brr)
  brr=''.join(brr)
  #解密后明文存入文件
  f=open(name,'w')
  f.writelines(brr)
  f.close()
Decrypt('1.txt')
