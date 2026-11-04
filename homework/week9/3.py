# eight_queens.py

def solve_queens(n=8):
    """使用回溯法 (DFS) 求解八皇后問題"""
    solutions = []
    
    def backtrack(row, current_placement):
        if row == n:
            solutions.append(current_placement)
            return
        
        for col in range(n):
            # 檢查與之前放置的皇后是否衝突（同列、同對角線）
            conflict = False
            for r, c in enumerate(current_placement):
                if c == col or abs(r - row) == abs(c - col):
                    conflict = True
                    break
            if not conflict:
                backtrack(row + 1, current_placement + [col])

    backtrack(0, [])
    return solutions

if __name__ == "__main__":
    print("=== 3. 八皇后問題 (DFS) ===")
    results = solve_queens(8)
    print(f"總共有 {len(results)} 組解法。")
    print("第一組解法的棋盤表示 (Q: 皇后, .: 空格):")
    for r in results[0]:
        row_str = "".join("Q" if c == r else "." for c in range(8))
        print(row_str)