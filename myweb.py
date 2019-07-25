from flask import Flask,render_template,request,url_for,redirect


app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def home():
    
    return render_template('homepage.html')

@app.route('/test')
def test():
    return 'test123456789!!!'

if __name__ == '__main__':
    #app.debug = True
    app.run()