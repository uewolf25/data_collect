#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, os.path
import sys
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
  # finally:
  #   print('---------------------------------------')

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
      if part_of_speech == "名詞":# and not word in noun_list:
        noun_list.append(word)
  # print( noun_list )
  return noun_list

# def text_all_set() -> None:
#   '''
#   全ジャンルの文書をそれぞれ格納していく。
#   '''

#   for cate_text_dir, cate_dir in zip(categories_text_dir, [sports_list, business_list, general_list]):
#     files = natsorted( os.listdir(cate_text_dir) ) # リストでファイル名が数字順に格納されている。
#     for each_file in files:
#       file_path = os.path.join( cate_text_dir, each_file )
#       # print( file_path )
#       data_list = data_set(file_path)
#       cate_dir.append(data_list)


def text_set(genre: str) -> None:
  # genre_dir = sports_list
  files = natsorted( os.listdir('sports_text') )
  for each_file in files:
    file_path = os.path.join( 'sports_text' , each_file )
    # print(file_path)
    data_list = data_set(file_path)
    # print(data_list)
    sports_list.append(data_list)
  # print(sports_list[0])
  # print(len(sports_list))


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

  for word, name in zip(sports_list, file_name):
    word_length = len(word)
    # print('ファイル名：{0}\t単語数：{1}'.format(name, word_length))
    devided_word_list = word
    purpose_word = devided_word_list.count(string)
    tf_value = purpose_word / word_length
    tf_list.append(tf_value)
    # print(' 選んだ単語 -> \'{0}\'\t 出現頻度：{1}回 \n tf値は{2}\n'.format(string, purpose_word, tf_value) )
    # print('------------------------------------------------------------')
  print(tf_list)

  # tf(file_number, string, genre)
  # idf()
  # tf_idf()



def tf(number: int, word: str, genre: str):
  '''
  １つのファイル内にある単語がどれだけ含まれているか。\n
  ・tf = ある単語の出現数(word_freq) / １つのファイルの全体の単語数(all_words)
  '''
  word_freq = number
  genre_list = [text for text in sports_list]
  all_words = len(genre_list)
  print( len(sports_list), all_words )

  for file_path in genre_list:
    values = 1
    print( 'ファイル名：{0}\ttf値：{1}'.format(file_path, values) )


def idf(select_list: list):
  '''
  全ファイル(100個)にある単語が何個のファイルに含まれているか。\n
  ・idf = log( 全ファイル数 / ある単語が出現したファイル数 )
  '''
  genre_list = set(select_list)


def tf_idf(tf: int, idf: int) -> int:
  '''
  tfとidfをかけた値。
  tf * idf
  '''
  pass


def input_check(string: str) -> str:
  '''
  入力されたジャンルが存在するかの判定。
  '''
  if string == 'sports' or string == '1':
    return 'sports'
  elif string == 'goverment' or string == '2':
    return 'business'
  elif string == 'society' or string == '3':
    return 'general'
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
  genre = input_check(input_genre)
  # string = input('input words >>> ')

  text_set(genre)
  # calc(genre, string)
  calc('sports_text', '日')
  # text_all_set()
  # print( data_set('/Users/wolf25/programing/data_collect/all_text/all_text1.txt') )