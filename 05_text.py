text='''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
 it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

#1.使用dict统计text中的英文单词出现频率
elements = text.split()

words = []
symbols = ',.-*!'

for element in elements:
    for symbol in symbols:
        #replace返回新的字符串，因此必须要新的字符串
        element = element.replace(symbol,'')
    if len(element) :
        words.append(element)
print('==============过滤特殊字符后的正常的单词列表====================')
print('正常的英文单词==>',words)

#初始化一个counter字典，用来存放单词出现的频次
counter = {}

#去重，减少迭代次数
word_set = set(words)

for word in word_set:
    counter[word] = words.count(word)
print("单词出现的频次==>",counter)

#2.从小到大排序输出

print('按照出现频次从小到大排序==>',sorted(counter.items(), key = lambda x:x[1],reverse=True))







