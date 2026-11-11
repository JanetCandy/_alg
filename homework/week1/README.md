# Homework 1: Power of 2 (power2n.py)

這是演算法課程的第一份作業，主要探討計算 $2^n$ 的不同實作方法（數學運算、純遞迴、遞迴加查表）及其效能差異。

## 📁 檔案內容
* `power2n.py`：包含四種不同方法的實作與效能測試主程式。

---

## 🔍 方法說明與效能分析 ($n = 100$)

| 方法名稱 | 實作邏輯 | 時間複雜度 | 執行狀態 / 表現 |
| :--- | :--- | :--- | :--- |
| **方法 1** | 數學次方運算 (`2 ** n`) | $O(1)$ 或 $O(\log n)$ | **極快**。Python 底層對大數運算有高度優化，瞬間完成。 |
| **方法 2a** | 雙分支遞迴 (`f(n-1) + f(n-1)`) | $O(2^n)$ | **出不來**。運算次數高達 $2^{100}$，會導致程式無限期卡死或引發 `RecursionError`。 |
| **方法 2b** | 單分支遞迴 (`2 * f(n-1)`) | $O(n)$ | **正常跑完**。遞迴深度為 100 層，可順利得出結果，但遞迴開銷比方法 1 稍大。 |
| **方法 3** | 遞迴 ＋ 查表 (Memoization) | $O(n)$ | **快速**。透過字典記錄已計算過的值，避免重複計算。 |

---

## 💻 程式碼範例 (`power2n.py`)

```python
import time

# 方法 1：數學次方運算
def power2n_method1(n):
    return 2 ** n

# 方法 2a：用遞迴 (Repeated addition)
def power2n_method2a(n):
    if n == 0:
        return 1
    return power2n_method2a(n - 1) + power2n_method2a(n - 1)

# 方法 2b：用遞迴 (Multiplication)
def power2n_method2b(n):
    if n == 0:
        return 1
    return 2 * power2n_method2b(n - 1)

# 方法 3：用遞迴 + 查表
memo = {0: 1}
def power2n_method3(n):
    if n in memo:
        return memo[n]
    memo[n] = power2n_method3(n - 1) + power2n_method3(n - 1)
    return memo[n]

if __name__ == "__main__":
    n = 100
    print(f"方法 1 結果: {power2n_method1(n)}")
    print(f"方法 2b 結果: {power2n_method2b(n)}")
    print(f"方法 3 結果: {power2n_method3(n)}")