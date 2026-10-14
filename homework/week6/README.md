readme_content = """# Lambda Calculus Interpreter (λ-calculus 解譯器)

這是一個以 **Python** 實作的輕量級 **Lambda Calculus（蘭姆達演算）解譯器**。它支援帶有名稱（Named）的 Lambda 表達式解析，並能逐步顯示完整的 **Beta-Reduction（貝塔歸約）** 計算過程與變數代換細節。

---

## 🚀 功能特色

* **完整的 AST 支援**：支援三種基本的 Lambda 運算子：
  * **變數 (Variable)**：如 `x`
  * **抽象 (Abstraction)**：如 `\\x. x`（代表 $\\lambda x. x$）
  * **應用 (Application)**：如 `(f x)`
* **內建詞法與語法解析器 (Lexer & Parser)**：可直接將帶有括號和反斜線的字串表達式轉換為抽象語法樹。
* **Alpha 轉換防護（避免變數捕捉）**：在進行 `substitute`（取代）時會檢查自由變數，自動處理變數名稱衝突，確保運算正確性。
* **詳細的計算過程追蹤**：每一步 Beta-Reduction 都會明確印出代換的參數與當前的樹狀結構狀態。

---

## 📦 專案檔案結構

* `lambda_interpreter.py`：包含語法樹定義、解析器、Beta-Reduction 引擎與測試範例的完整程式碼。
* `README.md`：專案說明文件。

---

## 🛠️ 安裝與執行

本專案僅使用 Python 標準函式庫（如 `re`），無需安裝任何外部第三方套件。

### 1. 系統需求
* **Python 3.x**

### 2. 執行方式
將解譯器程式碼儲存為 `lambda_interpreter.py` 後，在終端機（Terminal）執行：

```bash
python lambda_interpreter.py