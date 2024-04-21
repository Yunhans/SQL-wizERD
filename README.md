# 簡介

- 這是一個利用 AI 幫助初學者建立資料庫以及 ERD 的網頁小工具 

# 使用說明

- 需要 python3.8 或以上版本

### 1. 將 cmd 或 terminal 路徑 cd 至本資料夾
```bash
cd graduate_project
```

### 2. 下載 fastapi 以及 uvicorn
```bash
pip install fastapi
```

```bash
pip install "uvicorn[standard]"
```

### 3. 執行 main.py
```bash
uvicorn main:app --reload
```

### 4. 打開瀏覽器路由 http://127.0.0.1:8000/

# 預計製作功能

- [x] fastapi 主頁架設
- [ ] 登入系統(google 帳號)

