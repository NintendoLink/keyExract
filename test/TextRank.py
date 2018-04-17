# python 3.6.4
# encoding: utf-8
import numpy as np
node=['a','b','c','d','e']
# 初始化出入度矩阵
inout=np.zeros([len(node),len(node)])

outvj=np.ndarray(len(node))
invjarray=np.ndarray(len(node))

inout[0,4]=1
inout[0,3]=1

out_count=0
for i in inout.transpose():
    outvj[out_count]=i.sum()
    out_count+=1

# print(outvj)
