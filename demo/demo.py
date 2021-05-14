'''
print('hello world')
a=10
print("这是变量：",a)
#变量可以是任何数据类型，变量名必须是大小写字母、数字和下划线（_）组成，不能以数字开头
import keyword
r=keyword.kwlist
print(r)
'''

'''
print('我的名字是%s,我的国籍是%s'%("小陈","中国"))
age=20
print("我的年龄是%d岁"%age)


print("aaa","bbb","ccc")
print("www","baidu","com",sep='.')  #sep表示分割
print('hello',end='')
print('world',end='\t')  #\t加空格
print('python',end='\n') #\n换行
print('end')

'''

'''
#输入输出

password=input('请输入密码：')
print('您刚刚输入的密码是：%s'  %password)
print(type(password))

'''
'''
if判断条件1：     #条件后接：
   执行语句1
elif 判断条件2：
     执行语句2
else:
执行语句3
'''

'''
if True:
    print('True')   #同一层级下，缩进要统一
else:
    print('False')
print('end')        #回到与if同一个层级
'''
'''
score=77
if score>=90:
    print('成绩等级为：A')
else :
    if score>=60 and score<=90:
        print('成绩等级为:B')
    else :
        print('成绩等级为：C')
'''

'''
import random
x=random.randint(66,130)
print(x)
'''

'''
import random
c =input('请输入选择：')
c =int(c)
d =random.randint(0,3)
print(d)
if c<d :
    print('你输了')
else :
    print('你赢了')
'''
'''
for i in range(5,7):  #第一个循环要加：        
    print(i)
for i in range(0,10,3):  #（a,b,c）表示从a-b(不包括b)，c是步长；
    print(i)
'''

'''
for i in range(-10,-100,-30):            #负数步长为负
    print(i)
'''
'''
name ='wuhan'
for x in name:
    print(x)           #换行输出name中的每个字母

    print(x,end='\t')  #将name中的字母输出在同一行   
    
%s	通过str()字符串转换来格式化
%u	无符号的十进制整数
%d	有符号的十进制整数
%o	八进制整数
%x	十六进制整数，小写字母
%X	十六进制整数，大写字母
%e	浮点数字(科学计数法)
%E	浮点数字(科学计数法，用E代替e)
%f	浮点实数
%g	浮点数字(根据值的大小采用%e或%f)
%G	浮点数字(类似于%g)


'''

'''

a=['aa','bb','cc','dd']
for i in range(len(a)):     #循环下标
    print(i,a[i])          #打印下标以及里面的元素
'''

'''
i=0
while i<5:
    print('当前是第%d次循环'%(i+1))
    print('i=%d'%i)
    i+=1
'''

'''
n=100
sum=0
counter =1
while counter   <=n:
    sum = sum + counter
    counter += 1
print('%d'%sum)  
'''
'''
print('%5.2f\n%05.1f\n%-6.1f\n%-7.3f'%(3.14,3.14,3.14,3.14))
'''

'''
print('%c\n%o\n%d\n%x'%(65,65,65,65))    #ASCII码，八进制，十进制，十六进制

'''
'''
print('{0}的天气为{1}'.format('武汉','21'))
'''
'''
a=eval(input('请输入成绩一：'))
b=eval(input('请输入成绩二：'))
c=eval(input('请输入成绩三：'))
d=eval(input('请输入成绩四：'))
ave=(a+b+c+d)/4
print('平均成绩为:%.1f'%ave)
'''
'''
a=eval(input('请输入成绩一：'))
b=eval(input('请输入成绩二：'))
ave=(a+b)
print('平均成绩为：%.1f'%ave)
'''

'''
for i in range(1,100):
    if i%2==0:
        continue   #换break，则输出1，break打破循环，continue跳出当前循环，执行下一次循环
    print(i,end=',')
'''


def

























