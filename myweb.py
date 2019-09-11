# flask套件匯入類別、方法
from flask import Flask, render_template, request, url_for, redirect, make_response
from trade import team_give_score, trade_record, team_record
import SQL_method as sql
import re
# 自定義的Account套件，匯入兩個類別、兩個函式、四個變數
from Account import Member, login

# app就是網站啦!
app = Flask(__name__)

dict_member = sql.get_superviser_sql()
dict_team = {'phoenix': '朱雀', 'tiger': '白虎', 'tortoise': '玄武', 'dragon': '青龍'}

# 目前User的進入網站的資訊


# 裝飾器，app.route()，決定一個「路由」要做什麼事情
"""

'/' 路由

顯示首頁，即登入頁面

若使用者發出 POST 請求，表示使用者請求登入
    login函式判斷前端送出的 帳號、密碼
    回傳兩個變數給member、flag
        flag若為True，表示登入成功，那 member 將會是 Member 類別的變數
            把the_member變數，更新為該使用者的帳號密碼
            並把使用者的頁面，重新導向到 'go_to_team'函式的路由(即 '/team' 路由)
        否則，member將會是一個字串
            網頁會回應該字串member的訊息
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
            return member

    return render_template('homepage.html')


"""
'/QRscan' 路由

顯示一個QRcode scanner頁面給使用者

"""
@app.route('/QRscan', methods=['GET', 'POST'])
def QRcode_scan():
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
                return redirect(url_for('go_to_team'))
            else:
                team_give_score(
                   team, dict_member[target.group()], (int)(score))
                return redirect(url_for('go_to_team'))
        else:
            return 'QRcode 過期了啦!'
    else:
        return render_template('Reciver.html')


# 在經歷過首頁登入之後，member會有一個資料成員 team ，由team判斷該帳號是哪一個小隊，並顯示小隊頁面
@app.route('/team')
def go_to_team():
    cookie_team = request.cookies.get('TeamName')

    if cookie_team == '青龍':
        Dragon_trade = team_record('青龍')
        Dragon, Dragon_score = sql.get_team_table_SQL('青龍')
        return render_template('team_green.html', list=Dragon_trade.trade_list, score=Dragon_score)
    elif cookie_team == '白虎':
        Tiger_trade = team_record('白虎')
        Tiger, Tiger_score = sql.get_team_table_SQL('白虎')
        return render_template('team_white.html', list=Tiger_trade.trade_list, score=Tiger_score)
    elif cookie_team == '朱雀':
        Phoenix_trade = team_record('朱雀')
        Phoenix, Phoenix_score = sql.get_team_table_SQL('朱雀')
        return render_template('team_red.html', list=Phoenix_trade.trade_list, score=Phoenix_score)
    elif cookie_team == '玄武':
        Tortoise_trade = team_record('玄武')
        Tortoise, Tortoise_score = sql.get_team_table_SQL('玄武')
        return render_template('team_black.html', list=Tortoise_trade.trade_list, score=Tortoise_score)
    elif cookie_team.find('工作人員') != -1:
        return redirect(url_for('staff_page'))
    else:
        print(cookie_team)
        return '尚未登入!!'


@app.route('/staff', methods=['GET', 'POST'])
def staff_page():
    cookie_team = request.cookies.get('TeamName')
    cookie_name = request.cookies.get('User')
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
        return '不是工作人員'


@app.route('/record')
def get_record():
    cookie_team = request.cookies.get('TeamName')
    cookie_name = request.cookies.get('User')
    if cookie_team.find('工作人員') != -1:
        mytrade = trade_record()
        return render_template('allrecord.html', list=mytrade.trade_list)
    else:
        return '不是工作人員'


@app.route('/delcookie')
def delete_cookie():
    res = make_response(redirect(url_for('home')))
    res.delete_cookie('TeamName')
    res.delete_cookie('User')
    return res


# 當__name__ 等於 '__main__'時，運作該網站
if __name__ == '__main__':
    # app.debug = True
    app.run()


# 修正項目 :
# 登入密碼 全部小寫
# 一個小隊一個帳號
