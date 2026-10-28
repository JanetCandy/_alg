import time

# ==========================================
# 1. 動態規劃法 (Dynamic Programming)
# ==========================================
def combination_dp(n: int, k: int) -> int:
    """
    使用由下而上 (Bottom-Up) 的動態規劃計算組合數 C(n, k)
    時間複雜度: O(n * k)
    空間複雜度: O(n * k)
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    # 建立 (n+1) x (k+1) 的 DP 表格，初始化為 0
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # 填表
    for i in range(n + 1):
        dp[i][0] = 1  # 任何數取 0 個的方法數為 1
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            
    return dp[n][k]


# ==========================================
# 2. 純遞迴法 (Pure Recursion / 非動態規劃)
# ==========================================
def combination_recursion(n: int, k: int) -> int:
    """
    使用純遞迴（巴斯卡恆等式）計算組合數 C(n, k)
    時間複雜度: O(2^n)
    空間複雜度: O(n) (遞迴呼叫堆疊)
    """
    # 邊界條件
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    # 遞迴展開：C(n, k) = C(n-1, k-1) + C(n-1, k)
    return combination_recursion(n - 1, k - 1) + combination_recursion(n - 1, k)


# ==========================================
# 測試與效能驗證
# ==========================================
if __name__ == "__main__":
    print("=" * 45)
    print(" 組合數 C(n, k) 計算問題：DP v.s. 遞迴 ")
    print("=" * 45)
    
    # 測試 1：小數值
    n1, k1 = 5, 2
    print(f"\n[測試 1] C({n1}, {k1})")
    print(f"動態規劃結果: {combination_dp(n1, k1)}")
    print(f"純遞迴結果:   {combination_recursion(n1, k1)}")
    
    # 測試 2：中等數值
    n2, k2 = 20, 10
    print(f"\n[測試 2] C({n2}, {k2})")
    
    start_time = time.time()
    res_dp = combination_dp(n2, k2)
    time_dp = time.time() - start_time
    print(f"動態規劃結果: {res_dp} (耗時: {time_dp:.6f} 秒)")
    
    start_time = time.time()
    res_rec = combination_recursion(n2, k2)
    time_rec = time.time() - start_time
    print(f"純遞迴結果:   {res_rec} (耗時: {time_rec:.6f} 秒)")
    
    print("\n" + "=" * 45)