# =============================================================
# 1. 完全不使用迴圈自製的高階函數 (使用遞迴)
# =============================================================

def my_map(func, array):
    if not array:
        return []
    head, *tail = array
    return [func(head)] + my_map(func, tail)

def my_filter(func, array):
    if not array:
        return []
    head, *tail = array
    rest = my_filter(func, tail)
    return [head] + rest if func(head) else rest

def my_reduce(func, array, initial=None):
    if not array:
        if initial is None:
            raise TypeError("reduce() of empty sequence with no initial value")
        return initial
    head, *tail = array
    if initial is None:
        return my_reduce(func, tail, head)
    return my_reduce(func, tail, func(initial, head))


# =============================================================
# 2. 禁止使用迴圈的泡沫排序 (Bubble Sort)
# =============================================================

def bubble_pass(array):
    """單趟冒泡：使用自製 my_reduce 兩兩比較，將較大者往後推"""
    def step(acc, val):
        if not acc:
            return [val]
        prev = acc[-1]
        if prev > val:
            # 交換位置：取代最後一個數為 val，並將原本較大的 prev 接在後面
            return acc[:-1] + [val, prev]
        else:
            return acc + [val]

    return my_reduce(step, array, [])

def bubble_sort(array, n=None):
    """冒泡排序主函數（用遞迴代替外層迴圈）"""
    if n is None:
        n = len(array)
    if n <= 1:
        return array
    # 執行一趟沉澱後，遞迴縮減待處理的長度 n-1
    passed_array = bubble_pass(array)
    return bubble_sort(passed_array, n - 1)


# =============================================================
# 測試範例
# =============================================================
data = [64, 34, 25, 12, 22, 11, 90]

print("\n=== 自製高階函數測試 ===")
print("my_map (x * 2):", my_map(lambda x: x * 2, [1, 2, 3]))
print("my_filter (偶數):", my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print("my_reduce (總和):", my_reduce(lambda a, b: a + b, [1, 2, 3, 4], 0))

print("\n=== 無迴圈泡沫排序 ===")
print("排序前：", data)
print("排序後：", bubble_sort(data))