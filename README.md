# データ収集
単語とジャンルを指定して、最終的にtf-idf値の計算を行う。

## 前準備
### API
今回は特定のジャンルのニュースを取得するために、[NewsAPI](https://newsapi.org/)を使用しているので、APIキーを取得する必要がある。  
- 上記にアクセスする。
- 「Get API key」から登録を行う。  

また、パッケージのインストールも行う。  
- `pip install newsapi-python`

### Mecab
[公式サイト](http://taku910.github.io/mecab/)からMecabと辞書をインストール。  
解凍から使うまでの方法はサイトに書いているので割愛。

Mecabパッケージのインストール
- `sudo pip install mecab-python3`

### 環境変数ファイル
APIキーを使用できるように`.env-template`に自分のAPIキーを入力し、以下のコマンドを実行する。
- `mv .env-template .env`  


## 実行