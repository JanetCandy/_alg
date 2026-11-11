import os

# 定義表格標題欄位
headers = [
    "第幾週",
    "習題內容",
    "有上課且準時繳交",
    "補交",
    "附上請假證明",
    "作業連結",
]

# 定義你的表格內容資料
rows = [
    [
        "1",
        "查表法",
        "是",
        "",
        "",
        "[week1](https://github.com/JanetCandy/_alg/tree/main/homework/week1)",
    ],
    [
        "2",
        "複雜度",
        "是",
        "",
        "",
        "[week2](https://github.com/JanetCandy/_alg/tree/main/homework/week2)",
    ],
    [
        "3",
        "列舉＋暴力",
        "是",
        "",
        "[week3](https://github.com/JanetCandy/_alg/tree/main/homework/week3)",
        "",
    ],
    [
        "4",
        "迭代法",
        "是",
        "",
        "",
        "[week4](https://github.com/JanetCandy/_alg/tree/main/homework/week4)",
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
        "[week6](https://github.com/JanetCandy/_alg/tree/main/homework/week6)",
    ],
    [
        "7",
        "動態規劃與文字算法",
        "是",
        "",
        "",
        "[week7](https://github.com/JanetCandy/_alg/tree/main/homework/week7)",
    ],
    [
        "8",
        "優化算法",
        "是",
        "",
        "",
        "[week8](https://github.com/JanetCandy/_alg/tree/main/homework/week8)",
    ],
    [
        "9",
        "搜尋算法",
        "是",
        "",
        "",
        "[week9](https://github.com/JanetCandy/_alg/tree/main/homework/week9)",
    ],
]


def generate_markdown_table(headers, rows):
  """將標題與資料轉換為 Markdown 表格字串"""
  md = "| " + " | ".join(headers) + " |\n"
  md += "| " + " | ".join(["---"] * len(headers)) + " |\n"
  for row in rows:
    md += "| " + " | ".join(str(cell) for cell in row) + " |\n"
  return md


# 產生 Markdown 格式表格
table_markdown = "## 每週檢驗表格\n\n" + generate_markdown_table(headers, rows)

# 印在螢幕上檢查內容是否正確
print("--- 產生的 Markdown 內容預覽 ---")
print(table_markdown)
print("---------------------------------")

# 寫入檔案並確認絕對路徑
filename = "README.md"
with open(filename, "w", encoding="utf-8") as f:
  f.write(table_markdown)

print(
    f"已成功寫入！檔案儲存於: {os.path.abspath(filename)}"
)  # 顯示檔案實際存放在電腦哪裡