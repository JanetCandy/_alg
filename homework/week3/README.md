# Week3
要解決 SAT 問題（Boolean Satisfiability Problem，布林可滿足性問題），最直觀且系統化的方法就是窮舉真值表（Truth Table Enumeration）。也就是列出所有變數可能為真（True）或假（False）的組合，逐一帶入檢查是否有任何一組能讓整個布林公式成立（為 True）。
# SAT 之真值表法
姓名：許尹榛
學號：111310561
這題我用 Gemini 幫忙寫，程式在 [sat.py](sat.py)。
## 做法
SAT（Boolean Satisfiability Problem）旨在尋找一組布林變數值，使整個邏輯式等於 1。
本實作採用真值表法，遍歷所有變數的所有可能組合（2 n），逐一帶入驗證，找出所有能使式子成立的賦值組合。
## 執行結果
```
[ 求解結果 ]
➤ 此 SAT 問題是可滿足的 (Satisfiable, SAT)
➤ 找到以下可滿足的變數指定解 (Satisfying Assignments):
  解 1: { A = False, B = True, C = False }
  解 2: { A = True, B = False, C = False }
  解 3: { A = True, B = True, C = False }
```
## 心得
暴力法簡單，但具指數級瓶頸，故需仰賴更高效的 SAT 演算法。
