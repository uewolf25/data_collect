#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from natsort import natsorted
import bs4 

import file_path
import read_write

class Scraping():

  def __init__(self, genre):
    self.__genre = genre
    self.__file_path = file_path.FilePath(genre)
    self.__read_and_write = read_write.ReadWrite()

  def set_file_list(self) -> None:
    '''
    HTML文書を目的の本文の部分のみスクレイピングし、
    タグを消して１つの文字列とする。              
    '''
    # 各ファイルのパスを格納する
    file_path = []
    # ジャンルのディレクトリの中のファイル一覧を取得 & ソートする
    all_files = natsorted( os.listdir(self.__file_path.get_category_dir_path()) )
    # 各ファイルの絶対パスを格納していく
    for local_file in all_files:
      file_path.append( os.path.join(self.__file_path.get_category_dir_path(), local_file) )

    self.scraping(file_path)

  def scraping(self, category_files_path: list):
    '''
    HTML文書から文章を抜き出す。
    category_files_path: HTML文書の絶対パス
    '''
    list_len = len( os.listdir( self.__file_path.get_category_dir_path() ) )
    for html_file, count in zip(category_files_path, range(1,list_len+1)): #+1
      text = []
      try:
        with open(html_file) as f:
          # pタグの部分だけ抜いてくる
          text = bs4.BeautifulSoup(f, "html.parser").select('p')
      except IOError:
        print('cannot be opened .')
      except UnicodeDecodeError:
        print('{0} is not decoded . (fileNumber: {1})'.format(html_file, count) )

      for item in text:
        article = ''
        # タグ付きの文章のタグを除去し、文字列型に変換
        get_articles = str( item.get_text() )
        article += get_articles
        # あるジャンル１つの文書にまとめる
        self.__read_and_write.write_text( article, self.__file_path.get_category_textfile_path() )
        # １つ１つのテキストに書き込む
        self.__read_and_write.write_text( article, self.__file_path.get_each_text_file_name(count) )

# if __name__ == '__main__':
#   scap = Scraping('sports')
#   scap.set_file_list()
