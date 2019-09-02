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

#将所有better替换为worse
text = text.replace('better','worse')
print("将字符串中的所有better替换为better==>",text)
print('=======================过滤带有ea的单词=======================')

#2.删除包含ea的单词

#空格切分，返回列表
l1 = text.split()

filtered = []

for word in l1:
    if word.find('ea') < 1:
        filtered.append(word)
print(filtered)


#3.大小写翻转
swapcased = [i.swapcase() for i in filtered]
print('=======================大小写翻转=========================')
print(swapcased)

#4.单词按a--z大小排序
print('=================a--z大小排序')
print(sorted(swapcased))


