def hanoi_recursive(n, src='A', aux='B', dst='C'):
    if n == 1:
        print(f"Move disk 1 from {src} to {dst}")
        return
    # 1. 將上面 n-1 個盤子從 src 移到 aux
    hanoi_recursive(n - 1, src, dst, aux)
    # 2. 將第 n 個盤子從 src 移到 dst
    print(f"Move disk {n} from {src} to {dst}")
    # 3. 將 n-1 個盤子從 aux 移到 dst
    hanoi_recursive(n - 1, aux, src, dst)

# 測試
print("=== 河內塔（遞迴） ===")
hanoi_recursive(3)def hanoi_recursive(n, src='A', aux='B', dst='C'):
    if n == 1:
        print(f"Move disk 1 from {src} to {dst}")
        return
    # 1. 將上面 n-1 個盤子從 src 移到 aux
    hanoi_recursive(n - 1, src, dst, aux)
    # 2. 將第 n 個盤子從 src 移到 dst
    print(f"Move disk {n} from {src} to {dst}")
    # 3. 將 n-1 個盤子從 aux 移到 dst
    hanoi_recursive(n - 1, aux, src, dst)

# 測試
print("=== 河內塔（遞迴） ===")
hanoi_recursive(3)