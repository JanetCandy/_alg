# Traveling Salesperson Problem (TSP) Solver in Python

本專案使用 Python 實作了解決**旅行推銷員問題 (TSP)** 的多種經典啟發式演算法，包含貪婪演算法、2-opt 改良法以及模擬退火法，並提供視覺化圖表展示。

## 專案功能特色
- **貪婪演算法 (Nearest Neighbor)**：快速生成初始路徑。
- **2-opt 改良法 (Improvement Heuristic)**：消除路徑交叉，有效優化初始解。
- **模擬退火法 (Simulated Annealing)**：具備全域搜尋能力，跳出區域最佳解。
- **資料視覺化**：透過 `matplotlib` 繪製城市與最佳化後的行進路線。

---

## 環境需求與安裝

請確保您的電腦已安裝 **Python 3.x**。您需要安裝繪圖套件 `matplotlib`：

```bash
pip install matplotlib