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
ppp=0
#加密文件
def PPctxt(name):
    fil=open(name)
    lines=fil.readlines()
    strr=''.join(lines)
    arr=[]
    for line in strr:
        for ind in line:
            arr.append(ind)
    arr.remove('\n')

    global lenth
    lenth=len(arr)
    
    brr=[]
    global qq
    global pp
    for i in arr:
        brr.append(ord(i))
        q=0
        p=0
        l=len(brr)
        pp=np.zeros((l,),dtype=int)
        qq=np.zeros((l,),dtype=int)
        #小写记录
        for i in brr:
            if(96<i<123):
                qq[q]=32
            q=q+1
        #大写记录
        for i in brr:
            if(64<i<91):
                pp[p]=32
            p=p+1
    global ppp
    if(pp[0]==32):
        ppp=1
    print('qq',qq)
    pp=np.array(pp)
    pp=he.encryptBatch(pp)
    qq=np.array(qq)
    qq=he.encryptBatch(qq)

    crr=np.array(brr)
    err=he.encryptBatch(crr)
    err.save(name)
    pp.save('dxjl.txt')
    qq.save('xxjl.txt')
PPctxt('1.txt')
#print(qq)
#大写转换
def upper(name):
  a.load(name,encoding='array')
  b.load('xxjl.txt',encoding='array')
  
  c=he.sub(a,b) 
  c.save(name)
  #print(he.decryptBatch(c))
  a.load('dxjl.txt',encoding='array')
  e=he.decryptBatch(a)
  #print('e1',e[1])
  
  for i in range(len(e)):
      e[i]=32
  #print('e',e)
  e=he.encryptBatch(e)
  e.save('dxjl.txt')
#upper('1.txt')

#小写转换
def lower(name):
  a.load(name,encoding='array')
  b.load('dxjl.txt',encoding='array')
  #print(pp)
  #b=he.encryptBatch(pp)
  c=he.add(a,b)
  #d=he.decryptBatch(b)
  #print('b',b[:5])
  c.save(name)
  a.load('xxjl.txt',encoding='array')
  e=he.decryptBatch(a)

  for i in range(len(e)):
      e[i]=32

  e=he.encryptBatch(e)
  e.save('xxjl.txt')
#lower('1.txt')
#首字母大写(整体)其他小写
def capitalize(name):
  a.load(name,encoding='array')
  b.load('dxjl.txt',encoding='array')
  #首字母已经大写ppp=1
  if(ppp==1):
      c=he.add(a,b)
  else:
      d=[32,0]
      d=he.encryptBatch(d)
      c=he.add(a,b)
      c=he.sub(c,d)
  c.save(name)
  #修改大写记录
  e=he.decryptBatch(b)
  for i in range(len(e)):
      e[i]=0
  e[0]=32
  e=he.encryptBatch(e)
  e.save('dxjl.txt')
  #修改小写记录
  a.load('xxjl.txt',encoding='array')
  f=he.decryptBatch(a)
  for i in range(len(f)):
      f[i]=32
  f[0]=0
  f=he.encryptBatch(f)
  f.save('xxjl.txt')
#capitalize('1.txt')

#大小写反转
def swapcase(name):
    a.load(name,encoding='array')
    b.load('dxjl.txt',encoding='array')
    c=he.add(a,b)#原大写变小写
    b.save('xxjl.txt')
    b.load('xxjl.txt',encoding='array')
    b.save('dxjl.txt')

    c=he.sub(c,b)#原小写变大写

    c.save(name)
swapcase('1.txt')
#解密
def Decrypt(name):
  global q
  a.load(name,encoding='array')
  b=he.decryptBatch(a)
  b=b[:lenth]
  #print(b)
  brr=[]
  for i in b:
    brr.append(chr(i))
  print(brr)
Decrypt('1.txt')
