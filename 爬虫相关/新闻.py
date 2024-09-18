import httpx
import json
from bs4 import BeautifulSoup
import os

client = httpx.Client(http2=True)
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70',
    'referer': 'https://news.163.com/domestic/',
    'cookie': '_ntes_nnid=c793c7df5a6d71683c54cfaa435ec5df,1657424739992; _ntes_nuid=c793c7df5a6d71683c54cfaa435ec5df; Qs_lvt_382223=1657779504; Qs_pv_382223=4251433563490074600; _ga=GA1.1.72473570.1657779505; _ga_C6TGHFPQ1H=GS1.1.1657779504.1.0.1657779505.0; _clck=htg2y8|1|f35|0; __root_domain_v=.163.com; _qddaz=QD.103767222943559; __bid_n=1843dac90e2a56122d4207; NTES_P_UTID=Ys3PrkA1uwnh4hwDiKliRgYiEe3JSyHN|1670315844; nts_mail_user=losenine@163.com:-1:1; FEID=v10-76d4f93d074d9e3e5fc9d8cab279d8531bac8e80; __xaf_fpstarttimer__=1672895306732; __xaf_thstime__=1672895306913; __xaf_fptokentimer__=1672895306964; P_INFO=13520791099|1674994744|1|netease_buff|00&99|null&null&null#shx&140800#10#0|&0||13520791099; NTES_PASSPORT=.29cFj9vPm0izZC0VGj54sWBVDr5sq8EEkO5qin1_lm9YtclYUOmhkQmxB2ukMGKAmMUk.yTJG6MPHt31kvpDclVf8AcTtqoCalliU7yaIJiGhPbsUiGgPjqu4vIDSftdXXHJSbPezCrAYGi8jJjycGOXUQi.Eny3PeeX0DIgpwwydIrQCmemWTG.NGwfY8th; cm_newmsg=user%3Dlosenine%40163.com%26new%3D-1%26total%3D-1; s_n_f_l_n3=9288bb4a750d0af61675494347765; _antanalysis_s_id=1675494348199; BAIDU_SSP_lcr=https://www.bing.com/; pver_n_f_l_n3=a; UserProvince=%u5168%u56FD; FPTOKEN=RSN6XXRlx2xsz51ODRZqsD/ki2494am7PyROe4lB9Hj6Z4nwwtqtqx6HdivZvnMD6TG9Z+q/qOHJfHGzqGBSSM9f+9xEc3ERLLuIauDrX1LIrtntZd13r7ugwlj6yyo72gB3mEzKQZjCwFmlq+301mfiLucW5xJ6LLwhGzSABhpbk0Zdf0j9BJtevYt7i18H5oTkWQ47ql68Zugm+Sl5/Ak0QZjmOgD9mejSVCKN1RFye09iqYxDFr7ecFGM1cRd6Ckk3DoFRLSTvWR/jAYvQ3vA5/o5vmAlaIMpsts8fPkCcpQX1gO2X4OvD654tbVIEN3TlIzaHkihCUM9mMxG0rFc90Ckiv654PcAflp4yZklX6g7DpwstzUlojBKWEK/Um4G7vYDuIE4wr6rhyitmQ==|3ber1qCmSLdnVpZm1c0urO3oeonR1oCSyvDE+PsSEtY=|10|a40f272a607482739f7bfc179d17e838; NTES_PC_IP=%E5%BF%BB%E5%B7%9E%7C%E5%B1%B1%E8%A5%BF; ne_analysis_trace_id=1675495200009; NTES_CMT_USER_INFO=309770907%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B0itHGr%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F2018%2F08%2F13%2F078ea9f65d954410b62a52ac773875a1.jpeg%7Cfalse%7CbG9zZW5pbmVAMTYzLmNvbQ%3D%3D; vinfo_n_f_l_n3=9288bb4a750d0af6.1.2.1659186884554.1675494214526.1675495238759',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}
client.headers=headers
# 用于存储所有文章内容的列表
all_content = []

def innerGet(url, title, imgUrl, source):
    html = client.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    content = soup.select('.post_body p')
    myhtml = ''
    for p in content:
        myhtml += p.text + '\n'
    print('获取文本',myhtml)

    # 将每篇文章的标题、链接、图片、来源和内容合并到一个字符串
    full_content = f'标题：{title}\n链接：{url}\n图片：{imgUrl}\n来源：{source}\n\n{myhtml}\n' + '-' * 80 + '\n'

    # 添加到all_content列表中
    all_content.append(full_content)

def main():
    for i in range(1, 4):
        if i == 1:
            url = 'https://news.163.com/special/cm_guonei/?callback=data_callback'
        else:
            url = f'https://news.163.com/special/cm_guonei_0{i}/?callback=data_callback'
        print('正在爬取', url)
        html = client.get(url)
        data= html.text.replace('data_callback(', '')[:len(html.text.replace('data_callback(', ''))-1]
        result = json.loads(data)
        for res in result:
            title = res['title']
            innUlr = res['tlink']
            imgUrl = res['imgurl']
            source = res['source']
            print(f'标题：{title}\n链接：{innUlr}\n图片：{imgUrl}\n来源：{source}\n')
            innerGet(innUlr, title, imgUrl, source)
    # 所有文章爬取完成后，将所有内容写入一个文件
    if not os.path.exists('./content'):
        os.mkdir('./content')

    with open('./content/all_articles.txt', 'a+', encoding='utf8') as f:
        for content in all_content:
            f.write(content)

    print('所有文章内容已写入到文件：./content/all_articles.txt')


if __name__ == '__main__':
    main()