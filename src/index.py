#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Index():
  def __init__(self):
    pass

  def input_genre(self):
    categories = []
    print("Please press \'end\' if you finished entering . ")

    while True:
      category = input("Select categories >>> ")
      if category == 'end': break
      categories.append(category)
    return categories
  

if __name__ == '__main__':
  index = Index()
  category = index.input_genre()
  # print(category)
  instance_list = []
  for genre in category:
    # 「インスタンス」 = クラス(ジャンル)
    # 各インスタンスをsetterでジャンルを設定する
    instance_list.append() # 「インスタンス」を格納していく