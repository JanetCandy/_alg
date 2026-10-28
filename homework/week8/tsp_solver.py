import math
import random
import matplotlib.pyplot as plt


class TSPSolver:

  def __init__(self, cities):
    """cities: 城市座標列表 [(x1, y1), (x2, y2), ...]"""
    self.cities = cities
    self.num_cities = len(cities)

  def _calculate_distance(self, route):
    """計算整條路徑的總距離"""
    total_distance = 0
    for i in range(self.num_cities):
      c1 = self.cities[route[i]]
      c2 = self.cities[route[(i + 1) % self.num_cities]]  # 最後一個點連回起點
      total_distance += math.hypot(c1[0] - c2[0], c1[1] - c2[1])
    return total_distance

  # 1. 貪婪演算法 (Nearest Neighbor)
  def greedy_algorithm(self, start_node=0):
    unvisited = set(range(self.num_cities))
    current = start_node
    unvisited.remove(current)
    route = [current]

    while unvisited:
      next_city = min(
          unvisited,
          key=lambda city: math.hypot(
              self.cities[current][0] - self.cities[city][0],
              self.cities[current][1] - self.cities[city][1],
          ),
      )
      route.append(next_city)
      unvisited.remove(next_city)
      current = next_city

    return route, self._calculate_distance(route)

  # 2. 改良法 (2-opt Improvement)
  def two_opt(self, route):
    best_route = list(route)
    best_distance = self._calculate_distance(best_route)
    improved = True

    while improved:
      improved = False
      for i in range(1, self.num_cities - 1):
        for j in range(i + 1, self.num_cities):
          # 翻轉 i 到 j 之間的城市順序
          new_route = (
              best_route[:i] + best_route[i : j + 1][::-1] + best_route[j + 1 :]
          )
          new_distance = self._calculate_distance(new_route)
          if new_distance < best_distance:
            best_route = new_route
            best_distance = new_distance
            improved = True
            break
        if improved:
          break

    return best_route, best_distance

  # 3. 模擬退火法 (Simulated Annealing)
  def simulated_annealing(
      self, initial_route, temp=1000.0, cooling_rate=0.995, stopping_temp=1e-8
  ):
    current_route = list(initial_route)
    current_distance = self._calculate_distance(current_route)
    best_route = list(current_route)
    best_distance = current_distance

    while temp > stopping_temp:
      # 隨機選擇兩個點進行交換 (產生鄰居解)
      i, j = sorted(random.sample(range(self.num_cities), 2))
      new_route = (
          current_route[:i] + current_route[i : j + 1][::-1] + current_route[j + 1 :]
      )
      new_distance = self._calculate_distance(new_route)

      # 決定是否接受新解
      delta = new_distance - current_distance
      if delta < 0 or random.random() < math.exp(-delta / temp):
        current_route = new_route
        current_distance = new_distance

        if current_distance < best_distance:
          best_route = list(current_route)
          best_distance = current_distance

      temp *= cooling_rate

    return best_route, best_distance

  # 繪製路徑圖
  def plot_route(self, route, title):
    x = [self.cities[i][0] for i in route] + [self.cities[route[0]][0]]
    y = [self.cities[i][1] for i in route] + [self.cities[route[0]][1]]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'o-', linewidth=2, markersize=8, color='b')
    for i, city in enumerate(self.cities):
      plt.text(
          city[0] + 1, city[1] + 1, str(i), fontsize=12, fontweight='bold'
      )
    plt.title(title, fontsize=14)
    plt.xlabel('X 座標')
    plt.ylabel('Y 座標')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
  # 隨機生成 20 個城市的座標
  random.seed(42)
  cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(20)]

  solver = TSPSolver(cities)

  print('--- 旅行推銷員問題 (TSP) 求解器 ---')

  # 1. 貪婪演算法
  g_route, g_dist = solver.greedy_algorithm()
  print(f'貪婪演算法總距離: {g_dist:.2f}')

  # 2. 改良法 (以貪婪解作為初始解進行 2-opt)
  t_route, t_dist = solver.two_opt(g_route)
  print(f'2-opt 改良法總距離: {t_dist:.2f}')

  # 3. 模擬退火法
  sa_route, sa_dist = solver.simulated_annealing(g_route)
  print(f'模擬退火法總距離: {sa_dist:.2f}')

  # 顯示模擬退火法的最終路徑圖
  solver.plot_route(sa_route, f'TSP Simulated Annealing (Distance: {sa_dist:.2f})')