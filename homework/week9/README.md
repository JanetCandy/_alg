# 經典搜尋法實作專案 (Python & VS Code)

本專案使用 Python 實作了五大經典AI與圖論搜尋問題，展示深度優先搜尋 (DFS)、廣度優先搜尋 (BFS)、啟發式搜尋 (A*) 以及晶片實體設計中的繞線演算法。

---

## 包含問題與演算法對照

| 編號 | 問題名稱 | 核心演算法 | 應用場景說明 |
| :--- | :--- | :--- | :--- |
| **1** | 老鼠走迷宮 | **DFS** (深度優先搜尋) | 用於探索所有可能的單一路徑，直到找到出口。 |
| **2** | 狼羊甘藍菜過河 | **BFS** (廣度優先搜尋) | 用於尋找狀態空間中的「最短過河步驟序列」。 |
| **3** | 八皇后問題 | **DFS + Backtracking** | 用於約束滿足問題（CSP），透過回溯剪枝找出所有合法排法。 |
| **4** | NPC 搜尋玩家 | **A\* Search** | 遊戲 AI 中兼顧效能與精確度的最短路徑尋找（結合曼哈頓距離）。 |
| **5** | IC 設計電路繞線 | **Lee's Algorithm (BFS 變體)** | 晶片實體設計 (Physical Design) 中確保金屬線不相交的繞線法。 |

---

## 環境需求與執行方式

1. **環境需求**：
   * Python 3.10 或以上版本
   * Visual Studio Code

2. **在 VS Code 中執行**：
   * 開啟 VS Code，並將此專案資料夾加入工作區。
   * 開啟任一 Python 檔案（例如 `maze_dfs.py`）。
   * 點擊右上角的 **Play (Run Python File)** 按鈕，或在終端機 (Terminal) 中執行：
     ```bash
     python maze_dfs.py
     python river_bfs.py
     python eight_queens.py
     python npc_astar.py
     python circuit_routing.py
     ```