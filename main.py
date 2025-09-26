"""
Tetris Console - Version Python
Jeu de Tetris jouable en console avec des pièces 3x3 sur une grille 10x10.
"""
import time
from function import Tetris, get_key  
def main():
    """Fonction principale du jeu"""
    print("Bienvenue dans Tetris Console!")
    print("Appuyez sur une touche pour commencer...")
    
    game = Tetris()

    while game.running and not game.game_over:
        game.draw()  

        key = get_key()
        if key:
            if key in ['Q', 'A']:
                game.move_left()
            elif key == 'D':
                game.move_right()
            elif key == 'S':
                game.move_down()
            elif key == 'Z':
                game.rotate()
            elif key == 'X':
                game.running = False
                break

        time.sleep(0.05)

    game.draw()
    print("Score final:", game.score)
    print("Merci d'avoir joué!") 
   
if __name__ == "__main__":
    main()
