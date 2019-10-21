
# 從第三方模組 flask, 匯入 Flask、make_response、request 類別 ， url_for、 redirect 函數
from flask import Flask, render_template, request, url_for, redirect, make_response

"""
~翻譯時間~
Flask 類別 : 可以建構一個網站實例
render_template 函數 : 可以回應一個 html 網頁給client端
url_for 函數 : 可以利用函數名稱，引導到某一個路由
request 類別 : 


"""

# 從自定義模組 trade,匯入相關函數
from trade import team_give_score, trade_record, team_record

# 匯入自定義模組 SQL_method ，並簡寫為 sql
import SQL_method as sql

# 匯入模組 re -->模組有關於 Regular Expression (正規表達式) 的相關函數
import re

# 匯入模組 os --> 我沒用到拉ㄏ，忘記刪掉惹
import os

# 從自定義模組 Account,匯入 Member 類別 、 login 函數
from Account import Member, login

# app 是 Flask 的一個實例，app就是網站啦!
app = Flask(__name__)


dict_member = sql.get_superviser_sql()
dict_team = {'phoenix': '朱雀', 'tiger': '白虎', 'tortoise': '玄武', 'dragon': '青龍'}


# 裝飾器 decorator，app.route()，決定一個「路由」要回應的網頁
"""

'/' 路由，顯示首頁，即登入頁面

先檢查自身電腦本身有沒有相關 cookie
    若有，就引導到另一個網頁(即 小隊頁面 or 工作人員頁面)

如果client發出 POST 請求，即該client嘗試登入，利用login函數來判斷是否登入成功
    flag 將從 login 的回傳值，得到 True or False 值
        如果 flag == True，表示有該帳號、密碼也對，就登入成功
        res 是 make_response 的實例，利用 redirect(url_for()) 來建構
        利用 res 物件，在client端上留下 cookie (保留兩個資訊 -- 該帳號的隊伍名稱、該帳號的使用者名字)




"""
@app.route('/', methods=['GET', 'POST'])
def home():
    the_member = Member('', '', '', '')
    cookie_team = request.cookies.get('TeamName')
    cookie_name = request.cookies.get('User')
    if cookie_team != None and cookie_name != None:
        return redirect(url_for('go_to_team'))
    if request.method == 'POST':
        member, flag = login(
            request.values['Account'], request.values['Password'])
        if flag == True:
            the_member.renew(member.Name, member.Account,
                             member.Password, member.team)
            res = make_response(redirect(url_for('go_to_team')))
            res.set_cookie('TeamName', the_member.team)
            res.set_cookie('User', the_member.Name)
            return res
        else:
            return redirect(url_for('home', message=member))

    return render_template('homepage.html')


"""
'/QRscan' 路由

顯示一個QRcode scanner頁面給使用者

"""
@app.route('/QRscan', methods=['GET', 'POST'])
def QRcode_scan():
    cookie_team = request.cookies.get('TeamName')
    cookie_name = request.cookies.get('User')
    if cookie_team == None or cookie_team == None:
        return redirect(url_for('home', message='Not_login'))
    if request.method == 'POST':
        boolean = request.values['boolean']
        qrcode = request.values['QRcode']
        if boolean == 'true':
            target = re.search(r'A[0-9]+', qrcode)
            team_score = re.search(r'[a-z]+-?[0-9]+', qrcode)
            team = re.search(r'[a-z]+', team_score.group())
            score = re.search(r'-?[0-9]+', team_score.group())
            team = dict_team[team.group()]
            score = score.group()
            if team != request.cookies.get('TeamName'):
                return redirect(url_for('go_to_team', message='Not_QRcode'))
            else:
                team_give_score(
                    team, dict_member[target.group()], (int)(score))
                return redirect(url_for('go_to_team', message='Success'))
        else:
            return redirect(url_for('go_to_team', message='QRcode_error'))
    else:
        return render_template('Reciver.html')


# 在經歷過首頁登入之後，member會有一個資料成員 team ，由team判斷該帳號是哪一個小隊，並顯示小隊頁面
@app.route('/team')
def go_to_team():
    cookie_team = request.cookies.get('TeamName')
    cookie_name = request.cookies.get('User')
    if cookie_team == None or cookie_team == None:
        return redirect(url_for('home', message='Not_login'))
    if cookie_team == '青龍':
        Dragon_trade = team_record('青龍')
        Dragon, Dragon_score = sql.get_team_table_SQL('青龍')
        return render_template('team_green.html', list=Dragon_trade.trade_list, score=Dragon_score)
    elif cookie_team == '白虎':
        Tiger_trade = team_record('白虎')
        Tiger, Tiger_score = sql.get_team_table_SQL('白虎')
        return render_template('team_white.html', list=Tiger_trade.trade_list, score=Tiger_score)
    elif cookie_team == '玄武':
        Tortoise_trade = team_record('玄武')
        Tortoise, Tortoise_score = sql.get_team_table_SQL('玄武')
        return render_template('team_black.html', list=Tortoise_trade.trade_list, score=Tortoise_score)
    elif cookie_team == '朱雀':
        Phoenix_trade = team_record('朱雀')
        Phoenix, Phoenix_score = sql.get_team_table_SQL('朱雀')
        return render_template('team_red.html', list=Phoenix_trade.trade_list, score=Phoenix_score)

    elif cookie_team.find('工作人員') != -1:
        return redirect(url_for('staff_page'))
    else:
        # print(cookie_team)
        return redirect(url_for('home', message='Error'))


@app.route('/staff', methods=['GET', 'POST'])
def staff_page():
    cookie_team = request.cookies.get('TeamName')
    cookie_name = request.cookies.get('User')
    if cookie_team == None or cookie_team == None:
        return redirect(url_for('home', message='Not_login'))
    if request.method == 'POST':
        teamname = request.values['team_name']
        if teamname == '青龍':
            teamname = 'dragon'
        elif teamname == '白虎':
            teamname = 'tiger'
        elif teamname == '朱雀':
            teamname = 'phoenix'
        elif teamname == '玄武':
            teamname = 'tortoise'
        return render_template('Generator.html', team=teamname, score=(int)(request.values['team_score']),
                               target=dict_member[cookie_name])
    if cookie_team.find('工作人員') != -1:
        authority = False
        Dragon, Dragon_score = sql.get_team_table_SQL('青龍')
        Phoenix, Phoenix_score = sql.get_team_table_SQL('朱雀')
        Tiger, Tiger_score = sql.get_team_table_SQL('白虎')
        Tortoise, Tortoise_score = sql.get_team_table_SQL('玄武')
        if cookie_team == '上級工作人員':
            authority = True
        return render_template('staff.html', Dragon=Dragon, Dragon_score=Dragon_score,
                               Phoenix=Phoenix, Phoenix_score=Phoenix_score,
                               Tiger=Tiger, Tiger_score=Tiger_score,
                               Tortoise=Tortoise, Tortoise_score=Tortoise_score, flag=authority)
    else:
        return redirect(url_for('go_to_team', message='Not_staff'))


@app.route('/record')
def get_record():
    cookie_team = request.cookies.get('TeamName')
    cookie_name = request.cookies.get('User')
    if cookie_team == None or cookie_team == None:
        return redirect(url_for('home', message='Not_login'))
    if cookie_team.find('工作人員') != -1:
        mytrade = trade_record()
        return render_template('allrecord.html', list=mytrade.trade_list)
    else:
        return redirect(url_for('go_to_team', message='Not_staff'))


@app.route('/note')
def get_note():
    cookie_team = request.cookies.get('TeamName')
    cookie_name = request.cookies.get('User')
    if cookie_team == None or cookie_team == None:
        return redirect(url_for('home', message='Not_login'))
    return render_template('campnote.html')

@app.route('/note/roommate')
def get_roommate():
    cookie_team = request.cookies.get('TeamName')
    cookie_name = request.cookies.get('User')
    if cookie_team == None or cookie_team == None:
        return redirect(url_for('home', message='Not_login'))
    return render_template('roommate.html')

@app.route('/note/schedule')
def get_schedule():
    cookie_team = request.cookies.get('TeamName')
    cookie_name = request.cookies.get('User')
    if cookie_team == None or cookie_team == None:
        return redirect(url_for('home', message='Not_login'))
    return render_template('schedule.html')

@app.route('/note/teammate')
def get_teammate():
    cookie_team = request.cookies.get('TeamName')
    cookie_name = request.cookies.get('User')
    if cookie_team == None or cookie_team == None:
        return redirect(url_for('home', message='Not_login'))
    return render_template('teammate.html')


@app.route('/delcookie')
def delete_cookie():
    if request.cookies.get('TeamName') != None:
        res = make_response(redirect(url_for('home')))
        res.delete_cookie('TeamName')
        res.delete_cookie('User')
        return res
    else:
        return redirect(url_for('home'))




# 當__name__ 等於 '__main__'時，運作該網站
if __name__ == '__main__':
    #app.debug = True
    app.run()
