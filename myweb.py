from flask import Flask,render_template,request,url_for,redirect
import Account
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('login',account = request.values['Account'],password = request.values['Password']))

    return render_template('homepage.html')

@app.route('/login:<account>_and_<password>')
def login(account,password):
    test = Account.login_test(account,password)
    if test == True:
        return render_template('login.html',Account = account,Password = password)

    elif test == False:
        return '你輸入錯囉!'

@app.route('/registration',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        Account.register_new(request.values['Account'],request.values['Password'])
        return '註冊成功!'
    
    return render_template('registration.html')

if __name__ == '__main__':
    #app.debug = True
    app.run()