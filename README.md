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
1. `make`, `make install`  
2. 任意のジャンルを選択(複数選択可)  
指定したジャンル数を100件ずつwgetでダウンロード。  
どんなジャンルを入力すればいいかわからない場合は適当に入力するとヘルプが出るのでその表示に従ってください。(ただし、ジャンルはNewsAPI依存)  
**ジャンルの入力が終わったら「end」と入力する。**  
ダウンロード終了後、品詞で形態素解析を行い、ジャンルごとにテキストを出力する。  
3. 任意のクエリを入力  
クエリでtf-idfのランキングを行い、「ファイル名」・「tf-idf値」をテキストに書き込み、出力する。

- 出力するディレクトリ・ファイル類
  - 選択した「ジャンル_text」
  - 選択した「ジャンル.txt」
  - 選択した全ジャンル「mix_genre」
  - 入力したクエリでtf-idfランキングのテキスト「ranking_tfidf_value_クエリ」

- `make clean`
ダウンロードした文書、出力した結果のテキストファイル全てを削除する。
