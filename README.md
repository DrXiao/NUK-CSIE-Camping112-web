# Test-web
測試網站

所有code都在這歐

# 使用工具
* Visual Studio Code (VScode) : 

  * 不同於Visual Studio，只是個文字編輯器(不是IDE喔)，但只要裝好語言環境並設定好，幾乎所有程式語言都能寫。
 
  * 優點是可直接使用終端機(Coding有時候需要用命令提示字元打指令，VScode介面直接提供終端機介面直接打指令)。
 
  * 須裝Extensions(擴充套件)，才能使用Python
 
* Python 3.7.3 : Python環境，版本是3.7.3
* Python第三方套件 -- flask : 本次架設後端的主角，用Python的pip工具安裝
* Python第三方套件 -- psycopg2 : 可連結PSQL資料庫的套件，同樣要用pip工具安裝
* Heroku CLI : Heroku的工具，只有在最一開始部署網站到Heroku才用到
* Git 工具 : Very important 的工具，可以管理程式碼的各種事情，要用終端機操作指令才能部署網站到Heroku

# 檔案說明 : 
* __pycache__  資料夾 : 執行檔的資料夾
   * py檔案的「執行檔」，都會存在於此資料夾
    
   * 若有新的py檔案產生，上傳到Heroku時，會自動生成該py檔案的執行檔
    
   * 目前有三個執行檔
    
* static 資料夾 : 靜態資料夾，顧名思義這裡頭的檔案基本上都是靜態的
   * 包含 css、javascript、圖片的檔案等等
   
   * 現在裡面有 css資料夾、imgs資料夾
     * css 資料夾 : 松林做的css檔案，有被我小改過
     * img資料夾 : 松林放的圖片
     
   * html 若要用css、javascript的內容，都要到static找，所以herf就要打資料夾的路徑 (EX: herf = "/static/css/login_style.css")
     
* template 資料夾 : html檔案的集合
   * Flask要使用html網頁，都是到template找
   
   * 目前包含7個html檔案，松林做的前端頁面，有些已經被我套用了
   
   * mypage 資料夾 裡面是松林打的東西，不知道有啥功用，跪求松林解答
   
* Account.py : 自製的py檔案，內含有關處理"帳號"、"小隊" 相關資訊的class、function，以及事先宣告好的變數等等

* Procfile : 與Heroku相關的檔案，主要是告訴伺服器如何執行網站

* README.md : 就是你正在看的這一份文件，可線上編輯，可讓大家看到相關訊息

* SQL_method.py : 可操作我們網站的資料庫，相關函式的py檔案，主要有 在資料庫建立表格、在資料庫取得表格 等等函式

* requirements.txt : 告知Heroku，我們的檔案需要哪些套件與版本 (告知Heroku使用 Flask、gunicorn、psycopg2 套件)

* runtime.txt : 告訴Heroku，我們的Python環境版本為3.7.3

* myweb.py : 我們網站的主程式
   


# ==後端架設情況(8/15)   完成總%數評估--> 25% / 50% ==

### 1. QRcode scanner (15%):

已完成QRcode scanner，可掃描QRcode並在網頁看到網址

QRcode設計尚未完成(工作人員輸入分數量，可令小隊獲得分數)

可再小隊專屬頁面，按下 打開相機 ，開啟Scanner

評估完成%數: 8%

### 2. 交易系統 (10%):

未做，跪求RPG遊戲組速速列出所需功能

評估完成%數: 0%

### 3. 伺服器架設 (10%):

使用Heroku網站，提供免費伺服器、資料庫

成功部署網站並讓大家使用

資料庫為PSQL，已建立的資訊如下

Member 表格 : 一個人 名字、帳號、密碼、所屬小隊名稱

Team 表格 : 一個小隊 小隊名字、小隊分數

評估完成%數 : 8%

### 4. 登入系統 (15%):

有帳號登入功能、註冊帳號功能

登入成功後會顯示小隊專屬頁面、顯示小隊分數

註冊功能可令同學註冊一組帳密、並分配小隊

註冊的小隊密碼:

  * IamDargonTeam : 青龍小隊
  
  * BeTigerTeam : 白虎小隊
  
  * WeArePhoenixTeam : 朱雀小隊
  
  * GoToTortoiseTeam : 玄武小隊

這個是暫時的方案，小隊我們自己分

評估完成%數 : 9%


# ==前端架設情況==

未知? 

跪求前端組 松林 ㄏㄏ 告知
