# csv-merge

## 用途
- BigQueryでEXPORT DATAするとCloud Storageに複数ファイルで出力される
- 複数ファイルを一つのファイルにまとめるための処理

## 処理方法
- venvで仮想環境を構築する
    - python -m venv . で仮想環境を構築する
    - source ./bin/activate で仮想環境をアクティベートする
    - pip install pandas でpandasライブラリをインストールする
- Cloud Storageのバケット、パスをプログラムの変数に置き換える
- 本プログラムのカレントディレクトリに移動してcsv-merge.pyを実行する
- combined.csvが生成される
- プログラム実行後は生成されたファイルとCloud Storageからダウンロードしたファイルは削除すること
