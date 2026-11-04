# river_bfs.py
from collections import deque

def is_valid(state):
    """檢查狀態是否安全：無農夫在場時，狼不能與羊單獨在一起，羊不能與甘藍菜單獨在一起"""
    f, w, g, c = state
    if w == g and f != w: return False
    if g == c and f != g: return False
    return True

def bfs_river_crossing():
    """使用廣度優先搜尋尋找過河的最短步驟"""
    initial_state = (0, 0, 0, 0) # (農夫, 狼, 羊, 甘藍菜) 0:左岸, 1:右岸
    target_state = (1, 1, 1, 1)
    
    queue = deque([(initial_state, [])])
    visited = set([initial_state])
    
    # 農夫每次可單獨過河，或帶一樣物品過河
    moves = [
        ("農夫自己過河", (1, 0, 0, 0)),
        ("農夫帶狼過河", (1, 1, 0, 0)),
        ("農夫帶羊過河", (1, 0, 1, 0)),
        ("農夫帶甘藍菜過河", (1, 0, 0, 1))
    ]
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == target_state:
            return path
        
        f, w, g, c = current_state
        for action, (df, dw, dg, dc) in moves:
            # 依農夫當前位置決定是過去(加)還是回來(減)
            if f == 0:
                next_state = (f+df, w+dw, g+dg, c+dc)
            else:
                next_state = (f-df, w-dw, g-dg, c-dc)
                
            # 檢查邊界與安全性
            if all(0 <= val <= 1 for val in next_state):
                if is_valid(next_state) and next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, path + [(action, next_state)]))
                    
    return None

if __name__ == "__main__":
    print("=== 2. 狼羊甘藍菜過河 (BFS) ===")
    solution = bfs_river_crossing()
    if solution:
        for i, (action, state) in enumerate(solution, 1):
            print(f"步驟 {i}: {action} -> 狀態(農,狼,羊,菜): {state}")