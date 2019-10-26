#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import json
import key
from newsapi import NewsApiClient

API_KEY = key.KEY

def print_data():
  
  # クライアントを初期化
  newsapi = NewsApiClient(api_key=API_KEY)

  # headlines = newsapi.get_everything(q='sports', pageSize='100')
  headlines = newsapi.get_top_headlines(country='jp', category='sports', page=1)

  for data in headlines["articles"]:
    data_url = data["url"]
    load_html(data_url)

    # if os.path.exists( os.path.join("img"),  )
      
  # newsapi.get_sources()

def load_html(data):    
  # print(data)
  os.system('cd file/; wget ' + data)

def remove_old_folder():
  # 「img」フォルダが存在した時に消しておく。
  if os.path.exists('file/'):
      os.system('rm -r file/')
  os.system('mkdir file/')

def add_extension():
  name, extension = os.path.splitext(file_name)
  # 拡張子がない場合の追加
  if not extension:
      extension = ".html"
  html_file = '{}{}'.format(name, extension)
  return html_file

if __name__ == '__main__':
  remove_old_folder()
  print_data()
  
