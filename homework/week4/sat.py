"""
題目：使用牛頓迭代法 (Newton-Raphson Method) 求解實數的立方根 (Cube Root)
數學原理：
求解方程式 f(x) = x^3 - a = 0 的根。
牛頓法迭代公式：
  x_{n+1} = x_n - f(x_n) / f'(x_n)
          = x_n - (x_n^3 - a) / (3 * x_n^2)
          = (2 * x_n + a / (x_n^2)) / 3
"""

import math

def solve_cube_root(a, x0=1.0, max_iter=1000, tol=1e-7, verbose=True):
    """
    使用牛頓迭代法計算 a 的立方根 (cbrt(a))
    參數:
      a (float): 欲求解立方根的目標數值
      x0 (float): 初始猜測值，預設為 1.0
      max_iter (int): 最大迭代次數限制，預設為 1000
      tol (float): 容許誤差 (Tolerance)，預設為 1e-7
      verbose (bool): 是否印出每一代的詳細過程，預設為 True
    回傳:
      float: 立方根的近似解
      int: 總共使用的迭代次數
    """
    if a == 0:
        return 0.0, 0

    x = x0
    if verbose:
        print(f"=== 開始迭代求解 cbrt({a}) ===")
        print(f"初始猜測值 x0 = {x0:.6f}, 容許誤差 tol = {tol}\n")
        print(f"{'第幾代 (k)':<10}{'目前估計值 x_k':<20}{'單步變化量 |x_k - x_{k-1}|':<25}")
        print("-" * 55)

    for k in range(1, max_iter + 1):
        x_next = (2.0 * x + a / (x ** 2)) / 3.0
        
        diff = abs(x_next - x)

        if verbose:
            print(f"{k:<10}{x_next:<20.8f}{diff:<25.8e}")

        if diff < tol:
            if verbose:
                print("-" * 55)
                print(f"恭喜！演算法在第 {k} 次迭代時成功收斂。\n")
            return x_next, k

        x = x_next

    if verbose:
        print("-" * 55)
        print(f"警告：達到最大迭代次數 ({max_iter})，可能尚未完全收斂！\n")
    return x, max_iter



if __name__ == "__main__":
    target_val = 64.0
    ans, steps = solve_cube_root(a=target_val, x0=2.0, tol=1e-8, verbose=True)

    expected = math.pow(target_val, 1/3)
    print("【驗證結果】")
    print(f"迭代求解結果 : {ans:.8f}")
    print(f"標準庫計算結果: {expected:.8f}")
    print(f"絕對誤差值   : {abs(ans - expected):.8e}")
    print(f"總共迭代次數 : {steps} 次")

    print("\n" + "=" * 55 + "\n")

    target_val_2 = 0.125
    ans2, steps2 = solve_cube_root(a=target_val_2, x0=1.0, tol=1e-8, verbose=False)
    print(f"測試案例 2: 求 cbrt({target_val_2})")
    print(f"求解結果: {ans2:.8f} (共耗時 {steps2} 次迭代)")