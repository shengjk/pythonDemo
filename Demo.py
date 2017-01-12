#!/usr/bin/env python
#-*- coding: utf-8 -*-
#coding=utf-8
#Create by shengjk1 on  2017/1/10


if __name__ == '__main__':
#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
    print(ord("A"))
    print(chr(66))
    print('\u4e2d\u6587')#可以用十六进制来表示字符串

    #bytes类型
    print('ABC')
    print(b'ABC')#bytes的每一个字符都占用一个字节

    #通过encode()方法可以编码为指定的bytes
    print("ABC".encode('ascii'))
    print("中文".encode('utf-8'))
    print("ABC".encode('ascii'))
#反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
    print(b"\xe4\xb8\xad\xe6\x96\x87".decode('utf-8'))#将流转化为字符串

    #len
    print(len("ADB"))
    print(len(b"ADB"))#计算的是字节数
    print("===============")
    print(len("中文".encode("utf-8")))#计算的是字节数

    #格式化
    '''
       %d 整数
       %f 浮点数
       %s 字符串
       %x 十六进制整数

       如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
    '''
    print("hello ,%s" % 'world')
    print("hello, %s,you have %d" % ('Michael',10000))
    print("growth rate: %d %%" % 7)

#条件判断
    age=18
    if age>18:
        print("your age is ",age)
    elif age==18:
        print("a")
    else:
        print('else')

    # s=input("birth: ")
    # birth=int(s)
    # if birth<2000:
    #     print("00前")
    # else:
    #     print("00后")

#循环
    names=['Michael','Bib','Tracy']
    for name in names:
        print(name)


    sum=0
    for x in [1,2,3,4,5,6,7,8,9,10]:
        sum=sum+x
    print(sum)

#list(range(5)) [0, 1, 2, 3, 4]  [0,5)前包后不包
    sum=0
    for x in range(101):
        sum=sum+x
    print(sum)

    sum=0
    n=99
    while n>0:
        sum=sum+n
        n=n-2
    print(sum)

#字典
    d={'Michael':95,'Bob':67,'Tracy':85}
    print(d['Michael'])
    print("=================")

    print(d.get("ADF"))#key不存在时也不会报错，默认返回None
    print(d.get("ADF",-1))#key不存在时也不会报错，默认返回None

#set
    s=set([1,1,1,2,3,4,5])
    s.add("s")
    s.remove(1)

    s1=set([1,2,3])
    s2=set([2,3,4])
#交集、并集、合集
    s=s1 & s2
    for x in s:
        print(x)


    #函数
        print(bool(1))
        print(bool(1.01))
        print(bool(True))
        print(bool(1289))
#函数应该是这类语言的相对方便的地方
    def my_abs(x):
        if not isinstance(x,(int,float)):
            raise TypeError('bad operand type ') #相当于java中Throw Exception


        if x>0:
            return x,x
        else:
            return -x,-x
    print(my_abs(-1))

#返回多个值

#函数参数
    def power(x,n=2): #默认参数
        x=1


    def add_end(L=[]):
        L.append('end')
        return L
    #Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
    print(add_end())
    print(add_end())
    print(add_end([1,2,3]))
    print(add_end([1,2,3]))
#关键字参数
    def person(name,age,**kw1):
        print('name:',name,'age:',age,'other:',kw1)
 #关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
    person('Michael',30)
    person('Bob',30,city='Beijing')
#关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求



#命名关键字参数
    #如果要限制关键字参数的名字，就可以用命名关键字参数
    def person1(name,age,*,city,job): #只接受city和job作为关键字参数，这样写的还这两个关键字就是必须的了
        print(name,age,city,job)

    person1('Jack',24,city='Beijing',job='Engineer')


    def person1(name,age,*,city='Beijing',job):#使用命名关键字参数时，要特别注意，*不是参数，而是特殊分隔符
        print(name,age,city,job)

    person1('jack',34,job='Enter')#由于命名关键字参数city具有默认值，调用时，可不传入city参数


#复合参数  参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数
    def f1(a,b,c=2,*args,**kw):
        print(a,b,c,args,kw)

    def f2(a,b,c=2,*,d,**kw):
        print(a,b,c,d,kw)

    f1(1,2)
    f1(2,3,args=(1,2,3),kw={'a':1})
    f1(1,2,3,'a','b')
    f1(1,2,3,4,5,5,56)
    f1(1,2,3,'a','b',a1=32)

    f2(1,2,3,d=10,ext=None)

    '''
    1 2 2 () {}
    2 3 2 () {'kw': {'a': 1}, 'args': (1, 2, 3)}
    1 2 3 ('a', 'b') {}
    1 2 3 (4, 5, 5, 56) {}
    1 2 3 ('a', 'b') {'a1': 32}
    1 2 3 10 {'ext': None}
    '''
#递归函数
    def fact(n):
        if n==1:
            return 1
        return n*fact(n-1)

    print(fact(1))



#迭代 Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上
    d={'a':1,'b':2,'c':4}
    for key in  d:
        print(key)

    for value in d.values():
        print(value)

    for k,v in d.items():
        print(k +'=>'+str(v))

#下标迭代
    for i,value in enumerate(['a','b','c']):
        print(i,value)

    for x,y in [(1,1),(2,2)]:
        print(x,y)


#列表生成式
    list(range(1,11)) #[1,11)
    [x *x for x in range(1,11)]
    [x * x for x in range(1,11) if x %2==0] #觉得好像scala的语法，函数式编程互通的地方
    [x * x for  x in range(1,11) if x %2==0]
    [m+n for m in 'ABC' for n in 'XYZ'] #可以理解为java8的内循环，效率要比for循环(外循环)快的多

    import os
    [d for d in  os.listdir('.')]

    L = ['Hello', 'World', 'IBM', 'Apple']
    [s.lower() for s in L]

#生成器
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator
    print([x * x for x in  range(10)])
    print((x *x for x in range(10)))
    print(next(x * x for x in range(10)))
    print(next(x * x for x in range(10)))
    print(next(x * x for x in range(10)))#next越界 StopIteration
    g=(x * x for x in range(1,10))
    for n in g:
        print(n)
