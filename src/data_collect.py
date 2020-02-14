#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
from newsapi import NewsApiClient
from time import sleep
import pathlib

import key  #APIキー取得
import variable # リストを取得

# APIキー
API_KEY = key.KEY

# ジャンルのカテゴリ
categories = variable.categories
text_files = variable.text_files

class DataCollect():
  def __init__(self):
    '''
    コンストラクタ
    '''
    # カレントディレクトリ
    self.all_path = os.getcwd()
    # ソースファイルの１つ上の階層を取得
    self.path = pathlib.Path(self.all_path).parent


  def print_data(self) -> None:
    '''
    NewsAPIを用いて多ジャンルの文書をダウンロードする。
    '''
    # クライアントを初期化
    newsapi = NewsApiClient(api_key=API_KEY)

    for category in categories:
      for number in range(1,6):
        headlines = newsapi.get_top_headlines(country='jp', category=category, page=number)

        for data in headlines["articles"]:
          data_url = data["url"]
          self.load_html(data_url, category)
          sleep(3)


  def load_html(self, data: str, dir_name: str) -> None:
    '''
    wgetを使って文書をダウンロードする。
    '''
    # os.chdir( path + '/' + dir_name)
    os.chdir( os.path.join(self.path, dir_name) )
    os.system('wget -E -H ' + data)


  def update_files(self) -> None:
    '''
    ファイル・ディレクトリを更新する。
    '''
    for category in categories:
      dir_path = os.path.join(self.path, category)
      if not os.path.exists(dir_path):
        os.system('mkdir ' + dir_path)


if __name__ == '__main__':
  data_collect = DataCollect()
  data_collect.update_files()
  data_collect.print_data()

# categories = []
#   print("Please press \'end\' if you finished entering . ")
#   while True:
#     category = input("Select categories ...")
#     if category == 'end': break
    # categories.append(category)