#!/usr/bin/env python
#-*- coding: utf-8 -*-  
#coding=utf-8
#Create by shengjk1 on  2017/6/7
import re

rex=r'a.d'
original_str='and'
pattern=re.compile(rex)
m=pattern.match(original_str)
m=re.match(r'a.d','and')
print m;
'''
基本元字符

.：匹配除换行符以外的任意一个字符，例如："a.c" 可以完全匹配 "abc"，也可以匹配 "abcef" 中的 "abc"
\： 转义字符，使特殊字符具有本来的意义，例如： 1\.2 可以匹配 1.2
[...]：匹配方括号中的任意一个字符，例如：a[bcd]e 可以匹配 abe、ace、ade，它还支持范围操作，比如：a到z可表示为 "a-z"，0到9可表示为 "0-9"，注意，在 "[]" 中的特殊字符不再有特殊意义，就是它字面的意义，例如：[.*]就是匹配 . 或者 *
[^...]，字符集取反，表示只要不是括号中出现的字符都可以匹配，例如：a[^bcd]e 可匹配 aee、afe等
>>> re.match(r"a.c", "abc").group()
'abc'
>>> re.match(r"a.c", "abcef").group()
'abc'
>>> re.match(r"1\.2", "1.2").group()
'1.2'
>>> re.match(r"a[0-9]b", "a2b").group()
'a2b'
>>> re.match(r"a[0-9]b", "a5b11").group()
'a5b'
>>> re.match(r"a[.*?]b", "a.b").group()
'a.b'
>>> re.match(r"abc[^\w]", "abc!123").group()
'abc!
group 方法返回原字符串(abcef)中与正则表达式相匹配的那部分子字符串(abc)，提前是要匹配成功 match 方法才会返回 Match 对象，进而才有group方法。

预设元字符

\w 匹配任意一个单词字符，包括数字和下划线，它等价于 [A-Za-z0-9_]，例如 a\wc 可以匹配 abc、acc
\W 匹配任意一个非单词字符，与 \w 操作相反，它等价于 [^A-Za-z0-9_]，例如： a\Wc 可匹配 a!c
\s 匹配任意一个空白字符，空格、回车等都是空白字符，例如：a\sc 可以配 a\nc，这里的 \n表示回车
\S 匹配任意一个非空白字符
\d 匹配任意一个数字，它等价于[0-9]，例如：a\dc 可匹配 a1c、a2c ...
\D 匹配任意一个非数字
边界匹配

边界匹配相关的符号专门用于修饰字符。

^ 匹配字符的开头，在字符串的前面，例如：^abc 表示匹配 a开头，后面紧随bc的字符串，它可以匹配 abc
$ 匹配字符的结尾，在字符串的末尾位置，例如： hello$
>>> re.match(r"^abc","abc").group()
'abc'
>>> re.match(r"^abc$","abc").group()
'abc'
重复匹配

前面的元字符都是针对单个字符来匹配的，如果希望匹配的字符重复出现，比如匹配身份证号码，长度18位，那么就需要用到重复匹配的元字符

* 重复匹配零次或者更多次
? 重复匹配零次或者一次
+ 重复匹配1次或者多次
{n} 重复匹配n次
{n,} 重复匹配至少n次
{n, m} 重复匹配n到m次
# 简单匹配身份证号码，前面17位是数字，最后一位可以是数字或者字母X
>>> re.match(r"\d{17}[\dX]", "42350119900101153X").group()
'42350119900101153X'

# 匹配5到12的QQ号码
>>> re.match(r"\d{5,12}$", "4235011990").group()
'4235011990'
逻辑分支

匹配一个固定电话号码，不同地区规则不一样，有的地方区号是3位，电话是8位，有的地方区号是4位，电话为7位，区号与号码之间用 - 隔开，如果应对这样的需求呢？这时你需要用到逻辑分支条件字符 |，它把表达式分为左右两部分，先尝试匹配左边部分，如果匹配成功就不再匹配后面部分了，这是逻辑 "或" 的关系

# abc|cde 可以匹配abc 或者 cde，但优先匹配abc
>>> re.match(r"aa(abc|cde)","aaabccde").group()
'aaabc'
0\d{2}-\d{8}|0\d{3}-\d{7} 表达式以0开头，既可以匹配3位区号8位号码，也可以匹配4位区号7位号码

>>> re.match(r"0\d{2}-\d{8}|0\d{3}-\d{7}", "0755-4348767").group()
'0755-4348767'
>>> re.match(r"0\d{2}-\d{8}|0\d{3}-\d{7}", "010-34827637").group()
'010-34827637'
分组

前面介绍的匹配规则都是针对单个字符而言的，如果想要重复匹配多个字符怎么办，答案是，用子表达式（也叫分组）来表示，分组用小括号"()"表示，例如 (abc){2} 表示匹配abc两次， 匹配一个IP地址时，可以使用 (\d{1,3}\.){3}\d{1,3}，因为IP是由4组数组3个点组成的，所有，前面3组数字和3个点可以作为一个分组重复3次，最后一部分是一个1到3个数字组成的字符串。如：192.168.0.1。

关于分组，group 方法可用于提取匹配的字符串分组，默认它会把整个表达式的匹配结果当做第0个分组，就是不带参数的 group() 或者是 group(0)，第一组括号中的分组用group(1)获取，以此类推

>>> m = re.match(r"(\d+)(\w+)", "123abc")
＃分组０，匹配整个正则表达式
>>> m.group()
'123abc'
#等价
>>> m.group(0)
'123abc'
# 分组1，匹配第一对括号
>>> m.group(1)
'123'
# 分组2，匹配第二对括号
>>> m.group(2)
'abc'
>>>
通过分组，我们可以从字符串中提取出想要的信息。另外，分组还可以通过指定名字的方式获取。

# 第一个分组的名字是number
# 第二个分组的名字是char
>>> m = re.match(r"(?P<number>\d+)(?P<char>\w+)", "123abc")
>>> m.group("number")
'123'
# 等价
>>> m.group(1)
'123'
贪婪与非贪婪

默认情况下，正则表达式重复匹配时，在使整个表达式能得到匹配的前提下尽可能匹配多的字符，我们称之为贪婪模式，是一种贪得无厌的模式。例如： r"a.*b" 表示匹配 a 开头 b 结尾，中间可以是任意多个字符的字符串，如果用它来匹配 aaabcb，那么它会匹配整个字符串。

>>> re.match(r"a.*b", "aaabcb").group()
'aaabcb'
有时，我们希望尽可能少的匹配，怎么办？只需要在量词后面加一个问号" ？"，在保证匹配的情况下尽可能少的匹配，比如刚才的例子，我们只希望匹配 aaab，那么只需要修改正则表达式为 r"a.*?b"

>>> re.match(r"a.*?b", "aaabcb").group()
'aaab'
>>>
非贪婪模式在爬虫应用中使用非常频繁。比如之前在公众号「Python之禅」曾写过一篇爬取网站并将其转换为PDF文件的场景，在网页上涉及img标签元素是相对路径的情况，我们需要把它替换成绝对路径

>>> html = '<img src="/images/category.png"><img src="/images/js_framework.png">'

# 非贪婪模式就匹配的两个img标签
# 你可以改成贪婪模式看看可以匹配几个
>>> rex = r'<img.*?src="(.*?)">'
>>> re.findall(rex, html)
['/images/category.png', '/images/js_framework.png']
>>>
>>> def fun(match):
...     img_tag = match.group()
...     src = match.group(1)
...     full_src = "http://foofish.net" + src
...     new_img_tag = img_tag.replace(src, full_src)
...     return new_img_tag
...
>>> re.sub(rex, fun, html)
<img src="http://foofish.net/images/category.png"><img src="http://foofish.net/images/js_framework.png">
sub 函数可以接受一个函数作为替换目标对象，函数返回值用来替换正则表达式匹配的部分，在这里，我把整个img标签定义为一个正则表达式 r''，group() 返回的值是 <img src="/images/category.png">，而 group(1) 的返回值是 /images/category.png，最后，我用 replace 方法把相对路径替换成绝对路径。



正则表达式是一种更为强大的字符串匹配、字符串查找、字符串替换等操作工具。上篇讲解了正则表达式的基本概念和语法以及re模块的基本使用方式，这节来详细说说 re 模块作为 Python 正则表达式引擎提供了哪些便利性操作。

 >>> import re
正则表达式的所有操作都是围绕着匹配对象(Match)进行的，只有表达式与字符串匹配才有可能进行后续操作。判断匹配与否有两个方法，分别是 re.match() 和 re.search()，两者有什么区别呢？

re.match(pattern, string)

match 方法从字符串的起始位置开始检查，如果刚好有一个子字符串与正则表达式相匹配，则返回一个Match对象，只要起始位置不匹配则退出，不再往后检查了，返回 None

>>> re.match(r"b.r", "foobar")   # 不匹配
>>> re.match(r"b.r", "barfoo")   # 匹配
<_sre.SRE_Match object at 0x102f05b28>
>>>
re.search(pattern, string)

search 方法虽然也是从起始位置开始检查，但是它在起始位置不匹配的时候会一直尝试往后检查，直到匹配为止，如果到字符串的末尾还没有匹配，则返回 None

>>> re.search(r"b.r", "foobar") # 匹配
<_sre.SRE_Match object at 0x000000000254D578>
>>> re.match(r"b.r", "foobr")  # 不匹配
两者接收参数都是一样的，第一个参数是正则表达式，第二个是预匹配的字符串。另外，不管是 search 还是 match，一旦找到了匹配的子字符串，就立刻停止往后找，哪怕字符串中有多个可匹配的子字符串，例如

>>> re.search(r"f.o", "foobarfeobar").group()
'foo'
两者的差异使得他们在应用场景上也不一样，如果是检查文本是否匹配某种模式，比如，检查字符串是不是有效的邮箱地址，则可以使用 match 来判断：

>>> rex = r"[\w]+@[\w]+\.[\w]+$"
>>> re.match(rex, "123@qq.com")  # 匹配
<_sre.SRE_Match object at 0x102f05bf8> 
>>> re.match(rex, "the email is 123@qq.com") # 不匹配
>>>
尽管第二个字符串中包含有邮件地址，但字符串整体不能当作一个邮件地址来使用，在网页上填邮件地址时，显然第二种写法是无效的。

通常，search 方法可用于判断字符串中是否包含有与正则表达式相匹配的子字符串，还可以从中提出匹配的子字符串，例如：

>>> rex = r"[\w]+@[\w]+\.[\w]+"
>>> m = re.search(rex, "the email is 123@qq.com .")
>>> m is None
False
>>> m.group()
'123@qq.com'
>>>
细心的你可能已经发现了，上面例子与前面例子的正则表达式写法有细微区别，前者多一个元字符 $，它的目的是用于完全匹配字符串。因为不加 $，那么下面这种情况用match方法也匹配，显示这在表单验证时是无法满足要求的。

>>> rex = r"[\w]+@[\w]+\.[\w]+"
>>> re.match(rex, "123@qq.com is my email")
<_sre.SRE_Match object at 0x10cadebf8>
>>>
那么有没有可能不加$，就可以判断是否完全匹配字符串呢？在 Python3 中，re.fullmatch 就可以满足这样的需求。

>>> rex = r"[\w]+@[\w]+\.[\w]+"
>>> re.fullmatch(rex, "123@qq.com is my email") # 不匹配
>>> re.fullmatch(rex, "123@qq.com") # 匹配
<_sre.SRE_Match object; span=(0, 10), match='123@qq.com'>
虽然二者都可以通过 group() 提取出匹配的子字符串，但是，如果字符串中有多个匹配的子字符串时，两个方法都不行，因为它们都是在一旦匹配了第一个子字符串，就不再往后匹配了。

>>> m = re.search(rex, "email is 123@qq.com, anthor email is abc@gmail.com !")
>>> m.group()
'123@qq.com'
那么如何把文本中的所有匹配的邮件地址提取出来呢？re 模块为我们准备了 re.findall() 和 re.finditer() 这两个方法，它们会返回文本中所有与正则表达式相匹配的内容。前者返回的是一个列表(list)对象，后者返回的是一个迭代器(iterator)。

re.findall(pattern, string)

>>> emails = re.findall(rex, "email is 123@qq.com, anthor email is abc@gmail.com")
>>> emails
['123@qq.com', 'abc@gmail.com']
findall 返回的对象是由匹配的子字符串组成的列表，它返回了所有匹配的邮件地址。

re.finditer(pattern, string)

>>> emails = re.finditer(rex, "email is 123@qq.com, anthor email is abc@gmail.com")
>>> emails
<callable-iterator object at 0x0000000002592390>
>>> for e in emails:
...     print(e.group())
...
123@qq.com
abc@gmail.com
finditer 返回的对象是由 Match 对象组成的迭代器，因为里面的元素是Match对象，所以要获取里面的邮件地址还需要调用group方法来提取。关于列表和迭代器的区别，此文不做介绍，可以查看公众号“Python之禅”的历史文章。

re.split

我们都知道字符串有一个split方法，可根据某个子串分隔字符串，如：

>>> "this is a string.".split(" ")
['this', 'is', 'a', 'string.']
但该方法有一个缺陷，比如上面的字符串，根据空格分隔字符串时，字符串后面多一个点，如果用 re.split 就可以避免这种情况。

>>> words = re.split(r"\W+", "this is a string.")
>>> words
['this', 'is', 'a', 'string', '']
>>> list(filter(lambda x: x, words))
['this', 'is', 'a', 'string']
>>>
re.split是一种更为高级的字符串分隔操作的方法。在这里，split根据非字母正则来分隔字符串，但凡是 string.split 没法处理的问题，可以考虑使用re模块下的split方法来处理。此外，正则表达式中如果有分组括号，那么返回结果又不一致，这个可以留给大家查阅文档，某些场景用得着。

re.sub(pattern, repl, string)

re.split是一种更为高级的字符串分隔操作的方法。在这里，split根据非字母正则来分隔字符串，但凡是 string.split 没法处理的问题，可以考虑使用re模块下的split方法来处理。此外，正则表达式中如果有分组括号，那么返回结果又不一致，这个可以留给大家查阅文档，某些场景用得着。

把所有邮箱地址替换成 admin@qq.com

>>> rex = r"[\w]+@[\w]+\.[\w]+" # 邮件地址正则
>>> re.sub(rex, "admin@qq.com", "234@qq.com, 456@qq.com ")
'admin@qq.com, admin@qq.com '
>>>
另外一个例子，就是上次讲过的将 img 标签的 src 路径替换成绝对完整的URL地址

html = """
        ...
        <img src="/images/category.png">
        this is anthor words
        <img src="http://foofish.net/images/js_framework.png">
       """
如果用字符串的replace方法是没法实现了，这时需要用到正则表达式的 re.sub，正则表达式应用了非贪婪模式，使用了一个分组，用于提取 src 的路径。

rex = r'.*?<img src="(.*?)".*?>'
这里我们要把替换目标 repl 作为函数来处理。

def fun(m):
    img_tag = m.group()
    src = m.group(1)
    if not src.startswith("http:"):
        full_src = "http://foofish.net" + src
    else:
        full_src = src
    new_img_tag = img_tag.replace(src, full_src)
    return new_img_tag
引擎会自动把所有匹配的结果应用到该函数中，函数的参数就是每一个匹配的Match对象，通过 group(1) 提取分组后判断是否为一个完整的URL路径，只有是不完整的我们才替换，否则还是按照原来的方式返回。

new_html = re.compile(rex).sub(fun, html)
print(new_html)
# 输出
...
<img src="http://foofish.net/images/category.png">
this is anthor words
<img src="http://foofish.net/images/js_framework.png">
如果还想知道替换次数是多少，那么可以使用 re.subn方法，这个方法具体使用可以参考文档，留着读者自己思考。

此外，以上方法都有一个默认的 flag 参数，该参数用于改变匹配的行为，常用的可选值有：

re.I(IGNORECASE): 忽略大小写（括号内的单词为完整写法，两种方式都支持）
re.M(MULTILINE): 多行模式，改变'^'和'$'的行为
re.S(DOTALL): 改变'.'的行为，默认 . 只能匹配除换行之外的字符，加上它就可以匹配换行了 例如：
>>> re.match(r"foo", "FoObar", re.I)
<_sre.SRE_Match object; span=(0, 3), match='FoO'>
>>>
以上介绍的都是 re 模块下面的方法，其实，这些只不过是一些简便方法，例如 re.match 方法

re.match(r'foo', 'foo bar')
等价于

pattern = re.compile(r'foo')
pattern.match('foo bar')
那么，后者有什么好处呢？为了提高正则匹配的速度，它可以重复利用正则对象，如果一个正则表达式需要匹配多个字符串，那么就推荐后者，先编译在去匹配。更多使用方式可以参考文档 https://docs.python.org/3/library/re.html

'''

