"""
Tetris Console - Version Python
Jeu de Tetris jouable en console avec des pièces 3x3 sur une grille 10x10.
"""
import time
from function import TetrisGame, print_game, get_input, handle_input
def main():
    """Fonction principale du jeu"""
    print("Bienvenue dans Tetris Console!")
    print("Appuyez sur une touche pour commencer...")
    input()
    game = TetrisGame()
    last_time = time.time()
    try:
        while True:
            current_time = time.time()
            dt = (current_time - last_time) * 1000  # Delta time en millisecondes
            last_time = current_time
            print_game(game)
            key = get_input()
            if key:
                if not handle_input(game, key):
                    break
            game.update(dt)
            time.sleep(0.05)
            if game.game_over:
                print_game(game)
                print("\nVoulez-vous rejouer ? (o/n)")
                response = input().lower()
                if response == 'o' or response == 'oui':
                    game = TetrisGame()
                    last_time = time.time()
                else:
                    break
    except KeyboardInterrupt:
        print("\n\nMerci d'avoir joué à Tetris Console!")
    except Exception as e:
        print(f"\nErreur inattendue: {e}")
        print("Le jeu va se fermer.")
    print("Au revoir!")
if __name__ == "__main__":
    main()
