import sqlite3

# # データベースファイルのパス
dbpath = 'test2.db'

# # データベースの作成・接続とカーソル生成
c = sqlite3.connect(dbpath)
cur = c.cursor()

# # # データテーブルを作成する
cur.execute("create table test3_table(number int , ppm int)")
cur.execute("insert into test3_table(number,ppm) values(3,900)")
cur.execute("insert into test3_table(number,ppm) values(4,960)")
cur.execute("insert into test3_table(number,ppm) values(5,970)")
cur.execute("insert into test3_table(number,ppm) values(7,1000)")
cur.execute("insert into test3_table(number,ppm) values(5,990)")
c.commit()

# sql = """SELECT * FROM test_table"""

# for t in cur.execute(sql):#for文で作成した全テーブルを確認していく
#     print(t)
