#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, os.path
import sys
import math
from natsort import natsorted
import MeCab
from collections import Counter
import ranking

categories = ranking.categories
text_files = ranking.text_files
categories_text_dir = ['sports_text', 'business_text', 'general_text']

# 各文書の名詞を格納する
sports_list, business_list, general_list = [], [], []


def data_set(text_file: str) -> list:
  '''
  1~100文書をそれぞれ名詞のみ抽出してリストに格納する。
  [n番目[名詞]]
  '''
  # 重複なしの名詞を格納
  noun_list = []
  # ファイルから読み込んだ文字列を格納
  text = ''
  count_noun = Counter()
  try:
    f = open(text_file, 'r', encoding='utf8', errors='ignore')
  except IOError:
    print('cannot be opend .')
  except UnicodeDecodeError:
    print('{0} is not decoded .'.format(text_file) )
  else:
    text = f.read()
    f.close()

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
        noun_list.append(word)
  return noun_list



def text_set(genre: str) -> None:
  '''
  与えられた引数(ジャンル)の単語軍をリストに格納する。
  '''
  # genre_dir = sports_list
  files = natsorted( os.listdir('../sports_text') )
  for each_file in files:
    file_path = os.path.join( '../sports_text' , each_file )
    # print(file_path)
    data_list = data_set(file_path)
    # print(data_list)
    sports_list.append(data_list)


def calc(genre: str, string: str) -> None:
  '''
  実際にtf-idfを計算する関数
  ToDo:リストに格納されているものの重複をset()で消す
  '''
  # tf値を格納する用のリスト
  tf_list = []
  # 1ジャンルの全ファイル数(100つ)
  file_name = natsorted( os.listdir(genre) )
  file_number = len( file_name )

  idf_value_count = 0
  # リストに格納されているファイル内の単語と名前を一緒に回す
  for word, name in zip(sports_list, file_name):
    # 単語数
    word_length = len(word)
    # １ファイル内の単語群(リスト)
    devided_word_list = word

    # 何個のファイルに出現したか（idfのため）
    if string in set(devided_word_list):
      idf_value_count += 1
    
    # tf値の計算
    tf(word_length, string, devided_word_list, tf_list)

  idf_value = idf(file_number, idf_value_count+1)
  name, value = tf_idf(file_name, tf_list, idf_value)
  value_sort( name, value, string )
    


def tf(all_words: int, target_word: str, word_list: list, tf_list: list):
  '''
  １つのファイル内にある単語がどれだけ含まれているか。\n
  ・tf = ある単語の出現数(word_freq) / １つのファイルの全体の単語数(all_words)
  '''
  # １つのファイルに何回出現したか
  word_freq = word_list.count(target_word)
  word_freq += 1
  # print('ファイル名：{0}\t単語数：{1}'.format(file_name, all_words))
  try:
    # tf値の計算
    tf_value = word_freq / all_words
  except ZeroDivisionError:
    print('Cannot devide by zero .')
  tf_list.append(tf_value)



def idf(file_number: int, value: int):
  '''
  全ファイル(100個)にある単語が何個のファイルに含まれているか。\n
  ・idf = log( 全ファイル数 / ある単語が出現したファイル数 )
  '''
  return math.log( file_number / value )
  


def tf_idf(file_name: str, tf_list: list, idf: int) -> None:
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


def value_sort(names: list, values: list, string: str):
  '''
  辞書型でファイル名とtf-idf値を紐付け、昇順にソートする。\n
  ソートしたものをテキストに書き込む。
  '''
  # ソートするための辞書
  name_and_value_dictonary = {}
  for name, value in zip(names, values):
    name_and_value_dictonary[name] = value

  # ソート
  sorted_values = sorted(name_and_value_dictonary.items(), key=lambda value:value[1], reverse=True)
  # 出力するファイル名
  text_file = '../ranking_tfidf_value_' + string + '.txt'
  for key, value in sorted_values:
    # print(key + ' :\t' + str(value))
    #　テキストに書き込み
    try:
      f = open(text_file, 'a')
    except IOError:
      print('cannot be opened .')
    else:
      f.write('{0}:\t{1}\n\n'.format( key, str(value) ))
      f.close()
  print('Add ranking file .')



def input_check(string: str) -> str:
  '''
  入力されたジャンルが存在するかの判定。
  '''
  if string == 'sports' or string == '1':
    return 'sports', '../sports_text'
  elif string == 'goverment' or string == '2':
    return 'business', '../business_text'
  elif string == 'society' or string == '3':
    return 'general', '../general_text'
  else:
    print('選択されたジャンルが存在しません。\nプログラムを終了します。')
    sys.exit()


if __name__ == '__main__':
  input_genre = input(
    '1. sports\n'
    '2. goverment\n'
    '3. society\n\n'
    'select genre or number >>> '
    )
  genre, genre_text = input_check(input_genre)
  string = input('input words >>> ')

  text_set(genre)
  calc(genre_text, string)
  # text_all_set()