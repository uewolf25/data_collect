#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import math
import numpy as np
import matplotlib.pyplot as plt


def graph(x, y, name):
  xx, yy = [], []

  for a, b in zip(x, y):
    # print('{0} : {1}'.format(math.log10(a), math.log10(b)))
    xx.append(math.log10(a))
    yy.append(math.log10(b))

  # Figureオブジェクトとそれに属する一つのAxesオブジェクトを同時に作成
  fig, ax = plt.subplots()
  ax.plot(xx, yy, marker="o", color="red")

  # ax.set_xscale("log", basex=10, nonposx="mask")
  # ax.set_yscale("log")

  fig.suptitle(name)
  print('figuring -> {0} ...'.format(name))

  ax.set_xlabel("ranking")
  ax.set_ylabel("frequency")

  # ax.set_xticks( np.linspace(0, 3, 7), minor=False )
  # ax.set_yticks( np.linspace(0, 3, 7), minor=False )

  plt.show()