import sqlite3

# DB 생성
conn = sqlite3.connect('smart_farm.db')

# 커서 획득
c = conn.cursor()

# 데이터 불러오기
# c.execute("SELECT * FROM SF_machine")

# 데이터 삽입
# c.execute("INSERT INTO User VALUES(1, 'admin', 1111)")

c.execute("SELECT * FROM User")
print(c.fetchall())


conn.close()