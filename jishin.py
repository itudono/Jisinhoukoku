#!/usr/bin/python
# - coding: utf-8 -

#正規表現、URL取得、HTML整形ライブラリ
import re
import urllib.request
from bs4 import BeautifulSoup

#気象庁地震情報から拾う
url = "http://www.jma.go.jp/jp/quake/index.html"
html = urllib.request.urlopen(url).read()
data = html.decode('utf8')

#必要な部分の取得作業
soup = BeautifulSoup(data, "html.parser")

#calassネームがtextframeの部分だけを持ってくる
textframe = soup.find("table", class_= "textframe")
#その中の、td部分を切り取る
textframe = textframe.find("td")

#切り取った部分からテキストだけを抜き出す
ptext = textframe.getText()
#テキストにある空白文字をすべて消す
seikei = re.sub(r'\s','', ptext, flags=re.UNICODE)
#いらない部分の削除
seikei2 = re.sub(r'なお、＊印は気象庁以外の震度観測点についての情報です。','',seikei, flags=re.UNICODE)
seikei3 = re.sub(r'\&nbsp','',seikei2, flags=re.UNICODE)
seikei4 = re.sub(r'(（北).*(されます。)','で、', seikei3, flags=re.UNICODE)
seikei5 = re.sub(r'(平成).*(気象庁発表)','',seikei4, flags=re.UNICODE)

print(seikei5)
