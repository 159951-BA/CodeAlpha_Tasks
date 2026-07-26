import random

words = ["python", "hangman", "intern", "codealpha", "bilal"]
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("=== HANGMAN GAME ===")
print("Guess the word one letter at a time.")
print("You have 6 wrong guesses allowed.")
print("The word has", len(word), "letters.")

while wrong_guesses < max_wrong:
    print()
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

    print("Wrong guesses:", wrong_guesses, "/", max_wrong)
    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        wrong_guesses = wrong_guesses + 1

    # Check if user won
    won = True
    for letter in word:
        if letter not in guessed_letters:
            won = False
            break

    if won:
        print()
        print("You won! The word was:", word)
        break

if wrong_guesses == max_wrong:
    print()
    print("Game over! The word was:", word)