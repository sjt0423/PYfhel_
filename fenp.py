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
    global l
    l=len(strr)
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
    
    global e,f,g
    # :'#'记录
    ii=0
    b=c=d=np.zeros((l,),dtype=int)
    for i in arr:
        if(i=='#'):
            b[ii]=9
        ii=ii+1
    #print('b:::',b)
    bb=np.array(b)
    e=he.encryptBatch(bb)
    
    #' '记录
    iii=0
    for i in arr:
        if(i==' '):
            c[iii]=12
        iii=iii+1
    cc=np.array(c)
    f=he.encryptBatch(cc)

PPctxt('1.txt')
def slicing(name,cc):
    #cc-选择从‘#’/‘ ’处分片
    a.load(name,encoding='array')
    #print('a:',type(a))
    #print('e:',type(e))
    if(cc=='#'):
        bb=he.add(a,e)
        bb.save(name)
    elif(cc==' '):
        b=he.add(a,f)
        b.save(name)
    else:
        print('Error: \n mistake')
slicing('1.txt','#')
def Decrypt(name):
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
