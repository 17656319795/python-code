'''
Created on 2019年11月30日

@author: 黄智超
'''
# from random import random, randint
import random
phone=[None]*5
print(phone)
nba=["迪迦奥特曼","泰罗奥特曼","赛文奥特曼","雷欧奥特曼","艾斯奥特曼"]
if "迪迦奥特曼" in nba:
    print("迪迦奥特曼在nba里面")
elif "泰罗":
    print("abc")     
print(len(phone))
print(max(nba))
print(min(nba))
print(nba.__len__())
print(nba.count("泰罗奥特曼"))
print(nba.index("雷欧奥特曼"))
# print(nba.sum)
# print(sum(nba))
lk=[1,2,3,4,5]
print(sum(lk))
ll=[2,4,2,1,3,5]
print(ll.sort(),ll)
print(sorted(ll, key=None, reverse=False))
lie=[random.randint(10,100) for i in range(10)]
print(lie)
newnba=[x*2 for x in nba]
print(newnba)
l2=[x for x in ll if x>3]
print(l2)
