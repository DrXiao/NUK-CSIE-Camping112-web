#自定義模組SQL_method，是操作資料庫的模組
#匯入SQL_method，並在此簡寫為sql
import SQL_method as sql
import copy

member = []
team = []

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
    def renew(self,Name,Account,Password,team):
        self.Name = Name
        self.Account = Account
        self.Password = Password
        self.team = team

class Team:
    TeamName = ''
    Score= ''
    def __init__(self,TeamName,Score):
        self.TeamName = TeamName
        self.Score = Score
    def renew(self,TeamName,Score):
        self.TeamName = TeamName
        self.Score = Score

def login(account,password):
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

def register(Name,Account,Password,team_password):
    new_member = Member('','','','')
    if team_password == 'IamDargonTeam':
        new_member = Member(Name,Account,Password,'青龍')
    elif team_password == 'BeTigerTeam':
        new_member = Member(Name,Account,Password,'白虎')
    elif team_password == 'WeArePhoenixTeam':
        new_member = Member(Name,Account,Password,'朱雀')
    elif team_password == 'GoToTortoiseTeam':
        new_member = Member(Name,Account,Password,'玄武')
    else:
        return '輸入有誤!'
    if new_member.Name == '' or new_member.Account == '' or new_member.Password == '':
        return '名字、帳號、密碼有一個是空的!'
    else:
        sql.insert_member_table_SQL(new_member)
        print('新帳號註冊成功')
        return True



team = sql.get_team_table_SQL()

Dargon_team = Team(team[0][0],team[0][1])
Tiger_team = Team(team[1][0],team[1][1])
Phoenix_team = Team(team[2][0],team[2][1])
Tortoise_Team = Team(team[3][0],team[3][1])

#sql.create_team_table_SQL()
#team = Team('青龍',0)
#sql.insert_team_table_SQL(team)