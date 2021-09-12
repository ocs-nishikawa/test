import sqlite3

# データベースファイルのパス
dbpath = 'RasPi.db'

# データベースの作成・接続とカーソル生成
c = sqlite3.connect(dbpath)
cur = c.cursor()

# # データテーブルを作成する
cur.execute("create table RasPi_table(user_id text , pass text , classroom_name text , equipment_number text , concentration integer , date text , number integer)")
# cur.execute("insert into RasPi_table(id,name) values(1,'bitcoin')")
c.commit()

sql = """SELECT * FROM RasPi_table"""

for t in cur.execute(sql):#for文で作成した全テーブルを確認していく
    print(t)