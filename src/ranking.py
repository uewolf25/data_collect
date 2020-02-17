#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, os.path
import MeCab
from collections import Counter
import pathlib

import graph
import read_write
import file_path


class Ranking():

  def __init__(self, genre: str):
    '''
    コンストラクタ
    genre: ジャンル
    '''
    self.__genre = genre
    self.__path_class = file_path.FilePath(genre)
    self.__text_file_path = self.__path_class.get_category_textfile_path()


  def annalys_documents(self) -> list:
    '''
    Mecabを用いて、取得した文書を解析する。\n

    表層形  品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
    '''
    count_noun = Counter()
    # ファイルを読み書きするクラスのインスタンス生成
    file_class = read_write.ReadWrite()
    # Mecabの用意
    tagger = MeCab.Tagger()
    # テキスト読み込み
    text = file_class.read_text(self.__text_file_path)
    annalys_text = tagger.parse(text)
    for words in annalys_text.split("\n"):
      # 形態素取得(0番目)
      word = words.split("\t")[0]

      if word == "EOS":
        break
      else:
        # １番目の要素以降のまとまり
        words_list = words.split("\t")[1]
        # 品詞の抽出
        part_of_speech = words_list.split(",")[0]
        if part_of_speech == "名詞":
          count_noun[word] += 1
    return count_noun


  def rank_and_freq(self, count_noun: list) -> None:
    '''
    単語の頻度を降順で並べたものに順位をつける。
    '''

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

    graph.graph(rank_list, freq_list, self.__text_file_path)
  

# if __name__ == '__main__':
#   ranking = Ranking("sports")
#   ranking.rank_and_freq( ranking.annalys_documents() )