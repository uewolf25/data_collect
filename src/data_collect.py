#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
from newsapi import NewsApiClient
from time import sleep
import pathlib

import key  #APIキー取得
import file_path

# APIキー
API_KEY = key.KEY


class DataCollect():
  def __init__(self, genre: str, path_object: file_path):
    '''
    コンストラクタ
    '''
    self.__genre = genre
    self.__path = path_object


  def print_data(self) -> None:
    '''
    NewsAPIを用いて多ジャンルの文書をダウンロードする。
    '''
    # クライアントを初期化
    newsapi = NewsApiClient(api_key=API_KEY)

    for number in range(1,6):
      headlines = newsapi.get_top_headlines(country='jp', category=self.__genre, page=number)
      ganre_path = self.__path.get_category_dir_path()
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
  genre = 'sports'
  # ファイル・ディレクトリの初期化
  file_control_class = file_path.FilePath(genre)
  file_control_class.create_category_dir()
  file_control_class.create_category_text_dir()
  file_control_class.create_category_text_file()
  
  # メインクラス実行
  data_collect = DataCollect(genre, file_control_class)
  data_collect.print_data()
