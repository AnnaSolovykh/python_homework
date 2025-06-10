"""
Assignment 12 - Task 4: Closure 
"""

# Task 4
def make_hangman(secret_word):
    guesses = []
    
    def hangman_closure(letter):
        guesses.append(letter.lower())
        
        display_word = ""
        for char in secret_word.lower():
            if char in guesses:
                display_word += char
            else:
                display_word += "_"
        
        print(f"Word: {display_word}")
        print(f"Guesses so far: {guesses}")
        
        for char in secret_word.lower():
            if char not in guesses:
                return False  
        
        return True  
    
    return hangman_closure


def play_hangman():
    secret_word = input("Enter the secret word: ").strip()
    
    print("HANGMAN GAME STARTED!")
    
    game = make_hangman(secret_word)
    
    while True:
        guess = input("Enter a letter: ").strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
        
        word_complete = game(guess)
        
        if word_complete:
            print("\n" + "=" * 40)
            print("🎉 CONGRATULATIONS! You guessed the word!")
            print(f"The word was: {secret_word}")
            break


if __name__ == "__main__":
    while True:
        play_hangman()
        
        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if play_again not in ['y', 'yes']:
            print("Thanks for playing!")
            break
        print("\n" + "=" * 50)