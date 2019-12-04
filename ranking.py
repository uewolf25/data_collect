#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import bs4 
import MeCab
from collections import Counter
import data_collect as dc
import graph

categories = ['sports', 'business', 'general', 'all']
text_files = ['sports.txt', 'goverment.txt', 'society.txt', 'all_genre.txt']
text_folder = ['sports_text', 'business_text', 'general_text', 'all_text']

###############################################
### HTML文書を目的の本文の部分のみスクレイピングし、###
### タグを消して１つの文字列とする。              ###
###############################################
def html_parser():
  # 全てのジャンルの記事を
  all_genre_path = []

  for category_dir, text_file, text_dir in zip(categories, text_files, text_folder):

    # 各ファイルのパスを格納する
    file_path = []
    # ディレクトリの中のファイル一覧を取得
    all_files = os.listdir(category_dir)

    for local_file in all_files:
      file_path.append(os.path.join(category_dir, local_file))
      # all_genre_path.append(os.path.join(category_dir, local_file))

    article_get(file_path, category_dir, text_file, text_dir)
    
    # if dir_name == 'all':
    #   article_get(all_genre_path, text_list)
    # else:
    #   article_get(file_path, text_list)

#############################
### HTML文書から文章を抜き出す ###
#############################
def article_get(file_path, category_dir, text_list, text_dir):

  list_len = len( os.listdir(category_dir) )
  for local_file, count in zip(file_path, range(1,list_len)):
      text = []
      try:
        with open(local_file) as f:
          # pタグの部分だけ抜いてくる
          text = bs4.BeautifulSoup(f, "html.parser").select('p')
      except IOError:
        print('cannot be opened .')
      except UnicodeDecodeError:
        print('{0} is not decoded . (fileNumber: {1})'.format(local_file, count) )

      for item in text:
        article = ''
        # タグ付きの文章のタグを除去し、文字列型に変換
        get_articles = str( item.get_text() )
        article += get_articles
        add_text(article, text_list)
        add_text(article, connect_path(text_dir, local_file, count) )
    # 分析する
    # annalys_documents(text_list)

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


#####################################
###  ###
#####################################
def connect_path(dirs, file, number):
  path = os.getcwd()
  directory = dirs
  return os.path.join( os.path.join(path, directory), directory + str(number) + '.txt' )

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

  rank_and_freq(count_noun, file_text)

#############################################
### 単語の頻度を降順で並べたものに順位をつける。 ###
#############################################
def rank_and_freq(count_noun, file_text):

  # 順位
  rank_num = 1
  # ループ総回数のカウンター
  counter = 1
  # 最小値
  min_num = 1000000
  # グラフで使うための縦軸・横軸のリストをセット
  rank_list = []
  freq_list = []
  
  # 名詞と出現回数を全部出力
  for key, count in count_noun.most_common():

    # 単語の出現回数が同じ場合、順位を同率にしておく #
    if min_num == count: 
      # print( "{0}位 {1} : {2}".format( rank_num, key, str(count) ) )
      # print(str(count))
      rank_list.append(rank_num)
      freq_list.append(count)
    # 出現回数が異なる場合は、裏でループ回数を数えていたnumから値を受け取り順位を更新 #
    elif min_num > count:
      min_num = count
      rank_num = counter
      # print( "{0}位 {1} : {2}".format( rank_num, key, str(count) ) )
      # print(str(count))
      rank_list.append(rank_num)
      freq_list.append(count)
    counter += 1

  graph.graph(rank_list, freq_list, file_text)
  

if __name__ == '__main__':
  html_parser()
  # for text in ['sports.txt', 'goverment.txt', 'society.txt', 'all_genre.txt']:
  #   annalys_documents(text)