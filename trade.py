import SQL_method as sql
import psycopg2
import time

def team_give_score(team,target,score):
    localtime = time.localtime(time.time()+8*3600)
    Teamname,Score = sql.get_team_table_SQL(team)
    conn = psycopg2.connect(database="d1kq7fanns12dc", user="lnvsdyjiuitchs", password="bd4d4f3614d2f215d67162bd62296fc387fcb3ad7cb2bf3891b3da1c876db4fb", host="ec2-50-19-254-63.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute(' Update team SET score = %d Where teamname = \'%s\';'%(Score+score,Teamname))
    timestr = '%d/%d/%02d:%02d'%(localtime.tm_mon,localtime.tm_mday,localtime.tm_hour,localtime.tm_min)
    cur.execute('insert into trade(time,team,target,amount,total_score)values(\'%s\',\'%s\',\'%s\',%d,%d)'%(timestr,Teamname,target,score,Score+score))
    conn.commit()
    cur.close()
    conn.close()

class trade_record:
    def __init__(self):
        conn = psycopg2.connect(database="d1kq7fanns12dc", user="lnvsdyjiuitchs", password="bd4d4f3614d2f215d67162bd62296fc387fcb3ad7cb2bf3891b3da1c876db4fb", host="ec2-50-19-254-63.compute-1.amazonaws.com", port="5432")
        cur = conn.cursor()
        trade_list = []
        cur.execute(' SELECT * FROM trade ')
        trade_list = cur.fetchall()
        trade_list.reverse()
        self.trade_list = []
        for i in range(len(trade_list)):
            dict1 = {'date':trade_list[i][0],'team':trade_list[i][1],'target':trade_list[i][2],'score':trade_list[i][3],'total_score' : trade_list[i][4]}
            self.trade_list.append(dict1)
            if len(self.trade_list)>10:
                break
        conn.commit()
        cur.close()
        conn.close()

class team_record:
    def __init__(self,name):
        conn = psycopg2.connect(database="d1kq7fanns12dc", user="lnvsdyjiuitchs", password="bd4d4f3614d2f215d67162bd62296fc387fcb3ad7cb2bf3891b3da1c876db4fb", host="ec2-50-19-254-63.compute-1.amazonaws.com", port="5432")
        cur = conn.cursor()
        trade_list = []
        cur.execute(' SELECT * FROM trade WHERE team = \'%s\' '%(name))
        trade_list = cur.fetchall()
        trade_list.reverse()
        self.trade_list = []
        for i in range(len(trade_list)):
            dict1 = {'date':trade_list[i][0],'team':trade_list[i][1],'target':trade_list[i][2],'score':trade_list[i][3],'total_score':trade_list[i][4]}
            self.trade_list.append(dict1)
            if len(self.trade_list)>10:
                break
        conn.commit()
        cur.close()
        conn.close()
