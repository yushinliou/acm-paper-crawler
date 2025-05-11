# I read this so you don't have to

```
crawler/
├── __init__.py
├── run.py           # 主程式
├── parser.py        # 分析 HTML 的邏輯
├── fetch.py         # 負責請求網頁
├── utils.py         # 工具函式
├── papers.json      # 爬到的資料
└── requirements.txt # 爬蟲用的套件
```

# 修正

* IP要Rotate
* 順便爬下來論文的背景資料，例如下載次數
* 記錄一下上次爬到哪裡，已經爬過的不用接著爬

