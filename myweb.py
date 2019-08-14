#flask套件匯入類別、方法
from flask import Flask,render_template,request,url_for,redirect,Response

#自定義的套件，匯入三個函式
from Account import Member,Team,login,register
from Account import Dargon_team,Tiger_team,Phoenix_team,Tortoise_Team
app = Flask(__name__)

the_member = Member('','','','')

#裝飾器，app.route()，決定一個「路由」要做什麼事情
@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        member,flag = login(request.values['Account'],request.values['Password'])
        if flag ==True:
            the_member.renew(member.Name,member.Account,member.Password,member.team)
            return redirect(url_for('go_to_team'))
        else:
            return member

    return render_template('homepage.html')


"""
路由是「'/registration'」，顯示註冊網頁，並能接受GET,POST請求

如果接受到前端的POST請求，利用自定義模組「Account」的register_new_method方法，進行註冊
會將相關資訊寫進資料庫
"""
@app.route('/registration',methods = ['GET','POST'])
def registration_page():
    if request.method == 'POST':
        flag = register(request.values['Name'],request.values['Account'],request.values['Password'],request.values['Teampassword'])
        print(flag)
        if flag == True:
            return redirect(url_for('home'))
        else:
            return flag
    return render_template('registration.html')

@app.route('/QRscan',methods =['GET','POST'] )
def QRcode_scan():
    if request.method == 'POST':
        return request.values['QRcode']
    return render_template('QRscanner.html')

@app.route('/team')
def go_to_team():
    if the_member.team == '青龍':
        return render_template('team_green.html',team = the_member.team,Name = the_member.Name,Account = the_member.Account,Score = Dargon_team.Score)
    elif the_member.team == '白虎':
        return render_template('team_white.html',team = the_member.team,Name = the_member.Name,Account = the_member.Account,Score = Tiger_team.Score)
    elif the_member.team == '朱雀':
        return render_template('team_red.html',team = the_member.team,Name = the_member.Name,Account = the_member.Account,Score = Phoenix_team.Score)
    elif the_member.team == '玄武':
        return render_template('team_black.html',team = the_member.team,Name = the_member.Name,Account = the_member.Account,Score = Tortoise_Team.Score)
    else:
        print(the_member.team)
        return '尚未登入!!'

    
# 當__name__ 等於 '__main__'時，運作該網站
if __name__ == '__main__':
    #app.debug = True
    app.run()