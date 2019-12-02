'''
Created on 2019年11月29日

@author: hp
'''

n=int(input())
str2=""
if not n:
    print(0)
else:
    while n:
        if str2=="" and n%10==0:
            pass
        else:
            str2+=str(n%10)
        n//=10
    print(str2)
