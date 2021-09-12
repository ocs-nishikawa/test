import sqlite3

# # データベースファイルのパス
dbpath = 'test5.db'

# # データベースの作成・接続とカーソル生成
c = sqlite3.connect(dbpath)
cur = c.cursor()

# # # データテーブルを作成する
cur.execute("create table test5_table(id int , pass int)")