# Import libraries
import random
import string

# Hanged Man Pictures List
hangman_stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]
# Word list
words = [
    "cat", "dog", "sun", "sky", "car",      # Three-letter words
    "tree", "fish", "moon", "star", "wind", # Four-letter words
    "apple", "grape", "chair", "table", "house", # Five-letter words
    "planet", "summer", "winter", "forest", "garden" # Six-letter words
]

# Variables
Attempts = 6
word = random.choice(words)
Cach_word = ['_'] * len(word)
wrong = []
xx = 0

print(word)
print(''.join(Cach_word))

print(hangman_stages[0])

# Guess user
Guess_User = input('Please enter your guess :\n>> ')

while Attempts > 0 and '_' in Cach_word:

  if Guess_User in wrong:
    print('You have already selected this letter and it is wrong.')

  elif Guess_User in Cach_word:
    print('You have already chosen this letter and it is correct.')

  elif Guess_User in word and '_' in Cach_word:
    for x in range(len(word)):
      if Guess_User == word[x]:
         Cach_word[x] = Guess_User
  
  else:
    print(hangman_stages[xx])
    Attempts -= 1
    if Attempts == 0:
      break
    wrong.append(Guess_User)
    xx += 1

  if '_' not in Cach_word:
    break
  
  print(''.join(Cach_word))
  print(f'You still have {Attempts} attempts left.')
  Guess_User = input('Guess another letter :\n>> ')

if Attempts > 0:
  print('''
  ************
    YOU WIN!
  ************
  ''')
else:
  print('''
  *************
    YOU LOSE!
  *************
  ''')