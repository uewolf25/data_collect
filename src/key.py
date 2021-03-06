#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import dotenv

# .env-templeteに書かれているAPI_KEYを読み込む
dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
dotenv.load_dotenv(dotenv_path)

#　環境変数をセット
KEY = os.environ.get("API_KEY")