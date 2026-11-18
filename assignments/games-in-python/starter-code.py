# Código Inicial para a Tarefa do Jogo da Forca

import random

# Lista de palavras possíveis
words = ['python', 'hangman', 'challenge', 'programming', 'computer']

secret_word = random.choice(words)
guessed_letters = set()
incorrect_guesses = 0
max_incorrect = 6

print("Bem-vindo ao jogo da Forca!")

while incorrect_guesses < max_incorrect and not set(secret_word).issubset(guessed_letters):
	progress = " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)
	print(f"\nPalavra: {progress}")
	print(f"Tentativas incorretas restantes: {max_incorrect - incorrect_guesses}")

	guess = input("Digite uma letra: ").strip().lower()
	if len(guess) != 1 or not guess.isalpha():
		print("Entrada inválida. Digite apenas uma letra.")
		continue
	if guess in guessed_letters:
		print("Você já tentou essa letra.")
		continue

	guessed_letters.add(guess)
	if guess not in secret_word:
		incorrect_guesses += 1
		print("Essa letra não está na palavra.")
	else:
		print("Boa! Essa letra está na palavra.")

if set(secret_word).issubset(guessed_letters):
	print(f"\nParabéns! Você venceu. A palavra era: {secret_word}")
else:
	print(f"\nFim de jogo! Você perdeu. A palavra era: {secret_word}")
