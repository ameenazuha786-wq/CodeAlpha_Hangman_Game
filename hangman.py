import random

# List of 5 predefined words
words = ["python", "computer", "program", "coding", "software"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 6

# Display underscores for the hidden word
display_word = ["_"] * len(word)

print("Welcome to the Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

while incorrect_guesses > 0 and "_" in display_word:

    print("Word:", " ".join(display_word))
    print("Incorrect guesses remaining:", incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct guess!\n")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        incorrect_guesses -= 1
        print("Wrong guess!\n")

# Check the result
if "_" not in display_word:
    print("Congratulations! 🎉")
    print("You guessed the word:", word)
else:
    print("Game Over! 😢")
    print("The word was:", word)