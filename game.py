import random

# Accept level input unless it is something besides a positive integer (letter or negative integer).
while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    if level <= 0:
        continue

    # The number variable is a random one between 1 and the level.
    number = random.randint(1, level)
    break

# Accept guess input unless it is something besides a positive integer (letter or negative integer).
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
    except ValueError:
        continue

    # Output results, depending on whether the guess is less than, larger than, or the same as the random number.  Looping ends when guess is the same as the random number.
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else:
        print("Just right!")
        break