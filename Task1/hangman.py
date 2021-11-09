# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string


WORDLIST_FILENAME = "words.txt" 



def load_words():
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):

    return random.choice(wordlist)
wordlist = load_words()

def number_of_unique_letters(word):
  return len(set(word))


def is_word_guessed(secret_word, letters_guessed):

    for x in secret_word:
      if(x not in letters_guessed): return False
    return True



def get_guessed_word(secret_word, letters_guessed):

    correct_letters = list()
    for x in secret_word:
      if(x in letters_guessed): correct_letters.append(x)
      else: correct_letters.append('_ ')

    return ''.join(correct_letters)



def get_available_letters(letters_guessed):

    all_letters = string.ascii_lowercase
    available_letters = sorted(set(all_letters).difference(set(letters_guessed)))
    return ''.join(available_letters)
    
    
def is_vowel(letter):
  vowels = 'aeiou'   
  return (letter in vowels)

def read(warnings, lives):
    while(True):
        try:
          letter = input("Make your guess! Please use only latin letters: ")
          if(len(letter) > 1 or not letter.isalpha()):
            raise TypeError
          else: break
        except TypeError:
          print('Please use only latin letters')
          warnings -= 1
          if(warnings <= 0):
            lives -= 1
            print("You have no warnings! You lost your guess, you have " + str(lives) + " guesses")
            if(lives == 0):
              break 
          else:
            print('You have ' + str(warnings) + ' warnings left. Be carefull next time')  
    return letter, warnings, lives

def read_with_hints(warnings, lives):
    while(True):
        try:
          letter = input("Make your guess! Please use only latin letters: ")
          if(len(letter) > 1 or (not letter.isalpha() and letter != '*')):
            raise TypeError
          else: break
        except TypeError:
          print('Please use only latin letters')
          warnings -= 1
          if(warnings <= 0):
            lives -= 1
            print("You have no warnings! You lost your guess, you have " + str(lives) + " guesses")
            if(lives == 0):
              break 
          else:
            print('You have ' + str(warnings) + ' warnings left. Be carefull next time')  
    return letter, warnings, lives


def hangman(secret_word):
    lives = 6
    warnings = 3
    letters_guessed = list()
    print('Welcome to the game Hangman!\nI am thinking of a word that is ' + str(len(secret_word)) + ' letters long.\n----------------------')
    while(True):
      print('You have ' + str(lives) + ' guesses left.')
      print('Available letters: ' + get_available_letters(letters_guessed))
      letter, warnings, lives = read(warnings, lives)
      if(lives == 0):
        print("Game is over, you lost :(\nThe word was " + secret_word)
        break
      letter = letter.lower()
      if letter not in letters_guessed: 
        letters_guessed.append(letter)
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if letter in secret_word: 
          print('Good guess: ' + guessed_word)
        else: 
          print('You missed: ' + guessed_word)
          if(is_vowel(letter)):
            lives -= 2
          else: 
            lives -= 1
        if(lives <= 0):
          print("Game is over, you lost :(\nThe word was " + secret_word)
          break
        print('----------------------')
        if(is_word_guessed(secret_word, letters_guessed)):
          print("Congrats! Your total score is " + str((lives) * number_of_unique_letters(secret_word)) + " points")
          break
      else: 
        warnings -= 1
        print("You have already tried this one")
        if(warnings <= 0):
            lives -= 1 
            print("You have no warnings! You lost your guess, you have " + str(lives) + " guesses")
            if(lives == 0):
              print("Game is over, you lost :(\nThe word was " + secret_word)
              break
        else:
            print('You have ' + str(warnings) + ' warnings left. Be carefull next time')  

        print('----------------------')
    



def match_with_gaps(my_word, other_word):
 
    temp = list()
   
    my_word = my_word.replace(" ", "")
    if(len(my_word) != len(other_word)): return False
    for i in range(0, len(my_word)):
      if(my_word[i] != '_' and my_word[i] != other_word[i]): return False
    for i in range(len(other_word)):
      temp = list()
      for j in range(len(other_word)):
        if(other_word[i] == other_word[j]):
          temp.append(my_word[j])
      flag = 1
      if (temp[0] == '_'): flag = 0
      for x in temp:
        if((x == '_' and flag == 1) or (x != '_' and flag == 0)): return False


    return True



def show_possible_matches(my_word):
    matched_words = list()
    for other_word in wordlist:
      if(match_with_gaps(my_word, other_word)):
        matched_words.append(other_word)
    if(len(matched_words) == 0): print("No matches found")
    else: 
      for x in matched_words: print(x, end=" ")



def hangman_with_hints(secret_word):
    lives = 6
    warnings = 3
    letters_guessed = list()
    print('Welcome to the game Hangman!\nI am thinking of a word that is ' + str(len(secret_word)) + ' letters long.\n----------------------')
    while(True):
      print('You have ' + str(lives) + ' guesses left.')
      print('Available letters: ' + get_available_letters(letters_guessed))
      letter, warnings, lives = read_with_hints(warnings, lives)
      if(lives == 0):
        print("Game is over, you lost :(\nThe word was " + secret_word)
        break
      if(letter == '*'):
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        print(guessed_word)
        show_possible_matches(guessed_word)
        print()
      else:
        letter = letter.lower()
        if letter not in letters_guessed: 
          letters_guessed.append(letter)
          guessed_word = get_guessed_word(secret_word, letters_guessed)
          if letter in secret_word: 
            print('Good guess: ' + guessed_word)
          else: 
            print('You missed: ' + guessed_word)
            if(is_vowel(letter)):
              lives -= 2
            else: 
              lives -= 1
          if(lives <= 0):
            print("Game is over, you lost :(\nThe word was " + secret_word)
            break
          print('----------------------')
          if(is_word_guessed(secret_word, letters_guessed)):
            print("Congrats! Your total score is " + str((lives) * number_of_unique_letters(secret_word)) + " points")
            break
        else: 
          warnings -= 1
          print("You have already tried this one")
          if(warnings <= 0):
              lives -= 1 
              print("You have no warnings! You lost your guess, you have " + str(lives) + " guesses")
              if(lives == 0):
                print("Game is over, you lost :(\nThe word was " + secret_word)
                break
          else:
              print('You have ' + str(warnings) + ' warnings left. Be carefull next time')  

          print('----------------------')


if __name__ == "__main__": 
  secret_word = choose_word(wordlist)
  while(True):
    check = input("Do you want to play classic hangman or hangman with hits\nEnter 0 to play classic version\nEnter 1 to play hint version\n")
    if(check == '0'):
      hangman(secret_word)
      break
    elif(check == '1'):
      hangman_with_hints(secret_word)
      break
    else: print("You have to print 0 or 1")