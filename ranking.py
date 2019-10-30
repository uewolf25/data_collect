#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import bs4 
import re
import Mecab

###########################################
# HTML文書を目的の本文の部分のみスクレイピングし、#
# タグを消して１つの文字列とする。              #
###########################################
def html_parser():

  article = ''

  with open('file/index.html.1.html') as f:

    text = bs4.BeautifulSoup(f, "html.parser").select('p')
    for item in text:
      get_articles = str( item.get_text() )
      article += get_articles
    print(article)

    # 全部は出力しないmax36
    # soup = bs4.BeautifulSoup(f, "html.parser").contents[3]
    # print(soup)

    # .get_text()でタグを全て非表示で文章のみ表示させる。
    # soup = bs4.BeautifulSoup(f, "html.parser")
    # print(soup.get_text())

if __name__ == '__main__':
  html_parser()
