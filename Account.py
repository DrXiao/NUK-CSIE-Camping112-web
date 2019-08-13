#自定義模組SQL_method，是操作資料庫的模組
#匯入SQL_method，並在此簡寫為sql
import SQL_method as sql

class Member:
    Name = ''
    Account = ''
    Password = ''
    team = ''
    def __init__(self,Name,Account,Password,team):
        self.Name = Name
        self.Account = Account
        self.Password = Password
        self.team = team

class Team:
    score= ''

