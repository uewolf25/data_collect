#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import pathlib

class FilePath():

  def __init__(self, genre):
    '''
    コンストラクタ
    '''
    self.__category = genre # ジャンル名
    # パスの位置の取得
    self.__current_path = os.getcwd()
    self.__path = pathlib.Path(self.__current_path) # ~~/data_collect/src/
    self.__parent_path = self.__path.parent # ~~/data_collect/
    self.__genre_dir = self.__category + '_text' # ジャンル_text/
    self.__text_file = self.__category + '.txt' # ジャンル.txt

  def get_top_dir_path(self):
    '''
    一番上のディレクトリのパスを取得。
    '''
    return self.__parent_path

  def get_category_dir_path(self):
    '''
    ジャンル(HTML)のディレクトリを取得。
    '''
    return os.path.join( self.__parent_path, self.__category ) # ~~/data_collect/ジャンル/

  def get_category_text_dir_path(self):
    '''
    ジャンル１００件分を解析したテキストがあるディレクトリの取得。
    '''
    return os.path.join( self.__parent_path, self.__genre_dir ) # ~~/data_collect/ジャンル_text/

  def get_category_textfile_path(self):
    '''
    選択されたジャンルの解析済みのまとめたテキストファイルのファイルパスを取得。
    '''
    return os.path.join( self.__parent_path, self.__genre_dir ) # ~~/data_collect/ジャンル.txt

  def get_each_text_file_name(self, num: int):
    '''
    ジャンル１００件分を解析したテキスト１つ１つに名前(番号)付け。
    '''
    each_text_file = '{}_text{}.txt'.format(self.__category, num) # ジャンル_text_num.txt
    return os.path.join( 
      self.get_category_text_dir_path(), 
      each_text_file 
      ) # ~~/data_collect/ジャンル_text/ジャンル_text_num.txt


  def create_category_dir(self):
    '''
    wgetで落とした文書を格納するディレクトリの作成。
    '''
    dir_path = os.path.join(self.__parent_path, self.__category)
    if not os.path.exists(dir_path):
      os.system('mkdir ' + dir_path)
      
  def create_category_text_dir(self):
    '''
    落とした文書を解析した１つ１つのテキストを格納するディレクトリの作成。
    '''
    dir_path = os.path.join(self.__parent_path, self.__genre_dir)
    if not os.path.exists(dir_path):
      os.system('mkdir ' + dir_path)

  def create_category_text_file(self):
    '''
    選択されたジャンルの解析済みのまとめたテキストファイルの作成。
    '''
    text_path = os.path.join(self.__parent_path, self.__text_file)
    if not os.path.exists(text_path):
      os.system('touch ' + text_path)
