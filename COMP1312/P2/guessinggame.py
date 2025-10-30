# Do NOT include this in the submitted answer
import random
random.seed(42)
number = random.randint(1, 50)

# Submit only the game logic below
guess = int(input('Guess a number: '))
count = 1
while guess != number:
    if guess < number: 
        print('Too Low')
        count += 1
    if guess > number: 
        print('Too High')
        count += 1
    guess = int(input('Guess another number: '))

print('Correct!')
print(f"Number of guesses taken: {count}")