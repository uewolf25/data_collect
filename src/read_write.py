#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ReadWrite():

  def __init__(self):
    pass

  def read_text(self, text_file: str) -> str:
    '''
    テキストに書かれた文書を読み込む。
    '''
    text = ''

    try:
      f = open(text_file, 'r', encoding='utf8', errors='ignore')
    except IOError:
      print('{} is cannot be opend .'.format(text_file))
    except UnicodeDecodeError:
      print('{} is not decoded .'.format(text_file) )
    else:
      text = f.read()
      f.close()
    # finally:
    #   print('---------------------------------------')
    return text


  def write_text(self, string: str, text_file: str) -> None:
    '''
    文書をテキストに追記していく。
    '''
    try:  
      f = open(text_file, 'a')
    except IOError:
      print('{} is cannot be opened .'.format(text_file))
    else:
      f.write(string)
      f.close()

  def write_text_dict(self, dictonary: dict, text_file: str) -> None:
    for key, value in dictonary:
      try:
        f = open(text_file, 'a')
      except IOError:
        print('cannot be opened .')
      else:
        f.write('{0}:\t{1}\n\n'.format( key, str(value) ))
        f.close()
