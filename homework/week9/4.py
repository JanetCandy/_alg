# npc_astar.py
import heapq

def heuristic(a, b):
    """曼哈頓距離啟發函數"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    """A* 演算法尋找 NPC 移動路徑"""
    rows, cols = len(grid), len(grid[0])
    
    # 優先佇列存放: (f_score, g_score, current_pos, path)
    pq = [(0, 0, start, [start])]
    visited = set()
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while pq:
        f, g, current, path = heapq.heappop(pq)
        
        if current == goal:
            return path
            
        if current in visited:
            continue
        visited.add(current)
        
        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic(neighbor, goal)
                    heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
                    
    return None

if __name__ == "__main__":
    # 0 代表可通行，1 代表障礙物
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    npc_pos = (0, 0)
    player_pos = (4, 4)
    
    path = a_star_search(grid, npc_pos, player_pos)
    print("=== 4. NPC 搜尋玩家 (A*) ===")
    print("NPC 移動路徑:", path)