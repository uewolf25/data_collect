#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pathlib

class Initialize():

  def __init__(self):
    # パスの位置の取得
    self.__current_path = os.getcwd()
    self.__path = pathlib.Path(self.__current_path) # ~~/data_collect/src
    self.__parent_path = self.__path.parent # ~~/data_collect
    # ジャンル
    self.__categories = ['sports', 'business', 'general']

  def get_main_dir_path(self):
    return self.__parent_path

  def create_category_dir(self):
    '''
    ファイル・ディレクトリを更新する。
    '''
    for category in self.__categories:
      dir_path = os.path.join(self.__parent_path, category)
      if not os.path.exists(dir_path):
        os.system('mkdir ' + dir_path)