import random

class HangmanGame:
    def __init__(self, word_list=None):
        if word_list is None:
            self.word_list = ['python', 'programming', 'computer', 'algorithm', 'database', 
                            'network', 'software', 'developer', 'interface', 'variable']
        else:
            self.word_list = word_list
        
        self.max_tries = 6
        self.reset_game()
    
    def reset_game(self):
        """Initialize a new game with a random word."""
        self.word = random.choice(self.word_list).lower()
        self.word_letters = set(self.word)
        self.guessed_letters = set()
        self.tries_remaining = self.max_tries
        
    def get_word_display(self):
        """Return the current state of word with guessed letters filled in."""
        return ' '.join(letter if letter in self.guessed_letters else '_' for letter in self.word)
    
    def display_hangman(self):
        """Display the hangman ASCII art based on remaining tries."""
        stages = [
            # Initial empty state
            """
            --------
            |      |
            |
            |
            |
            |
            -
            """,
            # Head
            """
            --------
            |      |
            |      O
            |
            |
            |
            -
            """,
            # Head and torso
            """
            --------
            |      |
            |      O
            |      |
            |      |
            |
            -
            """,
            # Head, torso, one arm
            """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |
            -
            """,
            # Head, torso, both arms
            """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |
            -
            """,
            # Head, torso, both arms, one leg
            """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     /
            -
            """,
            # Final state: head, torso, both arms, both legs
            """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
            """
        ]

        return stages[self.tries_remaining]
    
    def make_guess(self, letter):
        """Process a letter guess and return a message about the guess."""
        letter = letter.lower()
        
        if letter in self.guessed_letters:
            return "You already guessed that letter!"
            
        self.guessed_letters.add(letter)
        
        if letter in self.word_letters:
            if self.word_letters <= self.guessed_letters:
                return "WIN"
            return "Good guess!"
        else:
            self.tries_remaining -= 1
            if self.tries_remaining == 0:
                return "LOSE"
            return f"Wrong guess! {self.tries_remaining} tries remaining."

def play_hangman():
    """Main game loop function."""
    game = HangmanGame()
    
    print("\nWELCOME TO HANGMAN")
    print(f"You have {game.max_tries} tries to guess the word.")
    
    while True:
        print("\n" + game.display_hangman())
        print("\nWord:", game.get_word_display())
        print("Guessed letters:", ' '.join(sorted(game.guessed_letters)) or "None")
        
        guess = input("\nGuess a letter: ").strip()
        
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter!")
            continue
            
        result = game.make_guess(guess)
        
        if result == "WIN":
            print("\nCongratulations! You won!")
            print(f"The word was: {game.word}")
            break
        elif result == "LOSE":
            print("\n" + game.display_hangman())
            print("Sorry, you lost!")
            print(f"The word was: {game.word}")
            break
        else:
            print(result)

if __name__ == "__main__":
    play_hangman()