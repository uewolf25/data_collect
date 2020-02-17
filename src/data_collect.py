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
  def __init__(self, genre: str):
    '''
    コンストラクタ
    '''
    self.__genre = genre
    self.__file_class = file_path.FilePath(genre)


  def print_data(self) -> None:
    '''
    NewsAPIを用いて多ジャンルの文書をダウンロードする。
    '''
    # クライアントを初期化
    newsapi = NewsApiClient(api_key=API_KEY)

    for number in range(1,6):
      headlines = newsapi.get_top_headlines(country='jp', category=self.__genre, page=number)
      ganre_path = self.__file_class.get_category_dir_path()
      # print(ganre_path)
      if self.is_file_count(str(ganre_path)): break

      for data in headlines["articles"]:
        data_url = data["url"]
        self.load_html(data_url, ganre_path)
        sleep(3)


  def load_html(self, data: str, dir_name: str) -> None:
    '''
    wgetを使って文書をダウンロードする。
    '''
    print( '----------↓ {} ↓----------'.format( len( os.listdir(dir_name) ) ) )
    os.chdir( dir_name )
    os.system('wget -E -H ' + data)


  def is_file_count(self, dir_name: str) -> bool:
    file_count = os.listdir(dir_name)
    if len(file_count) >= 100:
      print('このジャンルの文書が必要数揃っています。\n')
      return True 
    else: 
      return False
