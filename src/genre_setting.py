#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class GenreSetting():
  def __init__(self):
    '''
    ジャンルを入力する際のバリデーションを行うためのジャンル(変数)を格納する。
    NewsAPIにあるカテゴリ(ジャンル)に限る。
    '''
    self.__genre_list = [
      'sports', # スポーツ
      'society', # 社会
      'goverment', # 政治
      'technology', # 科学
      'entertainment', # エンタメ・娯楽
      'health', # 健康
      'end' # 終了を表す単語 #
    ]

  def validation(self, input_genre: str):
    '''
    設定しているジャンルにマッチしているかのバリデーション。
    '''
    if input_genre not in self.__genre_list:
      self.print_help()
      sys.exit(0)


  def print_help(self):
    '''
    どのジャンルが有効か述べる。
    '''
    print('Select correct genre ... ->  {}' .format(self.__genre_list))