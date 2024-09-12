import requests
from lxml import etree


url='https://www.baidu.com/s?wd=中秋节'
headers={
    'Cookie': 'BIDUPSID=5B1DFD3B99B5065DF1522F28819214A1; PSTM=1655266634; sug=0; sugstore=0; BAIDUID=5B1DFD3B99B5065DE2679BE9363853F4:SL=0:NR=10:FG=1; ORIGIN=2; bdime=0; BD_UPN=12314753; BDUSS=FjdE1JMlRSaG9JQ1lKVzRqb2tZSUQ1VDlySTlzczA1UE84ZVZrLTNLc2xzSzVqRVFBQUFBJCQAAAAAAAAAAAEAAAB-NgnqTG9zZU5pbmUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACUjh2MlI4djVV; BDUSS_BFESS=FjdE1JMlRSaG9JQ1lKVzRqb2tZSUQ1VDlySTlzczA1UE84ZVZrLTNLc2xzSzVqRVFBQUFBJCQAAAAAAAAAAAEAAAB-NgnqTG9zZU5pbmUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACUjh2MlI4djVV; H_PS_PSSID=37781_36558_37557_37906_36802_37927_37759_37901_26350_37788_37881; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; BAIDUID_BFESS=5B1DFD3B99B5065DE2679BE9363853F4:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=85808g0g84202g25al25a4nk1hp8kjk1g; ZFY=ouVq3lqZ3vGr5vvxToXTzY3:AUOE:B7MMjbbpyBNa3YHs:C; B64_BOT=1; BD_CK_SAM=1; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1669205558,1670065546,1670664897; RT="z=1&dm=baidu.com&si=s43l5qiay2f&ss=lbhreezm&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=vg&hd=ya"; ab_sr=1.0.1_NGNjMmNiODQzZWQyOWE1MDA5N2M1NjhkZDVlMzJkNTlkMTU3NmRjNmFhMWRjZDg1MmZhMDU5NmIxMTIxNWJmYmE3Y2Q4NjhkZDkxZTA2NjIxNmVkYzM0OThhZjRiY2ZiNzIwMWNkMmRkNzJiZGJjNzIzOTA0NTRiZTA2ODU2MDU2Mzg3ZmI1NDk3NWIwMTU5MjgxZGQ2ZGU2Y2RkMzFkODdjNGY3ZjkxNzZjYjQ4MzlkNjhhODA0YjI3NWE4NzE2; shifen[357772686099_3550]=1670666012; BCLID=10045372974471067391; BCLID_BFESS=10045372974471067391; BDSFRCVID=EFkOJeC62lzoAlJjrbI8Uwp7b779G63TH6aV3a3cCtV3rB9_bdLiEG0PKx8g0K4bIVxMogKKyeOTHuDF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSFRCVID_BFESS=EFkOJeC62lzoAlJjrbI8Uwp7b779G63TH6aV3a3cCtV3rB9_bdLiEG0PKx8g0K4bIVxMogKKyeOTHuDF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJ-DoIDytC03qR5gMJ5q-n3HKUrL5t_XbI6y3JjOHJOoDDvHQ4Rcy4LdjG5QhtRCagQBQJoYfU5bqK3PjTtBQT5y3-Aq5lKeKR725-bCt-oIbf7PbMvEQfbQ0-ROqP-jWbnaaxQyBR7JOpvwbfnxybLvQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ht6T2-DA_oC8-fC5P; H_BDCLCKID_SF_BFESS=tJ-DoIDytC03qR5gMJ5q-n3HKUrL5t_XbI6y3JjOHJOoDDvHQ4Rcy4LdjG5QhtRCagQBQJoYfU5bqK3PjTtBQT5y3-Aq5lKeKR725-bCt-oIbf7PbMvEQfbQ0-ROqP-jWbnaaxQyBR7JOpvwbfnxybLvQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ht6T2-DA_oC8-fC5P; H_PS_645EC=b855dTiWQHLnUFNnBWoZIPvHebTwUp2rk0bcZT1nJ1OBxOTZhf8vsjFWwKw; baikeVisitId=c00dd38a-3922-4046-8e1a-ec69d06f40b6; BDSVRTM=250; Hm_lpvt_aec699bb6442ba076c8981c6dc490771=1670666544; COOKIE_SESSION=9_1_8_8_16_53_0_3_6_6_165_28_678311_0_173_0_1670666553_1670665412_1670666380%7C9%233446414_6_1670664833%7C3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
}
html=requests.get(url,headers=headers)
html.encoding='utf8'
#print(html.text)
soup=etree.HTML(html.text)
"""
// 从当前节点或当前子节点开始查找
/  从当前节点开始查找
.  选取当前节点的子节点
..  选取当前节点的父节点
@  选取属性 可以是任意属性
[]  属性选择
严格匹配: 选取精确的节点或属性   必须要一模一样
//div[@class="c-container xpath-log new-pmd"]/h3/a
模糊匹配: 选取包含指定字符串的节点或属性 contains 只要包含就可以
//div[contains(@class,"c-container")]//h3/a

starts-with  选取以指定字符串开头的节点或属性
//div[starts-with(@class,"c-container")]//h3/a

<Element a at 0x2b3a70eed80> PyObject 内存地址
/text()  获取节点的文本内容
/string()  获取节点 及 子节点的文本内容

@href  获取属性值
@data-click  获取属性值
"""
results=soup.xpath('//div[contains(@class,"c-container xpath-log new-pmd")]//h3/a')
for r in results:
    print(r.xpath('string()'),r.xpath("@href"),r.xpath("@data-click"))
