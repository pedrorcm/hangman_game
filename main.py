import random
import re

#Chooses between the two scrapped lists
def which_list():
  choice = int(input('\nWith which list do you want to play?\n1.Brazilian Fruits\n2.Brazilian Names\n>> '))
  if choice == 1:
    openfile = open('fruit_list.txt', 'r')
    return openfile.readlines()

  elif choice == 2:
    openfile = open('name_list.txt', 'r')
    return openfile.readlines()


  else:
    print('choose a VALID option ')
    choice = which_list()
  

#Picks a word in the choosen list
def picking_word(readfile):
  selector = random.randint(0, (len(readfile)-1))
  word = readfile[selector].upper()
  return word.replace("\n", "")

#Prints a "blank" space for each non-revealed word
def hidden_letters(secret_word):
  return [' ' for letter in secret_word]

#Asks for an letter
def ask_for_guess():
  letter = input("\nMake a guess: ").strip().upper()
  if len(letter) > 1:
    print("Enter ONE letter at a time ")
    letter = ask_for_guess()
  return letter

#If the letter is right, "writes" it
def right_letter(guess, secret_word, blank_spaces):
  index = 0
  for letter in secret_word:
    if guess == letter:
      blank_spaces[index] = letter
    index +=1
  return secret_word

#User wants to play again?
def wanna_play_again():
  wpa = input('Do you want to play again?\n1.Yes\n2.No\n>>')
  if wpa == '1' or wpa == 'y' or wpa == 'yes' or wpa == 'YES':
    play()
  elif wpa == '2' or wpa == 'n' or wpa == 'no' or wpa == 'NO':
    print('\nThanks for playing')
    exit()
  else:
    print('Choose a valid option')
    wpa = wanna_play_again()

#Verifies if the letter was already tried
def already_tried(guess, tried):
  if guess in tried:
    print('You already tried this letter. ')
    return True
  else:
    return False

#Counts the wrong attempts.
def error_counter(error_count,secret_word):
  if error_count == 5:
    loser(secret_word)
    wanna_play_again()
  else:
    error_count += 1
    print(f"This word don't have this char. {error_count} of 5 errors.")
    return error_count

#Winner text
def winner():
  print("\nCONGRATS!!! You win!\n\n")
#Loser text
def loser(secret_word):
  print(f"\nGame over. The word was {secret_word}\n\n")
  hanged = True
  return hanged

#Main function. Defines states (if hanged or if word was completed) and has a list to store the letters that was already tried
def play():
  secret_word = picking_word(which_list())
  blank_spaces = hidden_letters(secret_word)
  hanged = False
  word_completed = False
  error_count = 0
  tried = []

  while not hanged and not word_completed:
    print(blank_spaces)
    guess = ask_for_guess()

    while already_tried(guess, tried):
      guess = ask_for_guess()
    tried.append(guess)

    if guess in secret_word:
      right_letter(guess, secret_word, blank_spaces)
    else:
      error_count = error_counter(error_count, secret_word)
    

    word_completed = ' ' not in blank_spaces
    if word_completed:
      winner()
      wanna_play_again()
    
    
if __name__ == '__main__':
  play()