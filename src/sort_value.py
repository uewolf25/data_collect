#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import file_path
import read_write

class SortValue():

  def __init__(self, name_list: list, value_list: list, genre: str, query: str):
    self.__file_list = name_list
    self.__value_list = value_list
    self.__genre = genre
    self.__file_class = file_path.FilePath(self.__genre)
    self.__query = query
    self.__read_write_class = read_write.ReadWrite()
    

  def value_sort(self):
      '''
      辞書型でファイル名とtf-idf値を紐付け、昇順にソートする。
      '''
      # ソートするための辞書
      file_name_and_value_dictonary = {}
      for name, value in zip(self.__file_list, self.__value_list):
        file_name_and_value_dictonary[name] = value

      # ソート
      sorted_result_values = sorted(file_name_and_value_dictonary.items(), key=lambda value:value[1], reverse=True)
      # 出力するファイル名
      output_file = self.__file_class.get_ranking_value_file_name(self.__query)

      self.__read_write_class.write_text_dict(sorted_result_values, output_file)
      print('Add ranking file . →　{}'.format(output_file))
