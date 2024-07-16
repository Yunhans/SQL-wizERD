# 簡介

> 這是一個利用 AI 幫助初學者建立資料庫以及 ERD 的網頁小工具

開發成員們
| 姓名 | github | 主要負責 |
| :--: | :-- | :--: |
| 石昀翰 | @Yunhans | 前端 |
| 管奕凱 | @CalvinKuan1007 | AI |
| 林均翰 | @HenryLin1412 | 後端 |
| 朱博脩 | @shioudidi | 後端 |
| 黃柏翰 | @hbh10601 | AI |

# 使用說明

> 需要 python3.10 或以上版本

1. 將 cmd 或 terminal 路徑 cd 至本資料夾
```bash
cd graduate_project
```

2. 下載 pip 套件
```bash
pip install fastapi

pip install "uvicorn[standard]"

pip install -r requirements.txt
```

3. 執行 main.py
```bash
uvicorn main:app --reload
```

4. 打開瀏覽器路由 http://127.0.0.1:8000/

# 預計製作功能

- [x] fastapi 主頁架設
- [x] 登入系統(google 帳號) (朱)
- 白板功能 (石)
    - [x] 資料表拖拉
    - [ ] 關聯線條呈現
    - [ ] json 資料 API 串接
- [ ] 語法偵錯 (朱)
- [ ] chatbot
- [ ] 小教程 (林)
- [ ] 雲端存檔 (林)


5. test data:

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL UNIQUE,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    PhoneNumber VARCHAR(20)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE NOT NULL,
    TotalAmount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);




