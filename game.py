import random
hangman_stages = [
    '''
       ------
       |    |
            |
            |
            |
            |
     ---------
    🪶
    ''',
    '''
       ------
       |    |
       O    |
            |
            |
            |
     ---------
    🪶
    ''',
    '''
       ------
       |    |
       O    |
       |    |
            |
            |
     ---------
    🪶
    ''',
    '''
       ------
       |    |
       O    |
      /|    |
            |
            |
     ---------
    🪶
    ''',
    '''
       ------
       |    |
       O    |
      /|\\   |
            |
            |
     ---------
    🪶
    ''',
    '''
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
     ---------
    🪶
    ''',
    '''
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
     ---------
    🪶
    '''
]

def display_hangman(tries):
    return hangman_stages[tries]

def hangman():
    words = ['melon', 'pomegranate', 'guava', 'apple', 'icecream', 'grapes']
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    guessed_letters = []
    tries = 0
    max_tries = 6
    print("🎉 Welcome to Hangman Game! 🎉")
    print("🎮 Try to guess the word! 🎮")
    print("💀 Each wrong guess adds a part of the hangman! 💀")
    print(display_hangman(tries))
    print(f"🧩 Word to guess: {' '.join(guessed_word)}")
    print(f"🕒 You have {max_tries} attempts left. Good luck! 🍀")
    while tries < max_tries:
        guess = input("💡 Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a valid single letter. 🔤")
            continue
        if guess in guessed_letters:
            print(f"💡 You've already guessed '{guess}'. Try a different letter. 🔄")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print(f"🎉 Nice guess! '{guess}' is in the word! 🥳")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"😞 Oops! '{guess}' is not in the word. Try again! ❌")
            tries += 1
        print(display_hangman(tries))
        print(f"🧩 Word to guess: {' '.join(guessed_word)}")
        print(f"🕒 You have {max_tries - tries} attempts left.")
        print(f"🔤 Guessed letters so far: {', '.join(guessed_letters)}")    
        if '_' not in guessed_word:
            print(f"🎉 Congratulations! You've guessed the word '{word}'! 🏆")
            break
    else:
        print(f"😢 You lost! The word was '{word}'. Better luck next time! 🍀")
        print("💔 Don't worry, keep playing!I'm sure, you would win the next game 🕹️")
hangman()
