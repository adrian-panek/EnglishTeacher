import random
from pyfiglet import figlet_format
from termcolor import colored

#a nice welcome header
def header_maker():
	header = figlet_format("PROFESOR HENRY REMAKE")
	header = colored(header, color = "cyan")
	print(header)

#reading all words from file
words = {}
def read_from_file():
	with open("words_base.txt") as f:
		for line in f:
			(key, val) = line.split()
			words[str(key)] = val

def game_logic():
	correct_answers = 0
	incorrect_answers = 0
	incorrect_words = []
	number_of_words = input("Ile slowek chcesz powtorzyc: ")
	if int(number_of_words) > len(words):
		print("Nie ma tylu slow w slowniku!")
		quit()
	for i in range (0, int(number_of_words)):
		#picking random word
		random_word = random.choice(list(words))
		#taking polish translation word from dictionary
		learn = words[random_word]
		#basic "game" logic
		print(f"Twoje slowo po polsku to: {random_word}")
		user_input = input("Podaj opowiednik tego slowa po angielsku: ").lower()
		if user_input == learn:
			correct_answers += 1
			print("poprawna odpowiedź")
		else:
			print("niepoprawna odpowiedź")
			incorrect_answers += 1
			incorrect_words.append(learn)
	print(f"Ilość poprawnych odpowiedzi: {correct_answers}, ilość niepoprawnych odpowiedzi: {incorrect_answers}")
	if incorrect_answers == 0:
		print("Brawo, 100% poprawnych odpowiedzi!")
	else:
		print(f"Niepoprawnie wprowadzone slowa: {incorrect_words}")

header_maker()
read_from_file()
game_logic()

