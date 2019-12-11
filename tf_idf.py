#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, os.path
import sys
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

def text_set() -> None:
  '''
  全ジャンルの文書をそれぞれ格納していく。
  '''

  for cate_text_dir, cate_dir in zip(categories_text_dir, [sports_list, business_list, general_list]):
    files = os.listdir(cate_text_dir) # リストでファイル名が格納されている。
    for each_file in files:
      file_path = os.path.join( cate_text_dir, each_file )
      data_list = data_set(file_path)
      # print(file_path)
      cate_dir.append(data_list)
    # print(cate_dir)

def calc() -> None:
  '''
  実際にtf-idfを計算する関数
  '''
  # tf()
  # idf()
  # tf_idf()
  pass



def tf():
  '''
  １つのファイル内にある単語がどれだけ含まれているか。\n
  ・tf = ある単語の出現数 / 文章全体の単語数
  '''
  pass

def idf():
  '''
  全ファイル(100個)にある単語が何個のファイルに含まれているか。\n
  ・idf = log( 全ファイル数 / ある単語が出現したファイル数 )
  '''
  pass

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
  string = input('input words >>> ')
  # text_set()
  # calc()
  # print( data_set('/Users/wolf25/programing/data_collect/all_text/all_text1.txt') )