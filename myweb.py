#flask套件匯入類別、方法
from flask import Flask,render_template,request,url_for,redirect,Response

#自定義的套件，匯入三個函式
from Account import Member
app = Flask(__name__)

member = Member('','','')

#裝飾器，app.route()，決定一個「路由」要做什麼事情
@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        pass

    return render_template('homepage.html')


"""
路由是「'/registration'」，顯示註冊網頁，並能接受GET,POST請求

如果接受到前端的POST請求，利用自定義模組「Account」的register_new_method方法，進行註冊
會將相關資訊寫進資料庫
"""
@app.route('/registration',methods = ['GET','POST'])
def registration_page():
    if request.method == 'POST':
        pass
    return render_template('registration.html')

@app.route('/QRscan',methods =['GET','POST'] )
def QRcode_scan():
    if request.method == 'POST':
        return request.values['QRcode']
    return render_template('QRscanner.html')


# 當__name__ 等於 '__main__'時，運作該網站
if __name__ == '__main__':
    app.debug = True
    app.run()