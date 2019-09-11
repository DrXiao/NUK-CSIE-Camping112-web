# psycopg2 模組，用來連結資料庫的模組，內含一堆方法
import psycopg2

"""
SQL_method的所有函式，必定包含下面6行code，我分為前3行跟後3行

conn = psycopg2.connect(database="d1kq7fanns12dc", user="lnvsdyjiuitchs", password="bd4d4f3614d2f215d67162bd62296fc387fcb3ad7cb2bf3891b3da1c876db4fb", host="ec2-50-19-254-63.compute-1.amazonaws.com", port="5432")
cur = conn.cursor()
cur.execute('')
---------------------------------------------------------------------------------
翻譯:
conn    :   利用psycopg2的connect方法，連結到資料庫，參數我已經打好惹，不用再變
cur     :   conn取得資料庫，利用cursor方法，返回資料庫的指標給cur
            如此，cur才是真正一個可以操作資料庫的變數
cur.execute('')   : cur利用execute方法操作資料庫，參數是字串，字串是SQL語法
---------------------------------------------------------------------------------

conn.commit()
cur.close()
conn.close()
---------------------------------------------------------------------------------
翻譯    :   關閉資料庫，沒有關，之前的動作都會無效而且會出問題
---------------------------------------------------------------------------------

利用這6行，加上自己的Python code，實現有關於資料庫的操作
"""

# print出所有小隊的資訊
def print_team_table_SQL():
    conn = psycopg2.connect(database="d1kq7fanns12dc", user="lnvsdyjiuitchs", password="bd4d4f3614d2f215d67162bd62296fc387fcb3ad7cb2bf3891b3da1c876db4fb", host="ec2-50-19-254-63.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Team")
    rows = []
    rows = cur.fetchall()
    for i in range(len(rows)):
        print(rows[i])
    conn.commit()
    cur.close()
    conn.close()

# 取得某個小隊的資訊，回傳二維陣列
def get_team_table_SQL(team):
    conn = psycopg2.connect(database="d1kq7fanns12dc", user="lnvsdyjiuitchs", password="bd4d4f3614d2f215d67162bd62296fc387fcb3ad7cb2bf3891b3da1c876db4fb", host="ec2-50-19-254-63.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM team where teamname = \'%s\'"%(team))
    rows = []
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return rows[0][0],rows[0][1]


# print出所有成員的資訊
def print_member_table_SQL():
    conn = psycopg2.connect(database="d1kq7fanns12dc", user="lnvsdyjiuitchs", password="bd4d4f3614d2f215d67162bd62296fc387fcb3ad7cb2bf3891b3da1c876db4fb", host="ec2-50-19-254-63.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM member")
    rows = []
    rows = cur.fetchall()
    for i in range(len(rows)):
        print(rows[i])
    conn.commit()
    cur.close()
    conn.close()

# 取得所有成員的資訊，回傳二維陣列
def get_member_table_SQL():
    conn = psycopg2.connect(database="d1kq7fanns12dc", user="lnvsdyjiuitchs", password="bd4d4f3614d2f215d67162bd62296fc387fcb3ad7cb2bf3891b3da1c876db4fb", host="ec2-50-19-254-63.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM member")
    rows = []
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return rows

# 取得所有上級工作人員
def get_superviser_sql():
    conn = psycopg2.connect(database="d1kq7fanns12dc", user="lnvsdyjiuitchs", password="bd4d4f3614d2f215d67162bd62296fc387fcb3ad7cb2bf3891b3da1c876db4fb", host="ec2-50-19-254-63.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM member where teamname = '上級工作人員'")
    rows = []
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    dict = {}
    for i in range(len(rows)):
        dict[rows[i][0]] = rows[i][1]
        dict[rows[i][1]] = rows[i][0]
    return dict
    

#你們可以把下面兩行的code執行一次，把註解符號拿掉，並按下F5執行，就可以得到資料庫建立的所有資訊了

#print_member_table_SQL()
#print_team_table_SQL()
