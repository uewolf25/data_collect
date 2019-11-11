#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import bs4 
import MeCab
from collections import Counter
import data_collect as dc

categories = dc.categories
text_files = dc.text_files

###############################################
### HTML文書を目的の本文の部分のみスクレイピングし、###
### タグを消して１つの文字列とする。              ###
###############################################
def html_parser():

  for dir_name, text_list in zip(categories, text_files):
    # 各ファイルのパスを格納する
    file_path = []
    all_files = os.listdir(dir_name)

    for local_file in all_files:
      file_path.append(os.path.join(dir_name, local_file))
      
    for local_file in file_path:
      # print(dir_name + ' : ' + text)
      try:
        with open(local_file) as f:
          # pタグの部分だけ抜いてくる
          text = bs4.BeautifulSoup(f, "html.parser").select('p')
      except IOError:
        print('cannot be opened .')
      except UnicodeDecodeError:
        print(local_file + ' is cannot be decoded')

      for item in text:
        article = ''
        # タグ付きの文章のタグを除去し、文字列型に変換
        get_articles = str( item.get_text() )
        article += get_articles
        add_text(article, text_list)
    # 分析する
    annalys_documents(text_list)

#####################################
### 取得した文書をテキストに追記していく ###
#####################################
def add_text(str, text_file):
  try:  
    f = open(text_file, 'a')
  except IOError:
    print('cannot be opened .')
  else:
    f.write(str)

#########################################################################
### Mecabを用いて、取得した文書を解析する。                                  ###
### 表層形  品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音 ###
#########################################################################
def annalys_documents(file_text):
  # 名詞収集
  noun = ''
  # ファイルから読み込んだ文字列を格納
  text = ''
  count_noun = Counter()
  try:
    f = open(file_text, 'r')
  except IOError:
    print('cannot be opend .')
  else:
    text = f.read()
    f.close()
  finally:
    print('---------------------------------------')

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
        count_noun[noun] += 1
  # 名詞と出現回数を全部出力
  for key, count in count_noun.most_common():
    print(key + " : " + str(count))

if __name__ == '__main__':
  html_parser()