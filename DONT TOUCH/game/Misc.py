import random
from Player import Player
from World_Gen import Generate_World as World


class Mischellaneous:
    """This class is intended for mischellaneous functions that don't fit anywhere else."""

    def __init__(self, player: Player, world: World) -> None:
        self.player = player
        self.world = world
    def minigame_1(self) -> None:
        """A simple minigame where the player has to guess a number between 1 and 10."""
        import random
        random.seed(1)
        number_to_guess = random.randint(1, 10)
        attempts = 3
        print("Welcome to the Guessing Game!")
        print("You have to guess a number between 1 and 10.")
        print(f"You have {attempts} attempts.")
        while attempts > 0:
            guess = input("Enter your guess: ")
            try:
                guess = int(guess)
            except ValueError:
                print("Please enter a valid number.")
                continue
            if guess < 1 or guess > 10:
                print("Your guess is out of range. Please guess between 1 and 10.")
                continue
            if guess == number_to_guess:
                print("Congratulations! You've guessed the correct number!")
                self.player.gain_exp(10)
                self.player.lvl_up()
                self.player.add_to_inventory("Small Reward")
        
                return
            elif guess < number_to_guess:
                attempts -= 1
                print(f"Too low! You have {attempts} attempts left.")
            elif guess > number_to_guess:
                attempts -= 1
                print(f"Too high! You have {attempts} attempts left.")
            else:
                attempts -= 1
                print(f"Wrong guess! You have {attempts} attempts left.")
        print(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}.")
    def minigame_2(self) -> None:
        """ A simple minigame where the player has to crack a ceaser cipher."""
        key = random.randint(1, 25)
        msg = random.choice(["HELLO", "WORLD", "PYTHON", "GAME", "DONTTOUCH"])
        cipher_text = ''.join(
            chr((ord(char) - 65 + key) % 26 + 65) for char in msg)
        print("Welcome to the Ceaser Cipher Cracking Game!")
        print("You have to crack the following cipher text:")
        print(cipher_text)
        attempts = 3
        rr = 0
        while attempts > 0:
            guess = input("Enter your guess for the original message: ").upper()
            if guess == msg:
                print("Congratulations! You've cracked the cipher!")
                self.player.gain_exp(15)
                self.player.lvl_up()
                self.player.add_to_inventory("Cipher Cracker Badge")
        
                return
            else:
                attempts -= 1
                rr += 2
                r = random.randint(5-rr,10-rr)
                print(f"Wrong guess! You have {attempts} attempts left.")
                print(f"The key is higher than {key-r} and lesser than {key+r}.")
    def minigame_3(self) -> None:
        """A simple minigame where the player has to solve a few equations."""

Mischellaneous(Player("Test"), World(12)).minigame_3()