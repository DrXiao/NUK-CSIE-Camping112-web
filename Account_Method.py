import json


"""打開檔案的Function，回傳json內容的物件陣列"""
def open_Member_json():
    with open("Member.json",mode = "r",encoding="utf-8") as file:
        load_obj = json.load(file)
        return load_obj


""" 註冊新的帳號
    1.  先讀取原本的檔案，得到原本的帳號陣列
    2.  新增一個變數，內容是新的使用者資料，包含帳號、密碼
    3.  把新的使用者資料，加入陣列後面
    4.  利用檔案覆寫，把新的帳號陣列寫入json檔案裡，註冊成功
"""
def register_new_account(account,password):
    ourMember = open_Member_json()
    new_account = {"Account" : account,"Password":password}
    ourMember.append(new_account)
    with open("Member.json",mode="w",encoding= "utf-8") as file:
        json.dump(ourMember,file)


"""帳號登入功能
    1.  優先判斷使用者如果輸入空字串，直接跳出
    2.  得到json檔案裡的帳號陣列
    3.  迴圈判斷法
        A.  帳號正確、密碼正確  --> 登入成功!
        B.  帳號正確、密碼錯誤  --> 登入失敗!
        C.  跳出迴圈           --> 沒有帳號!
"""
def login_account(account,password):
    if account == '' or password == '' :
        return '沒輸入帳號或密碼!'

    ourMember = open_Member_json()
    for i in range(len(ourMember)):
        if ourMember[i]["Account"] == account:
            if ourMember[i]["Password"] == password:
                return '輸入正確!'
            else:
                return '帳號對但是密碼錯囉!'
    
    return '你沒申請帳號喔!'


