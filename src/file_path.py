#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import shutil
import pathlib

class FilePath():

  def __init__(self, genre: str):
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

  def get_mix_category_dir(self):
    '''
    ジャンル１００件分を解析したテキストがあるジャンル区別無しのディレクトリの取得。
    '''
    return os.path.join( self.__parent_path, 'mix_genre' ) # ~~/data_collect/mix_genre

  def get_category_textfile_path(self):
    '''
    選択されたジャンルの解析済みのまとめたテキストファイルのファイルパスを取得。
    '''
    return os.path.join( self.__parent_path, self.__text_file ) # ~~/data_collect/ジャンル.txt

  def get_each_text_file_name(self, num: int):
    '''
    ジャンル１００件分を解析したテキスト１つ１つに名前(番号)付け。
    '''
    each_text_file = '{}_text{}.txt'.format(self.__category, num) # ジャンル_text_num.txt
    return os.path.join( 
      self.get_category_text_dir_path(), 
      each_text_file 
      ) # ~~/data_collect/ジャンル_text/ジャンル_text_num.txt

  def get_mix_each_text_file_name(self, num: int):
    '''
    ジャンル１００件分を解析したテキスト１つ１つに名前(番号)付け。→保存先はジャンル区別無しの「mix_genre/」
    '''
    each_text_file = '{}_text{}.txt'.format(self.__category, num) # ジャンル_text_num.txt
    return os.path.join( 
      self.get_mix_category_dir(),
      each_text_file
      ) # ~~/data_collect/mix_genre/ジャンル_text_num.txt

  def get_ranking_value_file_name(self, query: str):
    '''
    クエリに対しての値を計算した後のランキングしたテキストファイルのパス。
    '''
    ranking_result_file = 'ranking_tfidf_value_{}.txt'.format(query)
    return os.path.join(
      self.__parent_path,
      ranking_result_file
    ) # ~~/data_collect/ranking_tfidf_value_クエリ.txt

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
    複数回実行する度にテキストファイル群が上書きされてしまうので、一度消してから作成する。
    '''
    dir_path = os.path.join(self.__parent_path, self.__genre_dir)
    if not os.path.exists(dir_path):
      os.system('mkdir ' + dir_path)
    else:
      shutil.rmtree(dir_path)
      os.system('mkdir ' + dir_path)

  def create_mix_category_dir(self):
    '''
    解析した１つ１つのテキストをジャンル区別無しに格納するディレクトリの作成。
    複数回実行する度にテキストファイル群が上書きされてしまうので、一度消してから作成する。
    '''
    dir_path = os.path.join(self.__parent_path, 'mix_genre')
    if not os.path.exists(dir_path):
      os.system('mkdir ' + dir_path)


  def create_category_text_file(self):
    '''
    選択されたジャンルの解析済みのまとめたテキストファイルの作成。
    複数回実行する度にテキストファイルが上書きされてしまうので、一度消してから作成する。
    '''
    text_path = os.path.join(self.__parent_path, self.__text_file)
    if not os.path.exists(text_path):
      os.system('touch ' + text_path)
