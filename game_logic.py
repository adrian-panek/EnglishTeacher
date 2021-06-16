import random
import words_import

incorrect_words = []

def game_logic():
	correct_answers = 0
	incorrect_answers = 0
	number_of_words = input("Ile slowek chcesz powtorzyc: ")
	if int(number_of_words) > len(words_import.words):
		print("Nie ma tylu slow w slowniku!")
		quit()
	for i in range (0, int(number_of_words)):
		#picking random word
		random_word = random.choice(list(words_import.words))
		#taking polish translation word from dictionary
		learn = words_import.words[random_word]
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
