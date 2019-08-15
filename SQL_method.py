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

# 建立"一種"新的表格 Team，包含 小隊名稱、分數，此函式只需執行一次
def create_team_table_SQL():
    conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute('''create table public.Team(
    teamname    varchar(32) not null primary key,
    score       varchar(32) not null
    )'''
    )
    print('public table is created')
    conn.commit()
    cur.close()
    conn.close()

# 在Team表格加入新的資訊，四個小隊的資訊已經建立，不需再執行
def insert_team_table_SQL(team):
    conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute("insert into public.Team(teamname,score)values('%s','%s')"%(team.TeamName,team.Score))
    print('New team is created')
    conn.commit()
    cur.close()
    conn.close()

# print出所有小隊的資訊
def print_team_table_SQL():
    conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Team")
    rows = []
    rows = cur.fetchall()
    for i in range(len(rows)):
        print(rows[i])
    conn.commit()
    cur.close()
    conn.close()

# 取得所有小隊的資訊，回傳二維陣列
def get_team_table_SQL():
    conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM team")
    rows = []
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return rows

# 建立"一種"新的表格 Member，此函式只需執行一次，不需再執行
def create_member_table_SQL():
    conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute('''create table public.Member(
    name    varchar(32) not null,
    account varchar(32) not null primary key,
    password varchar(32) not null,
    teamname    varchar(32) not null)'''
    )
    print('public table is created')
    conn.commit()
    cur.close()
    conn.close()

# 在Member表格加入新的資訊，當有人去網頁註冊的時候，就會用這個函式去加入新的資料
def insert_member_table_SQL(Member):
    conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute("insert into public.Member(name,account,password,teamname)values('%s','%s','%s','%s')"%(Member.Name,Member.Account,Member.Password,Member.team))
    print('New user is created')
    conn.commit()
    cur.close()
    conn.close()

# print出所有成員的資訊
def print_member_table_SQL():
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

# 取得所有成員的資訊，回傳二維陣列
def get_member_table_SQL():
    conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM member")
    rows = []
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return rows



#你們可以把下面兩行的code執行一次，把註解符號拿掉，並按下F5執行，就可以得到資料庫建立的所有資訊了

#print_member_table_SQL()
#print_team_table_SQL()