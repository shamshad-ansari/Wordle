# Write the program that runs this game USING FUNCTIONS!
import random
def word_init():
 file = open("words.txt", "r")
 words = [word.strip() for word in file.readlines()]
 answer = random.choice(words)
 print(answer)
 return answer


def compare_guess(guess, answer):
 red = '🚨'
 yellow = '🚧'
 green = '💚'
 index = 0
 while index < len(answer):
     letter = guess[index]
     if letter == answer[index]:
         color = green
     elif letter in answer:
         color = yellow
     else:
         color = red
     print(f"{letter} - {color}")
     index += 1


def get_guess():
return input("Enter your guess : ")


attempts = 1
guess = input("Enter your guess : ")
answer = word_init()
while guess != answer and attempts <6:
 compare_guess(guess, answer)
 guess = get_guess()
 attempts += 1


if guess == answer and attempts <= 6:
 print("You Won! That took " + str(attempts) + " guess(es).")
else:
 print("You lost. The answer was " + answer + ".")
