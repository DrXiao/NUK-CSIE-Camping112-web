import SQL_method as sql
import psycopg2
import time
from Account import Team
from Account import Phoenix_team

def team_give_score(team,target,score):
    localtime = time.localtime()
    team.Score = team.Score+score
    conn = psycopg2.connect(database="d8ti03uqsns0a0", user="upsvubypqddslc", password="257462a430af3ef3323f2bfe71e0ae14bd5a97bcfed571564e47807fc00d2adf", host="ec2-54-243-193-59.compute-1.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute(' Update team SET score = %d Where teamname = \'%s\';'%(team.Score,team.TeamName))
    timestr = '%d/%d/%d:%d'%(localtime.tm_mon,localtime.tm_mday,localtime.tm_hour,localtime.tm_min)
    cur.execute('insert into trade(time,team,target,amount)values(\'%s\',\'%s\',\'%s\',%d)'%(timestr,team.TeamName,target,score))
    conn.commit()
    cur.close()
    conn.close()
