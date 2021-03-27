import random
from pyfiglet import figlet_format
from termcolor import colored

#a nice welcome header
header = figlet_format("ENGLISH TEACHER")
header = colored(header, color = "cyan")
print(header)

#reading all words from file
words = {}
with open("words_base.txt") as f:
	for line in f:
		(key, val) = line.split()
		words[str(key)] = val

incorrect_words = []
correct_answers = 0
incorrect_answers = 0

number_of_words = input("Ile slowek chcesz powtorzyc: ")
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

print(f"Bylo {incorrect_answers} niepoprawnych odpowiedzi, i {correct_answers} poprawnych")
print(f"Slowa ktore jeszcze nalezy powtorzyc: {incorrect_words}")