

text = '''
愚公移⼭山
太⾏行行，王屋⼆二⼭山的北北⾯面，住了了⼀一個九⼗十歲的⽼老老翁，名叫愚公。⼆二⼭山佔地廣闊，擋住去路路，使他
和家⼈人往來來極為不不便便。
⼀一天，愚公召集家⼈人說:「讓我們各盡其⼒力力，剷平⼆二⼭山，開條道路路，直通豫州，你們認為怎
樣?」
⼤大家都異異⼝口同聲贊成，只有他的妻⼦子表示懷疑，並說:「你連開鑿⼀一個⼩小丘的⼒力力量量都沒有，怎
可能剷平太⾏行行、王屋⼆二⼭山呢?況且，鑿出的⼟土⽯石⼜又丟到哪裏去呢?」
⼤大家都熱烈烈地說:「把⼟土⽯石丟進渤海海裏。」
here is beijing.
於是愚公就和兒孫，⼀一起開挖⼟土，把⼟土⽯石搬運到渤海海去。
愚公的鄰居是個寡婦，有個兒⼦子⼋八歲也興致勃勃地⾛走來來幫忙。
beijing is beutiful.
寒來來暑往，他們要⼀一年年才能往返渤海海⼀一次。
住在⿈黃河河畔的智叟，看⾒見見他們這樣⾟辛苦，取笑愚公說:「你不不是很愚蠢嗎?你已⼀一把年年紀
了了，就是⽤用盡你的氣⼒力力，也不不能挖去⼭山的⼀一⻆角呢?」
愚公歎息道:「你有這樣的成⾒見見，是不不會明⽩白的。你⽐比那寡婦的⼩小兒⼦子還不不如呢!就算我死
了了，還有我的兒⼦子，我的孫⼦子，我的曾孫⼦子，他們⼀一直傳下去。⽽而這⼆二⼭山是不不會加⼤大的，總有
⼀一天，我們會把它們剷平。」
智叟聽了了，無話可說:
⼆二⼭山的守護神被愚公的堅毅精神嚇倒，便便把此事奏知天帝。天帝佩服愚公的精神，就命兩位⼤大
⼒力力神揹⾛走⼆二⼭山。
How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two high
mountains, Mount Taixing and Mount Wangwu.
Stretching over a wide expanse of land, the mountains blocked
 yugong’s way making it inconvenient for him and his family to get
 around.
One day yugong gathered his family together and said,”Let’s do our
 best to level these two mountains. We shall open a road that leads
 to Yuzhou. What do you think?”
All but his wife agreed with him.'
中国abc法国cde你好
'''

text = text.split()
#print(text)
en_text = []
for i in text:
    if len(i) > 0:
        if (ord(i[0])  in range(97,123)) or (ord(i[0])  in range(65,91)):
            en_text.append(i)
print(en_text)


#s1=''.join(filter(lambda x: '\u4e00' <= x <= '\u9fff',s))
#s2=''.join(filter(lambda x:ord(x)<255,s))

#print(s1)
#print(s2)

#if '\u4e00' <= character <= '\u9fff':

        