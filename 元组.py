'''
Created on 2019年12月1日

@author: hp
'''
a=(1,2,3) #元组
b=(1,"23",[3,4,5],(6,7,8))
b[2][0]=4
# b[3][0]=7
print(b[2])
# a=input("请输入a")
yuanzu="床前明月光","疑是地上霜","举杯邀明月","对影成三人" #默认元组
print(yuanzu,type(yuanzu))
verse="一片冰心在玉壶",
print(verse,type(verse))
verse=("一片冰心在玉壶")
print(verse,type(verse))
verse=("一片冰心在玉壶",)
print(verse,type(verse))
emptytuple=()   #空元组
print(type(emptytuple))
yuanzu=tuple(x*2 for x in yuanzu)
print(yuanzu)
yuanzu=tuple([1,2,3])
print(yuanzu)
# del yuanzu
# print(yuanzu)
print(yuanzu[:2])
yuanzu=yuanzu+verse
print(yuanzu)
'''元组推导式'''
yuanzu=(x for x in [0,1,2,3,4]) #'''生成器对象'''
yuanzu2=yuanzu
print(type(yuanzu),type(yuanzu2))
aa=list(yuanzu2)
print(aa)
bb=tuple(yuanzu)
print(bb)
yuanzu=(x for x in [1,2,3,4,5,7])
print(yuanzu.__next__())
yuanzu=tuple(yuanzu)
print(yuanzu)
yuanzu=(x for x in [1,2,3,4,5])
print(yuanzu.__next__())
