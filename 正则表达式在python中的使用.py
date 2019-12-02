'''
Created on 2019年12月2日

@author: hp
'''
'''上一篇文章介绍了那么多关于正则表达式的用法,现在终于到了python中如何使用正则表达式了,不急,请诸君慢慢来'''
'''
之前在讲字符串时,已经说过了字符串的格式化输出,大家没看的可以看我的上一篇文章
格式化输出时,是含有模式串的,同样的,在python里面,正则表达式就是作为模式串被使用的
如:匹配一个不是字母的一个字符串的正则表达式表示的模式字符串
'[^a-zA-Z]'
再如;匹配一个m开头的单词:
'\bm\w*\b'
上面的模式字符串真的正确吗?事实上,他是错误的,因为一个\表示的是转义字符,需要在加上一个才能表示真正的\
正确写法:
'\\bm\\w*\\b'
python的开发人员考虑到了这样比较麻烦,于是有了简单的写法,即在模式字符串前面加上r或R,这样的话里面的字符就都不需要转义了
所以上面的模式字符串也可以写成如下形式
r'\bm\w*\b'
tip: 并不是所有的反斜杠都需要转义,如^\d{8}$中的反斜杠并不需要转义,因为\d并没有特殊意义.这里还是建议大家都用r或R开头的方式使用原生字符串
'''
# '''使用re模块实现正则表达式'''
# 使用正则表达式,需要导入rm模块
# 即:
# import re
# 1.match()方法
# match()方法用于从字符串的开始处进行匹配,如果在起始位置匹配成功,则返回对象,
# 否则返回None,其语法格式如下:
# re.match(patten,string,[flags])
# pattern表示模式字符串,由要匹配的正则表达式转换而来
# string表示要匹配的字符串
# flags表示标志位,用于控制匹配方式,如是否区分大小写.常用的标志如下
# A或ASCII         对于\w \W \b \B \d \D \s \S只进行ASCII匹配
# I或IGNORECASE    执行不区分大小写的匹配
# M或MULTILINE     将^和$用于包括整的字符串的开始和结尾的每一行(默认情况下,仅适用于整个字符串的开始和结尾处)
# S或DOTALL        使用'.'字符匹配所有字符,包括换行符
# X或VERBOSE       使用模式字符串中未转义的空格和注释
# 例如,匹配字符串是否以mr_开头,不区分大小写,代码如下
import re
pattern=r'mr_\w+'
string='MR_SHOP mr_shop'
match=re.match(pattern,string,re.I)
# 上述方法返回一个Match对象,该对象有如下方法:
# start()方法:返回匹配值的起始位置
# end()       返回匹配值的结束位置
# span()      返回匹配位置的元组
# group()     返回匹配到的字符串
# 还提供了string 属性,用以获取要匹配的字符串
print(match) 
print(match.start(),match.end(),'\n',match.span(),'\n',match.string,'\n',match.group())
# 输出结果:
# <re.Match object; span=(0, 7), match='MR_SHOP'>
# 0 7 
#  (0, 7) 
#  MR_SHOP mr_shop 
#  MR_SHOP
string="abcMR_SHOP mr_shop"
match=re.match(pattern,string,re.I)
print(match)
# 输出结果:
# None
# rm的serch()方法用于在整个字符串中搜索第一个匹配到的值,也就是说,他不在是想
# match()方法一样只匹配字符串最开始的部分,而是遍历整个字符串,一直到匹配到或遍历完为止
# 与match()方法相同,匹配到返回Match对象,否则返回None
# findall()用以查找所有符合的字符串,返回的是一个由Match对象组成的列表,用法与前两个相同
#只是要对findall()方法返回的列表进行遍历从而输出搜寻到的字符串
#例:
pattern=r'mr_\w+'
string='MR_SHOP mr_shop'
ans=re.findall(pattern,string,re.I)
print(ans)
#注意,如果指定的模式字符串中包含分组,则返回与分组匹配的文本列表,如:
pattern=r'[1-9]{1,3}(\.[0-9]{1,3}){3}'
str1='127.0.0.1 192.168.1.66'
ans=re.findall(pattern,str1)
print(ans)  #输出:['.1', '.66']
# 输出与预期的不一致,这是因为当模式字符串中含有分组时,得到的结果会是分组中模式字符串的结果,如果想要对整个模式字符串匹配,应该对整个字符串分组
# 然后在获取结果时只取返回的列表的每一个元素(是一个元组)的第一个元素
pattern=r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
ans=re.findall(pattern,str1)
for x in ans:
    print(x[0])
#输出:127.0.0.1
# 192.168.1.66
'''字符串替换方法sub()'''
# re.sub(pattern, repl, string, count, flags)
# pattern表示模式字符串
# repl表示替换的字符串
# string表示要被查找的原始字符串
# count(可选)表示模式匹配后替换的最大次数,默认值为0,表示替换所有的匹配
# flags(可选)表示标志位,用于控制匹配方式,常用的标志在介绍match()方法时已经介绍过,这里不再列举
pattern=r'1[345678]\d{9}'
string='中奖号码为:84978981 联系电话为:13122782807'
result=re.sub(pattern,'1xxxxxxxxxx', string)
print(result)
'''使用正则表达式分割字符串'''
# re.split(pattern, string, maxsplit, flags)
# maxsplit表示最大拆分多少次(可选)
# flags表示匹配模式(可选)
pattern=r'[?|&]'
url='http://www.mingsoft.com/login.jsp?username="mr"pwd="mrsoft"'
result=re.split(pattern, url)
print(result)
#输出为:['http://www.mingsoft.com/login.jsp', 'username="mr"pwd="mrsoft"']
'''关于正则表达式的介绍以及python中正则表达式的用法就介绍到这里了,笔者也是刚学,如果有不足之处,还请多多包涵'''