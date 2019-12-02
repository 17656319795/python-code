'''
Created on 2019年12月1日

@author: hp
'''
import random
mp={'zuofei':1,'chudai':2,'saiwen':3}
print(mp,'\n',mp['zuofei'])
mp2={}#空字典
print(mp2)
mp3=dict()#空字典
print(mp3)
mp4=dict(mp)
print(mp4)
'''zip()函数讲两个序列组合成字典并返回zip对象'''
duixiang=zip([1,2,3,4,5,6],["1",'2','3','4'])#组合成的字典较小
mp5=dict(duixiang)
print(mp5)
'''通过键值对创建字典'''
mp6=dict(迪迦='平成',戴拿='平成',艾斯='昭和',泰罗='昭和')
print(mp6)
'''创建value值为空的字典'''
mp7=dict.fromkeys([1,2,3,4,5])
print(mp7)
'''另外一种通过两个序列(元组->列表)建立字典的方式,但结果与14行代码不同,表示不同的含义'''
mp8={(1,2,3,4,5):[6,7,8,9,10]}
print(mp8)
del mp8#删除字典,完全消失
mp7.clear()#只删除元素,相当于删除后变成了空字典,但依然存在于内存中
'''通过键访问值'''
mp8={"奥特曼":"很厉害",'怪兽':'也很厉害'}
print(mp8["奥特曼"])
# print(mp8['不存在'])
'''如果直接输出字典中没有的键对应的值会出现异常,所以应该按照下面的方式'''
print(mp8["不存在"] if '' in mp8 else '我的字典里没有此人')#第一种方法
print(mp8.get('不存在', '我的字典里没有此人'))              #第二种方法
'''遍历字典'''
t=mp8.items();
for x in t:
    print(x)
print(t)
print(mp8)
for key,value in mp8.items():
    print(key+value)
'''只遍历键'''
for key in mp8.keys():
    print(key,end=" ")
print()
for value in mp8.values():
    print(value,end=" ")
print()
'''添加字典元素'''
mp9={}
print(mp9)
mp9['迪迦']='奥特曼'
print(mp9)
mp9['迪迦']='怪兽'          #由此可见,字典具有去重重复键保留最后一个键值的效果
print(mp9)
'''删除'''
del mp9["迪迦"]       #注意:当删除的项目不存在时程序会抛出异常
print(mp9)              #为避免出现异常,应该在删除前加上判断
if '迪迦' in mp9:
    del mp9['迪迦']
print('程序未抛出异常')
'''字典推导式'''
mp10={i:random.randint(10,100) for i in range(1,5)}
print(mp10)
mp11={i:j for i,j in enumerate((2,3,4,5,6))}
print(mp11)