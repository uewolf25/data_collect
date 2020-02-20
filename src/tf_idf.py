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


class TfIdf():
  def __init__(self, genre: str, query: str, all_genre_list: list):
    self.__genre = genre
    self.__query = query
    self.__list = all_genre_list
    self.__file_class = file_path.FilePath(self.__genre)


  def calc(self) -> None:
    '''
    tf-idfを計算する関数
    '''
    # tf値を格納する用のリスト
    tf_list = []
    # 1ジャンルの全ファイル数(100つ)
    file_name = natsorted( os.listdir(self.__file_class.get_mix_category_dir()) ) # 区別無しジャンルのディレクトリをソートしたもの
    # print(file_name)
    file_number = len( file_name ) # =選択したジャンル数*100

    # idf値の「どれくらいの数の文書である単語が出現したか」を数えるための変数
    idf_value_count = 0

    # リストに格納されているファイル内の単語とファイル名を一緒に回す
    for word, name in zip(self.__list, file_name):
      # １ファイルの単語数
      word_length = len(word)
      # １ファイル内の単語群(list)
      devided_word_list = word

      # df値の計算 ： 対象のクエリが何個のファイルに出現したか
      if self.__query in set(devided_word_list):
        idf_value_count += 1
      
      # tf値の計算
      self.tf(word_length, devided_word_list, tf_list)
    # idfの計算 (定数)
    idf_value = self.idf(file_number, idf_value_count)
    # ランキングを返す
    return self.tf_idf(file_name, tf_list, idf_value) # file_name_list, tf_idf_value
      


  def tf(self, all_words: int, word_list: list, tf_list: list):
    '''
    １つのファイル内にある単語がどれだけ含まれているか。\n
    ・tf = ある単語の出現数(word_freq) / １つのファイルの全体の単語数(all_words)
    '''
    # １つのファイルに何回出現したか
    word_freq = word_list.count(self.__query)
    word_freq += 1 # スムージング
    # print('ファイル名：{0}\t単語数：{1}'.format(file_name, all_words))
    try:
      # tf値の計算
      tf_value = word_freq / all_words
    except ZeroDivisionError:
      print('Cannot devide by zero .')
    tf_list.append(tf_value)



  def idf(self, file_number: int, value: int):
    '''
    全ファイル(100個)にある単語が何個のファイルに含まれているか。\n
    ・idf = log( 全ファイル数 / ある単語が出現したファイル数 )
    '''
    value += 1 # スムージング
    return math.log( file_number / value )
    


  def tf_idf(self, file_name: str, tf_list: list, idf: float) -> None:
    '''
    tfとidfをかけた値。
    tf * idf
    '''
    tf_idf_list, file_name_list = [], []
    for name, tf in zip(file_name, tf_list):
      tf_idf_value = tf * idf
      # print( 'ファイル名：{0}\n tf値：{1}\tidf値：{2}\ntf-idf値：{3}\n'.format(name, tf, idf, tf_idf_value) )
      file_name_list.append( name )
      tf_idf_list.append( tf_idf_value )
    return file_name_list, tf_idf_list
