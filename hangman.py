import random
import stages
word = ["python", "tiger", "college", "program", "iphone"]
lifes = 6
chosen_word = random.choice(word)
print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display += "_"
print(display)
game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    if guess not in chosen_word:
        lifes -= 1
        print("Lives left:", lifes)
    if lifes == 0:
            game_over = True
            print("You Lose!!")
    if "_" not in display:
        game_over = True
        print("You won!")
    print(display)
    print(stages.stages[lifes])