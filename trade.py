import SQL_method as sql
import psycopg2
import time

def team_give_score(team,target,score):
    localtime = time.localtime(time.time()+8*3600)
    Teamname,Score = sql.get_team_table_SQL(team)
    conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute(' Update team SET score = %d Where teamname = \'%s\';'%(Score+score,Teamname))
    timestr = '%d/%d/%02d:%02d'%(localtime.tm_mon,localtime.tm_mday,localtime.tm_hour,localtime.tm_min)
    cur.execute('insert into trade(time,team,target,amount)values(\'%s\',\'%s\',\'%s\',%d)'%(timestr,Teamname,target,score))
    conn.commit()
    cur.close()
    conn.close()

class trade_record:
    def __init__(self,name):
        conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
        cur = conn.cursor()
        trade_list = []
        cur.execute(' SELECT * FROM trade WHERE target = \'%s\' '%(name))
        trade_list = cur.fetchall()
        trade_list.reverse()
        self.trade_list = []
        for i in range(len(trade_list)):
            dict1 = {'date':trade_list[i][0],'team':trade_list[i][1],'target':trade_list[i][2],'score':trade_list[i][3]}
            self.trade_list.append(dict1)
            if len(self.trade_list)>10:
                break
        conn.commit()
        cur.close()
        conn.close()

class team_record:
    def __init__(self,name):
        conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
        cur = conn.cursor()
        trade_list = []
        cur.execute(' SELECT * FROM trade WHERE team = \'%s\' '%(name))
        trade_list = cur.fetchall()
        trade_list.reverse()
        self.trade_list = []
        for i in range(len(trade_list)):
            dict1 = {'date':trade_list[i][0],'team':trade_list[i][1],'target':trade_list[i][2],'score':trade_list[i][3]}
            self.trade_list.append(dict1)
            if len(self.trade_list)>10:
                break
        conn.commit()
        cur.close()
        conn.close()
