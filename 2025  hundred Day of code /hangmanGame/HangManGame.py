import random
from HangmanWords import hangman_words
from hangmanStages import stages

chosen_word = random.choice(hangman_words)

display = "_" * len(chosen_word)
deaths = 0
GameOver = False
lives = 6

print(display)

while not GameOver:
    guess = input("Guess a letter: ").lower()
    new_display = ""

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            new_display += guess
        else:
            new_display += display[i]

    if new_display == display:
        deaths += 1
        lives -= 1
        print(f"Wrong guess! Deaths: {deaths}")
        print(stages[lives])

    display = new_display
    print(display)
    
    if guess not in chosen_word:
        
        if lives == 0:
            GameOver == True
            print("you lose ")
    if "_" not in display:
        print("************************🎉 You win!***************************")
        GameOver = True
    elif deaths >= 6:
        print("****************************💀 Game over!********************")
        print(f"The word was: {chosen_word}")
        GameOver = True
        print(stages[lives])
