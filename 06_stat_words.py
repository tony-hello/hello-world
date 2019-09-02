#统计参数中每个英文单词出现的次数
def stats_text_en(text):
    elements = text.split()

    words = []
    symbols = ',.-*!'

    for element in elements:
        for symbol in symbols:
            #replace返回新的字符串，因此必须要新的字符串
            element = element.replace(symbol,'')
        if len(element) :
            words.append(element)

    #初始化一个counter字典，用来存放单词出现的频次
    counter = {}

    #去重，减少迭代次数
    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)

    #2.从小到大排序输出

    return sorted(counter.items(), key = lambda x:x[1],reverse=True)

#统计参数中每个中文字符出现的次数
def stats_text_cn(text):
    cn_characters = []
     
    for character in text:
         #unicode中中文字符的范围
         if 'u4e00' <= character <= 'u9fff':
             cn_characters.append(character)
    counter = {}

    #减少迭代次数
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(),key = lambda x:x[1],reverse=True)

    


    en_text ='''
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
    Namespaces are one honking great idea -- let's do more of those!
    '''

    cn_text = '''
    李白(701年－762年)，字太白，号青莲居士，唐朝浪漫主义诗人，
    被后人誉为诗仙。祖籍陇西成纪(待考)，出生于西域碎叶城，
    4岁再随父迁至剑南道绵州。李白存世诗文千余篇，
    有《李太白集》传世。762年病逝，享年61岁。..... 查看详情>>
    李白古诗词作品： 《静夜思》 《望庐山瀑布》 《早发白帝城》
    《短歌行》 《怨情》 《古风·庄周梦蝴蝶》 《送内寻庐山女道士李腾空二首》
    《独坐敬亭山》 《鹦鹉洲》 《子夜吴歌冬歌》
    '''

    if __name__ == '__main__':
        en_result = stats_text_en(en_text)
        cn_result = stats_text_cn(cn_text)
        print('英文单词词频==>',en_result)
        print('中文字符词频==>',cn_result)

    
