#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, os.path
import sys
import math
from natsort import natsorted
import MeCab
from collections import Counter

import file_path
import read_write


class DataSet():

  def __init__(self, genre: str):
    self.__genre = genre
    self.__file_path = file_path.FilePath(genre)
    self.__list = [] # １つ１つの文書について名詞を抽出し格納→二次元配列


  def data_set(self, text_file: str) -> list:
    '''
    1~100文書をそれぞれ名詞のみ抽出してリストに格納する。
    [n番目[名詞]] 重複あり
    '''
    # 重複なしの名詞を格納
    noun_list = []
    # ファイルから読み込んだ文字列を格納
    count_noun = Counter()

    # ファイルを読み書きするクラスのインスタンス生成
    read_write_class = read_write.ReadWrite()
    # Mecabの用意
    tagger = MeCab.Tagger()
    # テキスト読み込み
    text = read_write_class.read_text(text_file)
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
          noun_list.append(word)
    return noun_list



  def text_set(self) -> None:
    '''
    与えられた引数(ジャンル)の単語軍をリストに格納する。
    '''
    files = natsorted( os.listdir(self.__file_path.get_mix_category_dir()) )
    for each_file in files:
      file_path = os.path.join( self.__file_path.get_mix_category_dir() , each_file )
      # print(file_path)
      data_list = self.data_set(file_path)
      self.__list.append(data_list)
    return self.__list
