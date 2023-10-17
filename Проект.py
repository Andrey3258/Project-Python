
import random

class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.max_guesses = 10
        self.current_word = ""
        self.current_guesses = []

    def choose_word(self):
        self.current_word = random.choice(self.word_list).lower()

    def print_current_state(self):
        print("Загаданное слово: ", end="")
        for letter in self.current_word:
            if letter in self.current_guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("\n")

    def process_guess(self, guess):
        if guess in self.current_guesses:
            print("Вы уже говорили эту букву. Введите новую.")
        else:
            self.current_guesses.append(guess)
            if guess not in self.current_word:
                self.max_guesses -= 1

    def play(self):
        self.choose_word()

        while self.max_guesses > 0 and set(self.current_guesses) != set(self.current_word):
            self.print_current_state()

            guess = input("Введите букву: ").lower()
            while len(guess) != 1 or not guess.isalpha():
                print("Ошибка. Введите одну букву.")
                guess = input("Введите букву снова: ").lower()

            self.process_guess(guess)

        if set(self.current_guesses) == set(self.current_word):
            print("Вы выйграли! Компьютер загадал слово ", self.current_word)
        else:
            print("Вы проиграли! Компьютер загадал слово", self.current_word)


word_list = ['автомобиль', 'компьютер', 'яблоко', 'самолет', 'собака', 'кошка', 'осьминог', 'дом', 'роза', 'книга']
game = HangmanGame(word_list)
game.play()
