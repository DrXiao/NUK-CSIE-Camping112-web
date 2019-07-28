# psycopg2 模組，用來連結資料庫的模組，內含一堆方法
import psycopg2

"""
SQL_method的所有函式，必定包含下面6行code，我分為前3行跟後3行

conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
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


"""
create_table_SQL()    :   創建表格函式
只需執行一次，就可以在資料庫建立「一種表格」，不能重複建立相同種類的表格，否則會出錯

現在我已經建立一種表格叫做 Member，放在一個public的地方(呃...應該是這個意思)，內容是
account(帳號)，長度32個字元，不能為空，是一個鍵值(就是只能有一個這個帳號的意思)
password(密碼)，長度32個字元，不能為空
name(名字)，長度32個字元，不能為空

利用execute內加入SQL語法的字串，建立表格

建立成功後，就在終端機print出 'public table is created'，才知道有沒有建立成功
"""
def create_table_SQL():
    conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute('''create table public.Member(
    account varchar(32) not null primary key,
    password varchar(32) not null,
    name    varchar(32) not null)'''
    )
    print('public table is created')
    conn.commit()
    cur.close()
    conn.close()

"""
insert_table_SQL()      :   新增資料函式(新增帳號)

利用SQL語法，新增一筆Member格式的資料，把它加入PSQL資料庫裡面

在終端機print出 'New user is created' ，知道有沒有新建成功
"""
def insert_table_SQL(account,password,name):
    conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute("insert into public.Member(account,password,name)values('%s','%s','%s')"%(account,password,name))
    print('New user is created')
    conn.commit()
    cur.close()
    conn.close()

"""
print_table_SQL()       :   顯示資料函式

自己測試BUG的函式，平時不會用

利用SQL語法  "SELECT * FROM member"，取得有關member的所有資料
讓rows 陣列去接住這些資料( rows = cur.fetchall() )，並一行一行print出來(for迴圈)
"""
def print_table_SQL():
    conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM member")
    rows = []
    rows = cur.fetchall()
    for i in range(len(rows)):
        print(rows[i])
    conn.commit()
    cur.close()
    conn.close()

"""
get_table_SQL()     :   返回資料的函式

code 與  print_table_SQL()  大同小異

-->回傳資料二維陣列
"""

def get_table_SQL():
    conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM member")
    rows = []
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return rows