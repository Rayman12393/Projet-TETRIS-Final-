import random
import time
import os
import sys
import threading
try:
    import msvcrt
    WINDOWS = True
except ImportError:
    import termios
    import tty
    WINDOWS = False
GRID_WIDTH = 10
GRID_HEIGHT = 20
PIECES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]   # Z
]
class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.piece = random.choice(PIECES)
        self.piece_x = GRID_WIDTH // 2 - len(self.piece[0]) // 2
        self.piece_y = 0
        self.score = 0
        self.game_over = False
        self.running = True
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def draw(self):
        self.clear_screen()
        display_grid = [row[:] for row in self.grid]
        for y, row in enumerate(self.piece):
            for x, cell in enumerate(row):
                if cell and 0 <= self.piece_y + y < GRID_HEIGHT and 0 <= self.piece_x + x < GRID_WIDTH:
                    display_grid[self.piece_y + y][self.piece_x + x] = cell
        print(" TETRIS - Score:", self.score, "")
        print("+" + "━" * (GRID_WIDTH * 2) + "+")
        for row in display_grid:
            line = "┃"
            for cell in row:
                if cell:
                    line += "██"  # Bloc plein
                else:
                    line += "  "  # Vide
            line += "┃"
            print(line)
        print("+" + "━" * (GRID_WIDTH * 2) + "+")
        print(" A/Q: ←  D: →  S: ↓  Z:  X: Quit")
        if self.game_over:
            print("\n GAME OVER ")
