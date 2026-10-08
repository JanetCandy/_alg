def hanoi_iterative(n, src='A', aux='B', dst='C'):
    # 堆疊項目：(盤子數量, 起始柱, 中介柱, 目標柱)
    stack = [(n, src, aux, dst)]

    while stack:
        num, s, a, d = stack.pop()

        if num == 1:
            print(f"Move disk 1 from {s} to {d}")
        else:
            # 依後進先出 (LIFO) 壓入 Stack：
            # 步驟3：將 n-1 個盤子從 aux 經由 s 移到 d
            # 步驟2：將第 n 個盤子從 s 移到 d
            # 步驟1：將 n-1 個盤子從 s 經由 d 移到 a
            stack.append((num - 1, a, s, d))
            stack.append((1, s, a, d))
            stack.append((num - 1, s, d, a))

# 測試
print("\n=== 河內塔（非遞迴/Stack模擬） ===")
hanoi_iterative(3)