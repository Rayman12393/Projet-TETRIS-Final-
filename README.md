# Projet TETRIS Final 

## Le jeu choisi est un tetris en py.
La partie commence dès que la première pièce apparaît en haut de la grille. 
L'objectif est simple : empiler les pièces pour former des lignes complètes.
Chaque ligne complétée disparaît permettant de rapporter des points. Plus on enchaîne
des lignes, plus le niveau augmente et plus les pièces tombent vite.
## Comment cela va se passé ?
Une pièce 3×3 apparaît au centre, en haut de la grille 10×10.
Elle descend à intervalles réguliers. On peut la déplacer et la faire pivoter pour l’emboîter au mieux.
Quand une pièce ne peut plus descendre, elle se fige. Toute ligne entièrement remplie est effacée.
La partie se termine si une nouvelle pièce ne peut pas apparaître.
## Commande à utiliser 
Flèches gauche/droite: déplacer la pièce
Flèche bas: descendre d’un cran
Flèche haut: pivoter (90°)
p: pause / reprise
q: quitter
## Bon à retenir 
Score: plus vous effacez de lignes d’un coup, plus le bonus est élevé.
Niveaux: la vitesse augmente tous les X lignes effacées.
Stratégie: anticipez 1–2 coups à l’avance et utilisez le hold pour vous sauver.
