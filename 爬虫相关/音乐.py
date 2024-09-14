import httpx
from bs4 import BeautifulSoup
import os
import re


def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)


def download_mp3(client, title, url):
    try:
        html = client.get(url)
        data = html.json()

        # 检查 err_code 是否是 20010，表示资源不可用
        if data.get('err_code') == 20010:
            print(f"Resource not available for {title} (Error 20010)")
            return

        # 打印调试信息，查看返回的 JSON 数据结构
        print(f"Fetched data for {title}: {data}")

        if isinstance(data['data'], dict):
            play_url = data['data'].get('play_url')
        elif isinstance(data['data'], list) and data['data']:
            play_url = data['data'][0].get('play_url')
        else:
            print(f"Unexpected data format or no play_url found for {title}")
            return

        if not play_url:
            print(f"No play_url found for {title}")
            return

    except (KeyError, TypeError, httpx.HTTPError) as e:
        print(f"Error accessing or processing data for {title}: {e}")
        return

    if not os.path.exists('./mp3'):
        os.makedirs('./mp3')

    title = sanitize_filename(title)
    mp3_file_path = os.path.join('./mp3', f'{title}.mp3')

    try:
        with open(mp3_file_path, 'wb') as f:
            f.write(client.get(play_url).content)
        print(f"Downloaded: {title}")
    except Exception as e:
        print(f"Error writing file {title}: {e}")


def index(client):
    index_html = 'https://www.kugou.com/yy/html/rank.html'
    try:
        html1 = client.get(index_html)
        soup = BeautifulSoup(html1.text, 'lxml')
        data_flag = soup.select('div.pc_temp_songlist.pc_rank_songlist_short ul li')
    except httpx.HTTPError as e:
        print(f"Error fetching or parsing HTML: {e}")
        return

    for eid in data_flag:
        try:
            data_eid = eid['data-eid']
            title = eid['title']
            mp3_url = f'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&encode_album_audio_id={data_eid}'
            print(f"Fetching: {title}, ID: {data_eid}")
            download_mp3(client, title, mp3_url)
        except KeyError as e:
            print(f"Error extracting data from HTML for {eid}: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
        'cookie': 'kg_mid=ea3b321c894d74b76b67e48b2058b1b0; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1671683830; kg_dfid=08xnIG0VjAdG2L0f2t2WkE9j; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; kg_mid_temp=ea3b321c894d74b76b67e48b2058b1b0; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1671684384',
        'referer': 'https://www.kugou.com/'
    }
    with httpx.Client(headers=headers) as client:
        index(client)


if __name__ == '__main__':
    main()
