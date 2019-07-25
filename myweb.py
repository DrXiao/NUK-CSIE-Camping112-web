from flask import Flask,render_template,request,url_for,redirect

#從自定義的Account_Method模組匯入兩個函式
from Account_Method import register_new_account,login_account

app = Flask(__name__)

""" 路由在"根目錄"時
    1.  呈現"homepage.html"網頁，給出可輸入帳號密碼的TextField
    2.  如果client有做出'POST'請求，用login函式判斷要做出什麼回應
"""
@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        return login(request.values['Account'],request.values['Password'])
    return render_template('homepage.html')

""" login登入函式
    從Account_Mathod匯入的函式login_account去判斷有沒有登入正確的帳號
    否則就顯示錯誤訊息給client
"""
def login(account,password):
    login_context = login_account(account,password)
    if login_context == '輸入正確!':
        return redirect(url_for('logined',account = account))
    else:
        return login_context


""" 路由在'/registration'時，進入到'registration.html'網頁
    1.  呈現registration.html的網頁，可申請註冊
    2.  當client發出'POST'請求時，先從Account_Method裡使用register_new_account函式，寫進json檔案
        註冊成功後再回到首頁

"""
@app.route('/registration',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        register_new_account(request.values['Account'],request.values['Password'])
        return redirect(url_for('home'))

    return render_template('registration.html')


""" 登入成功時
    顯示歡迎的訊息
"""
@app.route('/login/<account>')
def logined(account):
    return render_template('login.html',Account = account)


if __name__ == '__main__':
    #app.debug = True
    app.run()