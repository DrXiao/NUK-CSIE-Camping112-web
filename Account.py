#自定義模組SQL_method，是操作資料庫的模組
#匯入SQL_method，並在此簡寫為sql
import SQL_method as sql

"""
登入判斷函式，必定回傳兩個值，回傳值組(字串,一維陣列)
在myweb「根目錄路由」的  context,Person = login(request.values['Account'],request.values['Password'])
這段程式碼，也就相當於
context,Person = '字串',[]

換言之，在login的函式判斷，確實有該帳號、密碼也輸入對的話
context 變數會得到 '正確!' 的字串
Person  變數會得到 list[i]，一個一維陣列，包含 (帳號,密碼,人名)

否則，
context 變數會得到 錯誤訊息  的字串
Person  變數會得到 None     值

list是陣列，在sql (SQL_method) 模組的 get_table_SQL方法得到二維陣列
得到所有帳號的資訊
在帳號裡面找有沒有 account 帳號，password 密碼對不對
"""
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

#註冊帳號的函式
def register_new_account(Name,Account,Password):
    sql.insert_table_SQL(Account,Password,Name)