#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by shengjk1 on  2018/5/10

print(4 + 5 * 7)
print(not 5 < 3)
print('sime\'s')

print('a' + ' b')
print(len("aaaaaaa"))
print("a" * 5)
print('abavcd'[3])

lst_of_random_things = [1, 3, 4, 'a string', True]
print(lst_of_random_things[-1])
print(lst_of_random_things[:2])
print(lst_of_random_things[:])
print('this' in 'this is a string')
print('this ' in 'this is a string')
print(not 'this ' not in 'this is a string')
print(5 not in [1, 2, 3, 4, 5, 6])
print(5 in [1, 2, 3, 4, 5, 6])

a = 'abcf'
# a[2] = 'a'  # 这是错的
print(a[2])


# enumerate,zip

# list是可变的,有序的,字符串是不可变的
my_lst=[1,2,3,4,5,6]
# my_lst[0]="none"
print(my_lst)
print(len(my_lst))
print(max(my_lst))
print(min(my_lst))
print(sorted(my_lst))
print('=========',my_lst.pop())
print(my_lst)

new_str='\n'.join(['fore','aft','starboard','port'])
print(new_str)

letters=['a','a','b','c','d']
letters.append('f')
print(letters[0])

# 元祖  不可变的有序的数据类型，无法向元组中添加项目或者从中删除项目
# 或者直接对元组排序
# 定义元组时小括号是可选的
location=(13.4125,103.86667)
print("Latitude:",location[0])
print("Longitude:",location[1])

dimension=52,40,100
length,width,height=dimension
print("the dimensions are {} x {} x{}".format(length,width,height))

'''
集合 set 去重  {1, 2, 3, 4},无序

你可以对集合执行的其他操作包括可以对数学集合执行的操作。
可以对集合轻松地执行 union、intersection 和 difference 等方法，
并且与其他容器相比，速度快了很多。

pop 随机删除一个元素
'''

numbers=[1,2,3,4,4,3,2,1]
print(set(numbers))

print(1 in set(numbers))


'''
字典  可变得，有序的

elements['carbon'] 不存在会报错
get 不存在返回None 或者给定的值

字典的键必须是不可变的
'''
elements={'hydrogen':1,'helium':2,'carbon':6,1:"qw",1:2}
print(elements['carbon'])
print(elements)
elements['carbon']=3
print(elements)
print(elements.get("a",1))
print('carbon' in elements)


'''
恒等运算符   对象相等
is 
is not

== 比较的元素相等
'''

a=[1,2,3]
b=a
c=[1,2,3]

print("=======")
print(a==b)
print(a is b)
print(a==c)
print(a is c)


elements={"hydrogen":{"number":1,
                      "weight":1.00794,
                      "symbol":"H"},
          "helium":{"number":2,
                    "weight":4.002602,
                    "symbol":"he"}}


print(elements["helium"])


'''
返回一个元组
'''
print(list(zip(['a','b','c'],[1,2,3])))

letters=['a','b','c']
nums=[1,2,3]

for letter,num in zip(letters,nums):
    print("{}:{}".format(letter,num))



'''
返回元组迭代器的内置函数
'''

letters=['a','b','c','d','e']

for i,letter in enumerate(letters):
    print(i,letter)



'''
lambda表达式
'''

def multipy(x,y):
    return x*y

double=lambda x,y:x*y




'''
列式推导
'''
cc=[x**2 for x in range(9) if x % 2 ==0]
print(cc)

