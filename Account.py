#自定義模組SQL_method，是操作資料庫的模組
#匯入SQL_method，並在此簡寫為sql
import SQL_method as sql
import copy

# Member 類別，一個同學的資訊
class Member:
    def __init__(self,Name,Account,Password,team):
        self.Name = Name
        self.Account = Account
        self.Password = Password
        self.team = team
    def renew(self,Name,Account,Password,team):
        self.Name = Name
        self.Account = Account
        self.Password = Password
        self.team = team

"""
login函式
由帳號密碼判斷登入成不成功，
若失敗就回傳        字串,Flase

成功就回傳一個      Member類別的變數,True
"""
def login(account,password):
    member = []
    if account == None or password == None:
        return '帳號或密碼為空',False
    member = sql.get_member_table_SQL()
    for i in range(len(member)):
        if member[i][1] == account:
            if member[i][2] == password:
                the_member = Member(member[i][0],member[i][1],member[i][2],member[i][3])
                return the_member,True
            else:
                return '密碼錯誤!',False
    return '沒有註冊帳號!',False


#sql.create_team_table_SQL()
#team = Team('青龍',0)
#sql.insert_team_table_SQL(team)