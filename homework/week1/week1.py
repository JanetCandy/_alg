import time

# ==========================================
# 方法 1：數學次方運算 (Direct)
# ==========================================


def power2n_method1(n):
  return 2**n


# ==========================================
# 方法 2a：用遞迴 (Repeated addition style)
# 邏輯：2^n = 2^(n-1) + 2^(n-1)
# ==========================================


def power2n_method2a(n):
  if n == 0:
    return 1
  return power2n_method2a(n - 1) + power2n_method2a(n - 1)


# ==========================================
# 方法 2b：用遞迴 (Multiplication style)
# 邏輯：2^n = 2 * 2^(n-1)
# ==========================================


def power2n_method2b(n):
  if n == 0:
    return 1
  return 2 * power2n_method2b(n - 1)


# ==========================================
# 方法 3：用遞迴 + 查表 (Memoization)
# ==========================================
# 建立一個全域或帶有快取的字典來做查表
memo = {0: 1}


def power2n_method3(n):
  if n in memo:
    return memo[n]
  # 遞迴計算並存入表格
  memo[n] = power2n_method3(n - 1) + power2n_method3(n - 1)
  return memo[n]


# ==========================================
# 主程式：測試與效能比較
# ==========================================
if __name__ == "__main__":
  # 根據題目要求，設定測試的 n
  n = 100
  print(f"--- 測試 n = {n} 的執行結果與效能 ---\n")

  # 1. 測試方法 1
  start_time = time.perf_counter()
  res1 = power2n_method1(n)
  end_time = time.perf_counter()
  print(f"方法 1 (數學運算): 結果 = {res1}")
  print(f"耗時: {end_time - start_time:.8f} 秒\n")

  # 2. 測試方法 2b (方法 2a 算 100 會爆掉，我們後面會特別處理)
  start_time = time.perf_counter()
  res2b = power2n_method2b(n)
  end_time = time.perf_counter()
  print(f"方法 2b (純遞迴 2*f(n-1)): 結果 = {res2b}")
  print(f"耗時: {end_time - start_time:.8f} 秒\n")

  # 3. 測試方法 3 (遞迴 + 查表)
  start_time = time.perf_counter()
  res3 = power2n_method3(n)
  end_time = time.perf_counter()
  print(f"方法 3 (遞迴 + 查表): 結果 = {res3}")
  print(f"耗時: {end_time - start_time:.8f} 秒\n")

  # 4. 測試方法 2a (2^100 的呼叫次數是 2^100 次方，會直接跑不出來或 Stack Overflow)
  print("方法 2a (遞迴 f(n-1) + f(n-1)) 測試：")
  if n <= 30:  # 如果 n 很小可以試，n=100 時千萬不要直接跑，否則電腦會卡死
    start_time = time.perf_counter()
    res2a = power2n_method2a(n)
    end_time = time.perf_counter()
    print(f"結果 = {res2a}, 耗時: {end_time - start_time:.8f} 秒")
  else:
    print(
        f"  [略過測試] 當 n = {n} 時，方法 2a 的時間複雜度為 $O(2^n)$，"
        "運算次數高達 $2^{100}$ 次，"
    )
    print("  這會導致程式執行時間無限長（甚至引發 RecursionError: 超過遞迴深度限制），因此**出不來**！")