# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:25:50 2024

@author: widia
"""

from collections import deque
import matplotlib.pyplot as plt

def visualize_path(grid, path):
    # Buat array untuk visualisasi
    vis_grid = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for x, y in path:
        vis_grid[x][y] = 2  # Tandai jalur dengan nilai 2
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                vis_grid[i][j] = 0  # Tandai dinding dengan nilai 1

    # Plot grid
    plt.imshow(vis_grid, cmap='gray')
    plt.show()

def bfs(grid, start, end):
  rows, cols = len(grid), len(grid[0])
  visited = set()
  parent = {}  # Dictionary untuk menyimpan parent
  queue = deque([(start[0], start[1])])
  visited.add((start[0], start[1]))

  while queue:
    row, col = queue.popleft()
    if (row, col) == end:
      # Construct the path
      path = []
      while (row, col) != start:
        path.append((row, col))
        row, col = parent[(row, col)]
      path.append(start)
      path.reverse()
      return path, len(path) - 1  # Mengembalikan jalur dan jumlah langkah

    # Cek tetangga (atas, bawah, kiri, kanan)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      r, c = row + dr, col + dc
      if 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#' and (r, c) not in visited:
        queue.append((r, c))
        visited.add((r, c))
        parent[(r, c)] = (row, col)

  return None, 0  # Jika tidak ada jalur

# Contoh penggunaan
grid = [
    ["1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"#" ,"#" ],
    ["#" ,"10","#" ,"#" ,"#" ,"14","15","16"],
    ["17","18","19","20","21","#" ,"#" ,"24"],
    ["25","#" ,"27","#" ,"29","#" ,"31","32"],
    ["33","#" ,"35","36","#" ,"#" ,"39","#" ],
    ["41","42","#" ,"44","#" ,"46","47","48"],
    ["#" ,"50","#" ,"52","53","#" ,"#" ,"56"],
    ["57","58","59","#" ,"61","62","63","64"],
]

start = (0, 0)  # Asumsi titik merah ada di baris 0, kolom 0
end = (7, 7)    # Asumsi titik hijau ada di baris 7, kolom 7
path, steps = bfs(grid, start, end)

if path:
  print("Jalur ditemukan:")
  for x, y in path:
    print(f"({x}, {y})")
  print(f"Jumlah langkah: {steps}")
  visualize_path(grid, path)
else:
  print("Tidak ada jalur")