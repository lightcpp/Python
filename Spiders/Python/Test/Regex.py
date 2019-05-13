#-*- coding:utf-8 -*-
'''
Created on 2019年5月10日

@author: Light
'''
import re

if __name__ == '__main__':
# 正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑
#     （1）数量词的贪婪模式与非贪婪模式
# 正则表达式通常用于在文本中查找匹配的字符串。Python里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符；非贪婪的则相反，总是尝试匹配尽可能少的字符。例如：正则表达式”ab*”如果用于查找”abbbc”，将找到”abbb”。而如果使用非贪婪的数量词”ab*?”，将找到”a”。
# 
# 注：我们一般使用非贪婪模式来提取
#     example = "<div>test1</div><div>test2</div>"
#     greedPattern = re.compile("<div>.*</div>*")
#     notGreedPattern = re.compile("<div>.*?</div>")
#     
#     greedResult = greedPattern.search(example)
#     notGreedResult = notGreedPattern.search(example)
#     
#     print("greedResult = %s" % greedResult.group())
#     print("notGreedResult = %s" % notGreedResult.group())

# （2）反斜杠问题
# 与大多数编程语言相同，正则表达式里使用”\”作为转义字符，这就可能造成反斜杠困扰。假如你需要匹配文本中的字符”\”，那么使用编程语言表示的正则表达式里将需要4个反斜杠”\\\\”：前两个和后两个分别用于在编程语言里转义成反斜杠，转换成两个反斜杠后再在正则表达式里转义成一个反斜杠。
# 
# Python里的原生字符串很好地解决了这个问题，这个例子中的正则表达式可以使用r”\\”表示。同样，匹配一个数字的”\\d”可以写成r”\d”
#     example = "abb\\bbcc"
#     pattern = re.compile(r"\\b.*")
#     result = pattern.search(example)
#     print example
#     print result.group()
    
#     Re模块
#     re.compile(pattern, flags)
#     参数flag是匹配模式，取值可以使用按位或运算符’|’表示同时生效，比如re.I | re.M。
# 可选值有：
#  • re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
#  • re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
#  • re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
#  • re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
#  • re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
#  • re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。
#     （1）re.match(pattern, string[, flags])
#     这个方法将会从string（我们要匹配的字符串）的【开头开始，尝试匹配pattern】，一直向后匹配，【如果遇到无法匹配的字符，立即返回None】，【如果匹配未结束已经到达string的末尾，也会返回None】。两个结果均表示匹配失败，否则匹配pattern成功，同时匹配终止，不再对string向后匹配。下面我们通过一个例子理解一下
    pattern = re.compile(r"hello")
    
    result1 = re.match(pattern, "hello")
    result2 = re.match(pattern,"helloo QWER!")
    result3 = re.match(pattern,"helo QWER!")
    result4 = re.match(pattern,"hello QWER!")
    
    if result1:
        print "result1:"+result1.group()
    if result2:
        print "result2:"+result2.group()
    if result3:
        print "result3:"+result3.group()
    if result4:
        print "result4:"+result4.group()
    
    