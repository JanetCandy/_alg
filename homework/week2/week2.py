import math

# ==========================================
# 題目 1: T(n) = T(n-1) + 8, T(1) = 1
# ==========================================


def T1_recursive(n):
  if n == 1:
    return 1
  return T1_recursive(n - 1) + 8


def T1_formula(n):
  return 8 * n - 7


# ==========================================
# 題目 2: T(n) = 2*T(n-1) + 9, T(1) = 1
# ==========================================


def T2_recursive(n):
  if n == 1:
    return 1
  return 2 * T2_recursive(n - 1) + 9


def T2_formula(n):
  return 5 * (2**n) - 9


# ==========================================
# 題目 3: T(n) = 2*T(n//2) + 1, T(1) = 1
# ==========================================


def T3_recursive(n):
  if n == 1:
    return 1
  return 2 * T3_recursive(n // 2) + 1


def T3_formula(n):
  return 2 * n - 1


# ==========================================
# 題目 4: T(n) = T(n//2) + 1, T(1) = 1
# ==========================================


def T4_recursive(n):
  if n == 1:
    return 1
  return T4_recursive(n // 2) + 1


def T4_formula(n):
  return int(math.log2(n)) + 1


# ==========================================
# 主程式測試
# ==========================================
if __name__ == "__main__":
  print("=== Homework 2: 遞迴關係式驗證 ===\n")

  # 測試 1 & 2 (n = 10)
  n_linear = 10
  print(f"[測試 n = {n_linear}]")
  print(
      f"1. T1({n_linear}) -> 遞迴: {T1_recursive(n_linear)}, 公式:"
      f" {T1_formula(n_linear)}"
  )
  print(
      f"2. T2({n_linear}) -> 遞迴: {T2_recursive(n_linear)}, 公式:"
      f" {T2_formula(n_linear)}\n"
  )

  # 測試 3 & 4 (n = 16，取 2 的次方方便驗證)
  n_power2 = 16
  print(f"[測試 n = {n_power2}]")
  print(
      f"3. T3({n_power2}) -> 遞迴: {T3_recursive(n_power2)}, 公式:"
      f" {T3_formula(n_power2)}"
  )
  print(
      f"4. T4({n_power2}) -> 遞迴: {T4_recursive(n_power2)}, 公式:"
      f" {T4_formula(n_power2)}"
  )