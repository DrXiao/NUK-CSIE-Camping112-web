from flask import Flask,render_template,request,url_for,redirect


app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('login',account = request.values['Account'],password = request.values['Password']))

    return render_template('homepage.html')


if __name__ == '__main__':
    #app.debug = True
    app.run()