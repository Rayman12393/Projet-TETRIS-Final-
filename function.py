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
    def can_move(self, dx=0, dy=0, piece=None):
        if piece is None:
            piece = self.piece
        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.piece_x + x + dx
                    new_y = self.piece_y + y + dy
                    if (new_x < 0 or new_x >= GRID_WIDTH or 
                        new_y >= GRID_HEIGHT or 
                        (new_y >= 0 and self.grid[new_y][new_x])):
                        return False
        return True
    def move_left(self):
        if self.can_move(-1, 0):
            self.piece_x -= 1
    def move_right(self):
        if self.can_move(1, 0):
            self.piece_x += 1
    def move_down(self):
        if self.can_move(0, 1):
            self.piece_y += 1
            return True
        else:
            self.place_piece()
            return False
    def rotate(self):
        rotated = [[self.piece[len(self.piece)-1-j][i] for j in range(len(self.piece))] 
                  for i in range(len(self.piece[0]))]
        if self.can_move(0, 0, rotated):
            self.piece = rotated
    def place_piece(self):
        for y, row in enumerate(self.piece):
            for x, cell in enumerate(row):
                if cell and self.piece_y + y >= 0:
                    self.grid[self.piece_y + y][self.piece_x + x] = 1
        self.clear_lines()
        self.piece = random.choice(PIECES)
        self.piece_x = GRID_WIDTH // 2 - len(self.piece[0]) // 2
        self.piece_y = 0
        if not self.can_move():
            self.game_over = True
    def clear_lines(self):
        lines_to_clear = []
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                lines_to_clear.append(y)
        for y in sorted(lines_to_clear, reverse=True):
            del self.grid[y]
            self.grid.insert(0, [0] * GRID_WIDTH)
            self.score += 100
def get_key():
    if WINDOWS:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').upper()
            return key
    else:
        try:
            stdin_fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(stdin_fd)
            tty.setraw(stdin_fd)
            key = sys.stdin.read(1).upper()
            termios.tcsetattr(stdin_fd, termios.TCSADRAIN, old_settings)
            return key
        except:
            pass
    return None
def auto_fall(game):
    """Thread pour faire tomber les pièces automatiquement"""
    while game.running and not game.game_over:
        time.sleep(1.0)  # Attendre 1 seconde
        if game.running and not game.game_over:
            game.move_down()
def main():
    game = Tetris()
    fall_thread = threading.Thread(target=auto_fall, args=(game,), daemon=True)
    fall_thread.start()
    print(" TETRIS démarré ! Les pièces tombent automatiquement...")
    time.sleep(2)
    while game.running and not game.game_over:
        game.draw()
        key = get_key()
        if key:
            if key in ['Q', 'A']:  # Gauche
                game.move_left()
            elif key == 'D':  # Droite
                game.move_right()
            elif key == 'S':  # Bas (accélère la chute)
                game.move_down()
            elif key == 'Z':  # Tourner
                game.rotate()
            elif key == 'X':  # Quitter
                game.running = False
                break
        time.sleep(0.05)  # Petite pause pour éviter la surcharge CPU
    game.running = False
    game.draw()
    print(" Score final:", game.score)
    print("Merci d'avoir joué ! Au revoir")
if __name__ == "__main__":
    main()
