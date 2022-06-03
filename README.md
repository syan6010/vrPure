# django實作的簡易GIS系統
*pure版本原始版本* by l3056762892(108207442同學)
## 使用之前
1. 創建一個虛擬環境（名稱要符合gitignore裏面的設定）
   #### windows
      ```shell
       python -m venv 虛擬環境的名稱
      ```
   #### Linux使用之前記得先安裝python venv
     ```shell
     python3 -m venv 虛擬環境的名稱
     ```
2. 切換到剛剛創建的venv
   #### windows
      ```shell
       剛剛設定的虛擬環境名稱\Scripts\activate
      ```
   #### Linux
     ```shell
     source 剛剛設定的虛擬環境名稱/bin/activate
     ```
3. 在虛擬環境裏面安裝會用到的套件(可以使用admin來開啓)
    ```shell
    pip install -r requirements.txt
    ```
4. 在gisweb資料夾當中新增media資料夾與preImg,reImg存放圖片
       結構如下：
    ```
           webGis_pure  
           └───gisweb
           │   └───media
           │       │ preImg
                   | reImg
     ```
5. 進入gisweb當中啓動server
    ```shell
    cd gisweb
   python manage.py runserver
    ```

    如果是https的時候
    ```shell
    python manage.py runserver_plus --cert server.crt 0.0.0.0:8000
    ```


## 功能介紹
**- 地圖功能（map.html）**
 1.尚未登入的使用者透過地圖協作的功能能夠看到所有使用者上傳的點位，而登入過後的使用者這可以查看自己所上傳的點位
 
 2.透過上方的查詢列表可以針對點位進行模糊搜索 
 
 3.點選地圖的marker後彈出popup視窗顯示出簡易點位説明
 
 4.點選地圖的popup時候會進入全景模式，如果使用行動裝置開啓則是能夠直接使用VR眼睛瀏覽360°照片 
 
 5.使用leaflet,以及國土測繪中心圖層進行圖層的切換
 
------------
**- 登入功能(login.html)**

1.輸入帳號密碼後即可登入系統（透過session獲得使用者資訊）此時主頁（index.html）的導覽列新增會員功能     選項提供使用者新增及修改動作

----

 **- 注冊功能(profileUpdate.html)** 
 
 1.提供用戶簡易的注冊頁面
 
 ----

 **- 新增功能(add.html)** 
 
 1.提供用戶上傳照片以及點位資料，透過用戶上傳的相片讀取exif，取得相片中的經緯度坐標以便與地圖上顯示點位
 
 ----
 
 ## 版本BUG與待修改部分

**- 地圖功能（map.html）**
- GIS功能擴充
- 資料框UI美化（相片大小的統一化）
- Choose bar 的資料庫化
- FLASH MESSAGE錯誤對話框提示
~~Search bar(關鍵字搜索&單獨搜索)~~
~~- 讀取CHOOSE BAR（建物植物~~
~~- 套用國土中心api~~
~~- 資料總覽BUTTON~~


 **- 新增功能(add.html)** 
- 上傳錯誤的提示與預設值（點位不存在的狀況）
~~- exif照片大小的更改與新資料夾的設定~~
- 照片預覽功能與頁面美化(動態表單的解決方案)
- 新資料欄位的建立（UPDATE-TIME）
- heic照片問題


**- 登入功能(login.html)**


- 登入功能基礎完善
- 忘記密碼功能
~~- profileUpdate（注冊頁面）~~
~~- 登入畫面的建製~~
- 注冊頁面的密碼確認（前端）

**- 報錯頁面(login.html)**

- 正確的錯誤提示
~~錯誤頁面的顯示~~

**DATABASE**
透過外鍵正規化資料庫（username）

  |ImgData   |   |
| ------------ | ------------ |
|   title|   |
|   content|   |
|   create_at   |  |
|  photo |   |
|   img_create_at |   |
|  lon |   |
|   lat |   |
|   username | 外鍵   |



**使用工具**

- 網頁框架：django
- 資料庫：firebase
- 地圖：leaflet.js
- 底圖資源：國土測繪中心 wmts
- VR框架：aframe.js

--------------


整體
利用extend, block精簡程式碼


## 專案啓動方式
**1.建構虛擬環境**

```bash
C:\Users\YOUR_NAME\<資料夾名稱>> python -m venv <虛擬環境的名字>
```

**2.啓動虛擬環境**
 
 ```bash
C:\Users\YOUR_NAME\<資料夾名稱>> <虛擬環境的名字>\Scripts\activate
```
**3.啓動伺服器**

 ```bash
cd C:\Users\YOUR_NAME\<app名稱>> 
python manage.py runserver (0.0.0.0:80) \\對外啓動伺服器

```
## git上傳

 ```bash
git add --all 
git commit -m "init commit" \\本地推送
git push origin HEAD:"遠端branch名稱" \\推送到指定的遠端branch 
```
 
設定remote
```bash
git remote add origin 遠端倉庫網址
git branch -M main
git push -u origin main
```
