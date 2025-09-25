"""
Tetris Console - Version Python
Jeu de Tetris jouable en console avec des pièces 3x3 sur une grille 10x10.
"""
import time
from functions import TetrisGame, print_game, get_input, handle_input
def main():
    """Fonction principale du jeu"""
    print("Bienvenue dans Tetris Console!")
    print("Appuyez sur une touche pour commencer...")
    input()
    game = TetrisGame()
    last_time = time.time()
