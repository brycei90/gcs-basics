import asyncio
import aiohttp

websites = """https://www.youtube.com
https://www.facebook.com
https://www.baidu.com
https://www.yahoo.com
https://www.amazon.com
https://www.wikipedia.org
http://www.qq.com
https://www.google.com
https://www.twitter.com
https://www.live.com
http://www.taobao.com
https://www.bing.com
https://www.instagram.com
http://www.weibo.com
http://www.sina.com.cn
https://www.linkedin.com
http://www.yahoo.co.jp
http://www.msn.com
http://www.uol.com.br
https://www.google.de
http://www.yandex.ru
http://www.hao123.com
https://www.google.co.uk
https://www.reddit.com
https://www.ebay.com
https://www.google.fr
https://www.t.co
http://www.tmall.com
http://www.google.com.br
https://www.360.cn
http://www.sohu.com
https://www.amazon.co.jp
http://www.pinterest.com
https://www.netflix.com
http://www.google.it
https://www.google.ru
https://www.microsoft.com
http://www.google.es
https://www.wordpress.com
http://www.gmw.cn
https://www.tumblr.com
http://www.paypal.com
http://www.blogspot.com
http://www.imgur.com
https://www.stackoverflow.com
https://www.aliexpress.com
https://www.naver.com
http://www.ok.ru
https://www.apple.com
http://www.github.com
http://www.chinadaily.com.cn
http://www.imdb.com
https://www.google.co.kr
http://www.fc2.com
http://www.jd.com
http://www.blogger.com
http://www.163.com
http://www.google.ca
https://www.whatsapp.com
https://www.amazon.in
http://www.office.com
http://www.google.co.id
http://www.youku.com
https://www.example.com
http://www.craigslist.org
https://www.amazon.de
http://www.nicovideo.jp
https://www.google.pl
http://www.soso.com
http://www.bilibili.com
http://www.dropbox.com
http://www.xinhuanet.com
http://www.outbrain.com
http://www.pixnet.net
http://www.alibaba.com
http://www.alipay.com
http://www.chrome.com
http://www.booking.com
http://www.googleusercontent.com
http://www.google.com.au
http://www.popads.net
http://www.cntv.cn
http://www.zhihu.com
https://www.amazon.co.uk
http://www.diply.com
http://www.coccoc.com
https://www.cnn.com
http://www.bbc.co.uk
https://www.twitch.tv
https://www.wikia.com
http://www.google.co.th
http://www.go.com
https://www.google.com.ph
http://www.doubleclick.net
http://www.onet.pl
http://www.googleadservices.com
http://www.accuweather.com
http://www.googleweblight.com
http://www.answers.yahoo.com"""

async def get(url, session):
    try:
        async with session.get(url) as resp:
            data = await resp.read()
            length = len(data)
            print(f"got {url} ({length} bytes)")
            return length
    except Exception:
        print(f"failed {url}")
        return None

async def main(urls):
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(get(u, session) for u in urls))
    print(results)             # [15786, 20345, …, None, …]

urls = websites.split("\n")

asyncio.run(main(urls))