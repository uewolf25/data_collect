#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import search
import data_collect
import scraping
import ranking
import file_path
import read_write
import data_set
import tf_idf
import sort_value
# モジュール
import graph

class Index():
  def __init__(self):
    pass
  
  def flow(self, category: list, query: str):
    print(category)

    instance_list = []
    for genre in category:
      print('\n genre : {} \n'.format(genre))
      file_path_class = file_path.FilePath(genre)
      file_path_class.create_category_dir()
      file_path_class.create_category_text_dir()
      file_path_class.create_mix_category_dir()
      file_path_class.create_category_text_file()

      data_collect_class = data_collect.DataCollect(genre)
      data_collect_class.print_data() # 何回か実行させる必要あり。

      scraping_class = scraping.Scraping(genre)
      scraping_class.set_file_list()

      ranking_class = ranking.Ranking(genre)
      ranking_class.rank_and_freq( ranking_class.annalys_documents() )

    for genre in category:

      data_set_class = data_set.DataSet(genre)
      all_genre_list = data_set_class.text_set()
      # print(all_genre_list) # ジャンル区別無しの件数全部入ってる
      tfidf_class = tf_idf.TfIdf(genre, query, all_genre_list)
      file_name_list, result_value_list = tfidf_class.calc()

      sort_class = sort_value.SortValue(file_name_list, result_value_list, genre, query)
      sort_class.value_sort()

      # 「インスタンス」 = クラス(ジャンル)
      # 各インスタンスをsetterでジャンルを設定する
      # instance_list.append() # 「インスタンス」を格納していく

      # インスタンスの消去
      # del file_path_class
      # del data_collect_class
      # del scraping_class
      # del ranking_class
