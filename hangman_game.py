import random
import re


class hangman:
    def __init__(self):
        self.word_list = ['sensitive', 'humidity', 'backpack', 'travelling',
                          'silence', 'allergy']
        self.word = random.choice(self.word_list)
        self.word_completion = "-" * len(self.word)
        self.guessed = False
        self.guessed_letters = []
        self.guessed_words = []
        self.tries = 6


class get_play(hangman):
    def get_word(self):
        return self.word.upper()

    def play(self):
        print("Hi! Welcome to Hangman game!!")
        print("Let us start!")
        print(self.word_completion)
        print("\n")
        while not self.guessed and self.tries >= 0:
            print("You have ", self.tries, " tries")
            guess = input("Please guess a letter or word: ")
            if len(guess) == 1 and guess.isalpha():
                if guess in self.guessed_letters:
                    print("You already guessed the letter", guess)
                elif guess not in self.word:
                    print(guess, "is not in the word.")
                    self.tries -= 1
                    self.guessed_letters.append(guess)
                else:
                    print("Good job,", guess, "is in the word!")
                    self.guessed_letters.append(guess)
                    self.word_as_list = list(self.word_completion)
                    indices = [i for i, letter in enumerate(self.word)
                               if letter == guess]
                    for index in indices:
                        self.word_as_list[index] = guess
                        self.word_completion = "".join(self.word_as_list)
                    if "-" not in self.word_completion:
                        self.guessed = True
            elif len(guess) == len(self.word) and guess.isalpha():
                if guess in self.guessed_words:
                    print("You already guessed the word", guess)
                elif guess != self.word:
                    print(guess, "is not the word.")
                    self.tries -= 1
                    self.guessed_words.append(guess)
                else:
                    self.guessed = True
                    self.word_completion = self.word
            else:
                print("Not a valid guess.")
            print(self.word_completion)
            print("\n")
        if self.guessed:
            print("Congrats, you guessed the word! You win!")
            print(re.match("[a-z]+", self.word))
        else:
            print("Sorry, you ran out of tries.")
            print(" The word was " + self.word + ". Maybe next time!")
            print(re.match("[a-z]+", self.word))


object1 = hangman()
object2 = get_play()
object2.get_word()
object2.play()
