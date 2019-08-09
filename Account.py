#自定義模組SQL_method，是操作資料庫的模組
#匯入SQL_method，並在此簡寫為sql
import SQL_method as sql

class Member:
    Account = ''
    Password = ''
    Name = ''
    def __init__(self,Account,Password,Name):
        self.Account = Account
        self.Password = Password
        self.Name = Name
    def change(self,Account,Password,Name):
        self.Account = Account
        self.Password = Password
        self.Name = Name


def login(account,password):
    if account == '' or password == '':
        return '帳號或密碼為空!',[]
    list = []
    list = sql.get_table_SQL()
    for i in range(len(list)):
        if account == list[i][0]:
            if password == list[i][1]:
                return '正確!',list[i]
            else:
                return 'Error! 你的密碼輸入錯誤!',[]
    return '你沒有帳號喔~ 快去註冊',[]

def register_new_account(Name,Account,Password):
    sql.insert_table_SQL(Account,Password,Name)