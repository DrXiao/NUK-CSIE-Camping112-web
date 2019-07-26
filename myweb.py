from flask import Flask,render_template,request,url_for,redirect
from Account import login,find_account,register_new_account

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        Person = []
        context,Person = login(request.values['Account'],request.values['Password'])
        if context == '正確!':
            return redirect(url_for('logined_page',Account = Person[0]))
        else:
            return context

    return render_template('homepage.html')

@app.route('/<Account>')
def logined_page(Account):
    list = []
    list = find_account(Account)
    return render_template('person_page.html',Name = list[2], Account = list[0], Password = list[1])

@app.route('/registration',methods = ['GET','POST'])
def registration_page():
    if request.method == 'POST':
        register_new_account(request.values['Name'],request.values['Account'],request.values['Password'])
        return '註冊成功!'

    return render_template('registration.html')

if __name__ == '__main__':
    #app.debug = True
    app.run()