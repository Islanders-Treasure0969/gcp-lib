import subprocess
import pandas as pd
import glob

# Cloud Storageのバケット名とファイルのパス
bucket_name = 'dev-dwh-fdg-sm-tmp'
bucket_path = 'iwashita_Work'
local_path = './target-files/'

# gsutilを使ってCloud StorageからローカルにCSVファイルをダウンロード
subprocess.run(['gsutil', '-m', 'cp', '-r', f'gs://{bucket_name}/{bucket_path}/*.csv', local_path], check=True)

# ダウンロードしたすべてのCSVファイルを取得
all_files = glob.glob(local_path + "*.csv")

# 各ファイルを読み込み、一つのDataFrameに結合
df_list = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df_list.append(df)

# ヘッダーを残したまま結合
combined_csv = pd.concat(df_list, axis=0, ignore_index=True)

# 結果を新しいCSVファイルに保存
combined_csv.to_csv(local_path + "combined_csv.csv", index=False, encoding='utf-8-sig')

# gsutilを使って処理済みのCSVファイルをCloud Storageにアップロード
subprocess.run(['gsutil', 'cp', local_path + "combined_csv.csv", f'gs://{bucket_name}/{bucket_path}/'], check=True)
