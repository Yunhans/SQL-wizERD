# 簡介

> 這是一個利用 AI 幫助初學者建立資料庫以及 ERD 的網頁小工具

開發成員們
| 姓名 | github | 主要負責 |
| :--: | :-- | :--: |
| 石昀翰 | @Yunhans | 前端 |
| 管奕凱 | @CalvinKuan1007 | AI |
| 林均翰 | @HenryLin1412 | 資料庫 |
| 朱博脩 | @shioudidi | 後端 |
| 黃柏翰 | @hbh10601 | AI+使用說明(魔法書) |

# 使用說明

> 需要 python3.10 或以上版本

1. 下載 
    - MySQL Server 8.0.38 [點此下載](https://dev.mysql.com/downloads/mysql/)
    - MySQL WorkBench 8.0.38 [點此下載](https://dev.mysql.com/downloads/mysql/)
    - NodeJS 20.15.1 [點此下載](https://nodejs.org/en/download/prebuilt-installer)
> 檢查版本
```bash
python3 -V      # should print Python 3.11.9(recommend)  or above
node -v         # should print `v20.15.1` or above
npm -v          # should print `10.7.0` or above
```

2. 利用 MySQL WorkBench 與 MySQL Server Localhost 連線之後跑 [schema](Graduated_Project_test.sql) 建立資料庫

3. 下載並將下面兩個檔案放進本資料夾最外層(與main.py同層級)
    - [myconfig.py](https://drive.google.com/drive/u/0/folders/15-sAc_Mu2l6ROezuPmi5HhFCdFezt0ED)
    - [connectdb.py](https://drive.google.com/drive/u/0/folders/15-sAc_Mu2l6ROezuPmi5HhFCdFezt0ED)
> 記得修改 Localhost 連線 user & password

4. 建立python虛擬環境並將 cmd 或 terminal 路徑 cd 至本資料夾
```bash
cd graduate-project
```

5. 下載 pip 套件
```bash
pip install fastapi

pip install "uvicorn[standard]"

pip install -r requirements.txt
```

6. 執行 main.py
```bash
uvicorn main:app --reload
```

7. 新增 cmd 視窗 cd 進去 frontend 資料夾，下載 React 所需套件並執行
```bash
cd frontend

npm install

npm start           # Mac
npm run start-pc    # Windows
```

8. 打開瀏覽器路由 `http://127.0.0.1:8000/`

# 預計製作功能

- [x] fastapi 主頁架設
- [x] 登入系統(google 帳號) (朱)
- 白板功能 (石)
    - [x] 資料表拖拉
    - [x] 白板縮放
    - [x] 白板拖拉
    - [x] 關聯線條呈現
    - [x] json 資料 API 串接
    - [x] chatbot 串接
- [x] 語法偵錯 (朱)
- [x] chatbot 模型微調 (管)
- [ ] 小教程 (林)
- [x] 存檔 (林)

# 參考連結
1. [雲端硬碟]()

# Acknowledgements

This project uses the following open source projects:
- [Create React App](https://github.com/facebook/create-react-app) - Licensed under the [MIT License](https://github.com/facebook/create-react-app/blob/main/LICENSE) 
- [xyflow](https://github.com/xyflow/xyflow) - Licensed under the [MIT License](https://github.com/xyflow/xyflow/blob/main/LICENSE) 
