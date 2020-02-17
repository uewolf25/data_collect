#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import data_collect
import scraping
import ranking
import file_path
import read_write
import genre_setting
import graph

class Index():
  def __init__(self):
    self.__setting = genre_setting.GenreSetting()

  def input_genre(self):
    categories = []
    print("Please press \'end\' if you finished entering .\n ")

    try:
      while True:
        category = input("Select categories >>> ")
        self.__setting.validation(category)
        if category == 'end': break
        if 'end' not in categories:
          categories.append(category)
        # if 'end' in categories:
        #   categories.remove('end')
      return categories

    except KeyboardInterrupt:
      print('\n\tEnd this program ...\n')
      sys.exit(0)

  

if __name__ == '__main__':
  index = Index()
  category = index.input_genre()
  print(category)
  instance_list = []
  for genre in category:
    file_path_class = file_path.FilePath(genre)
    file_path_class.create_category_dir()
    file_path_class.create_category_text_dir()
    file_path_class.create_category_text_file()

    data_collect = data_collect.DataCollect(genre)
    data_collect.print_data() # 何回か実行させる必要あり。

    scraping = scraping.Scraping(genre)
    scraping.set_file_list()

    ranking = ranking.Ranking(genre)
    ranking.rank_and_freq( ranking.annalys_documents() )
    # 「インスタンス」 = クラス(ジャンル)
    # 各インスタンスをsetterでジャンルを設定する
    # instance_list.append() # 「インスタンス」を格納していく