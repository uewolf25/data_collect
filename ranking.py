#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import bs4 
import re
import MeCab
from collections import Counter


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
    # print(article)
  annalys_documents(article)

    # 全部は出力しないmax36
    # soup = bs4.BeautifulSoup(f, "html.parser").contents[3]
    # print(soup)

    # .get_text()でタグを全て非表示で文章のみ表示させる。
    # soup = bs4.BeautifulSoup(f, "html.parser")
    # print(soup.get_text())

#####################################################################
# Mecabを用いて、取得した文書を解析する。                                  #
# 表層形  品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音 #
#####################################################################
def annalys_documents(doc):
  noun = ''
  count_noun = Counter()
  text = doc
  tagger = MeCab.Tagger()
  annalys_text = tagger.parse(text)
  for words in annalys_text.split("\n"):
    # 形態素取得(0番目)
    word = words.split("\t")[0]

    if word == "EOS":
      break
    else:
      # １番目の要素以降のまとまり
      words_list = words.split("\t")[1]
      part_of_speech = words_list[:2]
      # 前から２文字目でスライスして「名詞」に合致するか判別
      if part_of_speech == "名詞":
        noun = word
        # print(noun)
        count_noun[noun] += 1
  for key, count in count_noun.most_common():
    print(key + " : " + str(count))
      

if __name__ == '__main__':
  html_parser()
  # annalys_documents()