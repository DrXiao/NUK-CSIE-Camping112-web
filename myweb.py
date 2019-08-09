#flask套件匯入類別、方法
from flask import Flask,render_template,request,url_for,redirect

from QRscanner import detect
#自定義的套件，匯入三個函式
from Account import login,register_new_account

# __name__ 目前執行的模組
app = Flask(__name__)

Person = []

#裝飾器，app.route()，決定一個「路由」要做什麼事情
"""
當路由是「'/'」(根目錄)的時候，顯示首頁，且該路由可以接受前端的GET、POST請求
若沒有接受到前端的任何請求，顯示首頁頁面

如果接受到來自前端的'POST'請求，則讓前端登入帳號

context 變數，表示登入的對錯資訊字串
若context的字串是 '正確!'，那麼就利用logined_page函式，返回一個「個人頁面」
否則，就對前端顯示client的錯誤資訊

Person 陣列，表示從資料庫取得的所有人的帳號密碼資訊
是一個二維陣列，取得的資訊會長這樣
[
(帳號,密碼,人名),
(帳號,密碼,人名),
.
.
.
]

Person[i]，表示取得第i個人的所有資訊(變成一維陣列)
Person[i][0]，表示第i個人的帳號
以此類推

使用「循序搜尋法」，尋找該帳號，核對密碼，即為判斷登入成不成功的方式
"""
@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        context,Person = login(request.values['Account'],request.values['Password'])
        if context == '正確!':
            return render_template('person_page.html',Name = Person[2], Account = Person[0], Password = Person[1],QRCODE = '')
        else:
            return context

    return render_template('homepage.html')


"""
路由是「'/registration'」，顯示註冊網頁，並能接受GET,POST請求

如果接受到前端的POST請求，利用自定義模組「Account」的register_new_method方法，進行註冊
會將相關資訊寫進資料庫
"""
@app.route('/registration',methods = ['GET','POST'])
def registration_page():
    if request.method == 'POST':
        register_new_account(request.values['Name'],request.values['Account'],request.values['Password'])
        return '註冊成功!'

    return render_template('registration.html')

@app.route('/QRscan')
def qrcode_scan():
    Data = detect()
    return render_template('person_page.html',Name = '', Account = '', Password = '',QRCODE = Data)


# 當__name__ 等於 '__main__'時，運作該網站
if __name__ == '__main__':
    app.debug = True
    app.run()