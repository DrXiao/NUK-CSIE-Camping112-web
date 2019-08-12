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

