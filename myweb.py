# flask套件匯入類別、方法
from flask import Flask, render_template, request, url_for, redirect, make_response
from trade import team_give_score
"""
翻譯時間

Flask : 網站主體的class  (可能是class沒錯)
render_template : 函式，顯示一個html網頁
request : 函式，判斷前端發出POST、GET請求等等
url_for : 函式，會逆向分析，從一個函式找到它的路由為何
redirect : 函式，把前端重新導向一個新路由
"""

# 自定義的Account套件，匯入兩個類別、兩個函式、四個變數
from Account import Member, Team, login
from Account import Dargon_team, Tiger_team, Phoenix_team, Tortoise_team

# app就是網站啦!
app = Flask(__name__)

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
    if request.method == 'POST':
        member, flag = login(
            request.values['Account'], request.values['Password'])
        if flag == True:
            the_member.renew(member.Name, member.Account,
                             member.Password, member.team)
            res = make_response(redirect(url_for('go_to_team')))
            res.set_cookie('TeamName', the_member.team)
            return res
        else:
            return member

    return render_template('homepage.html')


"""
'/QRscan' 路由

顯示一個QRcode scanner頁面給使用者

QRscanner.html已設計好，當掃到QRcode時，會自動發出POST請求
    此時網頁會回應該QRcode的網址

這方面再請參閱 QRscanner.html 網頁檔案
"""
@app.route('/QRscan', methods=['GET', 'POST'])
def QRcode_scan():
    if request.method == 'POST':
        return request.values['QRcode']
    return render_template('QRscanner.html')


# 在經歷過首頁登入之後，member會有一個資料成員 team ，由team判斷該帳號是哪一個小隊，並顯示小隊頁面
@app.route('/team')
def go_to_team():
    cookie = request.cookies.get('TeamName')

    if cookie == '青龍':
        return render_template('team_green.html')
    elif cookie == '白虎':
        return render_template('team_white.html')
    elif cookie == '朱雀':
        return render_template('team_red.html')
    elif cookie == '玄武':
        return render_template('team_black.html')
    elif  cookie== '工作人員':
        return redirect(url_for('staff_page'))
    else:
        print(cookie)
        return '尚未登入!!'


@app.route('/staff', methods=['GET', 'POST'])
def staff_page():
    cookie = request.cookies.get('TeamName')
    if cookie== '工作人員':
        return render_template('staff.html', Dragon=Dargon_team.TeamName, Dragon_score=Dargon_team.Score,
            Phoenix=Phoenix_team.TeamName, Phoenix_score=Phoenix_team.Score,
             Tiger=Tiger_team.TeamName, Tiger_score=Tiger_team.Score,
             Tortoise=Tortoise_team.TeamName, Tortoise_score=Tortoise_team.Score)
    else:
        return '不是工作人員'


@app.route('/record')
def get_record():
    cookie = request.cookies.get('TeamName')
    if cookie == '工作人員':
        return render_template('allrecord.html')
    else:
        return '不是工作人員'


# 當__name__ 等於 '__main__'時，運作該網站
if __name__ == '__main__':
    app.debug = True
    app.run()
