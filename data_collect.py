#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import key
from newsapi import NewsApiClient
from time import sleep

API_KEY = key.KEY

categories = ['sports', 'business', 'general']
text_files = ['sports.txt', 'goverment.txt', 'society.txt']
path = os.getcwd()


###################################################
### NewsAPIを用いて３ジャンルの文書をダウンロードする。 ###
###################################################
def print_data():
  # クライアントを初期化
  newsapi = NewsApiClient(api_key=API_KEY)

  for category in categories:
    for number in range(1,6):
      headlines = newsapi.get_top_headlines(country='jp', category=category, page=number)

      for data in headlines["articles"]:
        data_url = data["url"]
        load_html(data_url, category)
        sleep(3)

#####################################
### wgetを使って文書をダウンロードする ###
#####################################
def load_html(data, dir_name):
  # os.chdir( path + '/' + dir_name)
  os.chdir( os.path.join(path, dir_name) )
  os.system('wget -E -H ' + data)

####################################
### ファイル・ディレクトリを更新する。 ###
####################################
def update_files():
  for category in categories:
    remove_old_folder(category)

  for text in text_files:
    remove_textfiles(text)

######################################################
### 古いディレクトリを削除し、新しいディレクトリを生成する。 ###
######################################################
def remove_old_folder(dir_name):
  dir_path = os.path.join(path, dir_name)
  if os.path.exists(dir_path):
      os.system('rm -r ' + dir_name)
      print('Deleting old directory ... \t' + dir_name)
  os.system('mkdir ' + dir_name)
  print('Generating new directory ... \t' + dir_name)

################################################
### 古いテキストを削除し、新しいテキストを生成する。 ###
################################################
def remove_textfiles(text):
  if os.path.exists(text):
    os.system('rm -r ' + text)
    print('Deleting old text files ... \t' + text)
  os.system('touch ' + text)
  print('Generating new text files ... \t' + text)


if __name__ == '__main__':
  update_files()
  print_data()

