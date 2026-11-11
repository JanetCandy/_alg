# 定義表格標題欄位
headers = [
    "第幾週",
    "習題內容",
    "有上課且準時繳交",
    "補交",
    "附上請假證明",
    "作業連結",
]

# 定義你的表格內容資料（你可以直接在這裡修改、新增或刪除行）
rows = [
    [
        "1", 
        "查表法", 
        "是", 
        "", 
        "", 
        "[week1](https://github.com/JanetCandy/_alg/tree/main/homework/week1)"
    ],
    [
        "2", 
        "複雜度", 
        "是", 
        "", 
        "", 
        "[week2](https://github.com/JanetCandy/_alg/tree/main/homework/week2)"
    ],
    [
        "3", 
        "列舉＋暴力", 
        "是", 
        "", 
        "", 
        "[week3]"(https://github.com/JanetCandy/_alg/tree/main/homework/week3)
    ],
    [
        "4", 
        "迭代法", 
        "是", 
        "", 
        "", 
        "[week4](https://github.com/JanetCandy/_alg/tree/main/homework/week4)"
    ],
    [
        "5",
        "遞迴，函數式編程",
        "是",
        "",
        "",
        "[week5](https://github.com/JanetCandy/_alg/tree/main/homework/week5)",
    ],
    [
        "6", 
        "Lambda Calculus", 
        "是", 
        "", 
        "", 
        "[week6](https://github.com/JanetCandy/_alg/tree/main/homework/week6)"
    ],
    [
        "7", 
        "動態規劃與文字算法", 
        "是", 
        "", 
        "", 
        "[week7](https://github.com/JanetCandy/_alg/tree/main/homework/week7)"
    ],
    [
        "8", 
        "優化算法", 
        "是", 
        "", 
        "", 
        "[week8](https://github.com/JanetCandy/_alg/tree/main/homework/week8)"
    ],
    [
        "9", 
        "搜尋算法", 
        "是", 
        "", 
        "", 
        "[week9](https://github.com/JanetCandy/_alg/tree/main/homework/week9)"
    ],
    
]


def generate_markdown_table(headers, rows):
  """將標題與資料轉換為 Markdown 表格字串"""
  # 產生表頭
  md = "| " + " | ".join(headers) + " |\n"
  # 產生分隔線（對齊線）
  md += "| " + " | ".join(["---"] * len(headers)) + " |\n"
  # 產生各列資料
  for row in rows:
    md += "| " + " | ".join(str(cell) for cell in row) + " |\n"
  return md


# 產生 Markdown 格式表格
table_markdown = "## 每週檢驗表格\n\n" + generate_markdown_table(headers, rows)

# 1. 印在螢幕上查看
print(table_markdown)

# 2. 自動寫入專案的 README.md 檔案中（若有需要可取消下方註解）
# with open("README.md", "w", encoding="utf-8") as f:
#     f.write(table_markdown)
#     print("已成功更新 README.md 檔案！")