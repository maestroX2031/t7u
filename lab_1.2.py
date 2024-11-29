import random

# Список слів для вгадування
word_list = ["яблуко", "банан", "персик", "груша", "апельсин"]
# Вибір випадкового слова з цього списку
secret_word = random.choice(word_list)
attempts = 0
guessed_word = ["_"] * len(secret_word)

print("Я загадав слово, спробуй вгадати його!")

# Основний цикл гри
while "".join(guessed_word) != secret_word:
    print(" ".join(guessed_word)) 
    guess = input("Введи одну літеру: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Будь ласка, введи лише одну літеру.")
        continue

    attempts += 1

    # Перевірка, чи є введена буква в слові
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
        print("Правильно!")
    else:
        print("Немає такої букви в слові.")
    
    if "".join(guessed_word) == secret_word:
        print(f"Вітаю! Ти вгадав слово '{secret_word}' за {attempts} спроб.")
