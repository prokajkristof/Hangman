import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list

lives = 6
stages = hangman_art.stages

print(hangman_art.logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

correct_letters = []

display = "_" * len(chosen_word)
guessed_letters = []

while lives != 0 and chosen_word != display:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed this letter!")
    else:
        guessed_letters.append(guess)

        if guess in chosen_word:
            print("Right!")
            for i in range(0, len(chosen_word)):
                if chosen_word[i] == guess:
                    display = display[:i] + guess + display[i + 1:]
        else:
            print(f"You guessed {guess} that is not in the word, you lost a life!")
            lives -= 1
        print(display)
    print(stages[lives])

if display == chosen_word:
    print("****************************YOU WIN****************************")
else:
    print(f"***********************YOU LOSE! The word was {chosen_word} **********************")

