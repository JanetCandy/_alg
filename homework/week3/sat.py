import itertools

def solve_sat_by_enumeration(variables, formula_func):
    """
    使用真值表窮舉法解決 SAT 問題
    :param variables: 變數名稱清單，例如 ['A', 'B', 'C']
    :param formula_func: 接收一個字典（變數對應真假值）並回傳布林結果的函數
    """
    n = len(variables)
    satisfiable = False
    satisfying_assignments = []

    print(f"=== 系統化真值表 (變數: {variables}) ===")
    
    # 建立表頭
    header = " | ".join([f"{v:^5}" for v in variables]) + " | 運算結果"
    print(header)
    print("-" * len(header))

    # 利用 itertools.product 產生 2^n 種 True/False 組合
    for values in itertools.product([False, True], repeat=n):
        # 將變數與值對應結合成字典
        assignment = dict(zip(variables, values))
        
        # 帶入公式計算結果
        result = formula_func(assignment)
        
        # 格式化輸出真值表的一行 (T 代表 True, F 代表 False)
        row_str = " | ".join([f"{('T' if assignment[v] else 'F'):^5}" for v in variables])
        row_str += f" | {'T' if result else 'F'}"
        print(row_str)

        # 記錄滿足條件的解
        if result:
            satisfiable = True
            satisfying_assignments.append(assignment)

    print("-" * len(header))
    print("\n[ 求解結果 ]")
    if satisfiable:
        print("➤ 此 SAT 問題是可滿足的 (Satisfiable, SAT)")
        print("➤ 找到以下可滿足的變數指定解 (Satisfying Assignments):")
        for idx, sol in enumerate(satisfying_assignments, 1):
            formatted_sol = ", ".join([f"{k} = {v}" for k, v in sol.items()])
            print(f"  解 {idx}: {{ {formatted_sol} }}")
    else:
        print("➤ 此 SAT 問題是不可滿足的 (Unsatisfiable, UNSAT)")

# ==========================================
# 測試範例：求解公式 (A or B) and (not C)
# ==========================================
if __name__ == "__main__":
    # 1. 定義變數
    vars_list = ['A', 'B', 'C']
    
    # 2. 定義布林表達式 (對應邏輯：(A ∨ B) ∧ ¬C)
    # 使用 lambda 函式接收字典 v
    formula = lambda v: (v['A'] or v['B']) and (not v['C'])
    
    # 3. 執行求解
    solve_sat_by_enumeration(vars_list, formula)