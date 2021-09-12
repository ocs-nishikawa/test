import sqlite3

# データベースファイルのパス
dbpath = 'test.db'

# データベースの作成・接続とカーソル生成
c = sqlite3.connect(dbpath)
cur = c.cursor()

a1 = """SELECT pass FROM test2_table"""
a2 = """SELECT pass FROM test2_table WHERE id = 2"""
a3 = """SELECT pass FROM test2_table WHERE id = 3"""

L1 = [x for x in range(0, 100, 1)]
n = 0
m = 0

for t1 in cur.execute(a1):
    L1[n] = t1
    n = n + 1
    print(type(t1))
    
print(L1[0:n:1])
