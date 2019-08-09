#flask套件匯入類別、方法
from flask import Flask,render_template,request,url_for,redirect,Response

#自定義的套件，匯入三個函式
from Account import login,register_new_account,Member
import cv2
import pyzbar.pyzbar
app = Flask(__name__)

member = Member('','','')

def decodeDisplay(image):
    barcodes = pyzbar.pyzbar.decode(image)
    Data = ''
    for barcode in barcodes:
        # 提取条形码的边界框的位置
        # 画出图像中条形码的边界框
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
        # 条形码数据为字节对象，所以如果我们想在输出图像上
        # 画出来，就需要先将它转换成字符串
        Data = barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
 
        # 绘出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    .5, (0, 0, 125), 2)
 
        # 向终端打印条形码数据和条形码类型
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    return image

class VideoCamera(object):
    def __init__(self):
     # 通过opencv获取实时视频流
        self.video = cv2.VideoCapture(0) 

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        image2 = decodeDisplay(image)
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', image2)
        return jpeg.tobytes()


@app.route('/QRscan')  # 主页
def index():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('test.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():
    return Response(gen(VideoCamera()),
                mimetype='multipart/x-mixed-replace; boundary=frame')   

#裝飾器，app.route()，決定一個「路由」要做什麼事情

@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        context,Person = login(request.values['Account'],request.values['Password'])
        if context == '正確!':
            member.change(Person[0],Person[1],Person[2])
            return render_template('person_page.html',Name = member.Name, Account = member.Account, Password = member.Password,QRCODE = '')
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


# 當__name__ 等於 '__main__'時，運作該網站
if __name__ == '__main__':
    #app.debug = True
    app.run()