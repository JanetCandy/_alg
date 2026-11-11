# circuit_routing.py
from collections import deque

def lees_algorithm(grid, start, target):
    """IC 設計中的迷宮繞線演算法 (Lee's Algorithm / BFS 變體)"""
    rows, cols = len(grid), len(grid[0])
    
    # 1. 波動傳播階段 (Wave Propagation)
    queue = deque([start])
    distance_grid = [[-1 for _ in range(cols)] for _ in range(rows)]
    distance_grid[start[0]][start[1]] = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    reached = False
    
    while queue:
        r, c = queue.popleft()
        if (r, c) == target:
            reached = True
            break
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                # 0 代表可繞線空間，或者到達目標點
                if grid[nr][nc] == 0 and distance_grid[nr][nc] == -1:
                    distance_grid[nr][nc] = distance_grid[r][c] + 1
                    queue.append((nr, nc))
                    
    if not reached:
        return None # 無法繞線
        
    # 2. 回溯階段 (Backtracking)
    path = [target]
    curr = target
    while curr != start:
        r, c = curr
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if distance_grid[nr][nc] == distance_grid[r][c] - 1:
                    curr = (nr, nc)
                    path.append(curr)
                    break
    path.reverse()
    return path

if __name__ == "__main__":
    # 0 代表通道，1 代表障礙物或已有佈線
    ic_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start_pin = (0, 0)
    target_pin = (4, 4)
    
    routing_path = lees_algorithm(ic_grid, start_pin, target_pin)
    print("=== 5. IC 電路繞線 (Lee's Algorithm / BFS) ===")
    print("最佳繞線金屬路徑座標:", routing_path)