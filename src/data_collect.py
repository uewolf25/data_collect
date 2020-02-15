#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
from newsapi import NewsApiClient
from time import sleep
import pathlib

import key  #APIキー取得
import variable # リストを取得
import initialize

# APIキー
API_KEY = key.KEY

# ジャンルのカテゴリ
# categories = variable.categories
categories = ['sports', 'business', 'general']
text_files = variable.text_files

class DataCollect():
  def __init__(self, path_object):
    '''
    コンストラクタ
    '''
    self.path = path_object.get_main_dir_path()


  def print_data(self) -> None:
    '''
    NewsAPIを用いて多ジャンルの文書をダウンロードする。
    '''
    # クライアントを初期化
    newsapi = NewsApiClient(api_key=API_KEY)

    for category in categories:
      for number in range(1,6):
        headlines = newsapi.get_top_headlines(country='jp', category=category, page=number)
        ganre_path = os.path.join(self.path, category)
        # print(ganre_path)
        if self.is_file_count(ganre_path): break

        for data in headlines["articles"]:
          data_url = data["url"]
          self.load_html(data_url, ganre_path)
          sleep(3)


  def load_html(self, data: str, dir_name: str) -> None:
    '''
    wgetを使って文書をダウンロードする。
    '''
    os.chdir( dir_name )
    os.system('wget -E -H ' + data)


  def is_file_count(self, dir_name: str) -> bool:
    file_count = os.listdir(dir_name)
    if len(file_count) >= 100:
      print('このジャンルの文書が必要数揃っています。')
      return True 
    else: 
      return False


if __name__ == '__main__':
  # ファイル・ディレクトリの初期化
  init_object = initialize.Initialize()
  init_object.create_category_dir()
  # メインクラス実行
  data_collect = DataCollect(init_object)
  data_collect.print_data()

# categories = []
#   print("Please press \'end\' if you finished entering . ")
#   while True:
#     category = input("Select categories ...")
#     if category == 'end': break
    # categories.append(category)