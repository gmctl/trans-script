# -*- coding: utf-8 -*-
import urllib.request
import requests
import execjs

PROXY_POOL_SERVER = '218.0.54.152:5010'


def get_proxy():
    return requests.get("http://{}/get/".format(PROXY_POOL_SERVER)).json()

def delete_proxy(proxy):
    requests.get("http://{proxy_pool_server}/delete/?proxy={proxy}".format(proxy=proxy, proxy_pool_server=PROXY_POOL_SERVER))


class GoogleTranslaterTk():
    def __init__(self):
        self.ctx = execjs.compile("""
        function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;

        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";

        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };

    function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
    """)

    def getTk(self, text):
        return self.ctx.call("TL", text)


def fetch_url(url, retry_count=5):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    proxy = get_proxy().get("proxy")
    while retry_count > 0:
        try:
            response = requests.get(url=url, proxies={"http": "http://{}".format(proxy)}, headers=headers)
            data = response.content.decode('utf-8')
            return data
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理 // 并且继续尝试，知道我们搞到了目标为止。
    delete_proxy(proxy)
    return fetch_url(url, retry_count=5)


def translate(content, tk):
    if len(content) > 4891: ##这里可以用try
        print("翻译长度过长;请注意分割")
        return

    content = urllib.parse.quote(content)

    url = "http://translate.google.cn/translate_a/single?client=t" \
          "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
          "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
          "&srcrom=0&ssel=0&tsel=0&kc=2&tk={}&q={}".format(tk, content)
	
    result = fetch_url(url)
    end = result.find("\",")
    if end > 4:
        return result[4:end]


def tranEn2Cn(content):
    js = GoogleTranslaterTk()
    return translate(content, js.getTk(content))
