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
