from collections import deque
import time
import sys
from Player import Player
class Admin(Player):
    """
    Docstring for Admin
    
    Admin is a special type of Player with enhanced attributes and abilities.
    Attributes:
    - name (str): The name of the admin player.
    Methods:
    - end_game() -> None: Ends the game and exits the program.
    
    """
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.level = 2**32
        self.hp *= 2**10
        self.mp *= 2**10
        self.dmg *= 2**10
        self.dex *= 2**10
        self.luck /= (2**10)
        self.inventory.append("Admin Powers Token")
        self.inventory = deque(self.inventory, maxlen=10**6)

    def end_game(self) -> None:
        print("You have chosen to end the game.")
        time.sleep(2)
        print("Thank you for playing!")
        time.sleep(2)
        sys.exit()

