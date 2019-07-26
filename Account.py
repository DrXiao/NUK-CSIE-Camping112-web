import SQL_method as sql

def login(account,password):
    if account == '' or password == '':
        return '帳號或密碼為空!',None
    list = []
    list = sql.get_table_SQL()
    for i in range(len(list)):
        if account == list[i][0]:
            if password == list[i][1]:
                return '正確!',list[i]
            else:
                return 'Error! 你的密碼輸入錯誤!',None
    return '你沒有帳號喔~ 快去註冊',None

def find_account(account):
    list = []
    list = sql.get_table_SQL()
    for i in range(len(list)):
        if account == list[i][0]:
            return list[i]

def register_new_account(Name,Account,Password):
    sql.insert_table_SQL(Account,Password,Name)