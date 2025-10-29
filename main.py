import random
print("Вы стали участником игры Полечудес")
print("Сейчас мы загадаем слово, а вы его должны отгадать")
print("Вопрос: угадайте домашнее животное")
# Выбор слова для угадывания
file_name = "Полечудес.txt"
try:
    with open(file_name, "r", encoding="utf-8") as my_file:
        words = my_file.read().split()
        if not words:
            print("файл пуст или не содержит слов")
        else:
            secret_word = random.choice(words)
            guessed_letters = set()
            correct_letters = set(secret_word)
            current_player_index = 0
except FileNotFoundError:
     print(f"Файл {file_name} не найден")

# Функция для отображения текущего состояния слова
def display_progress(word, guessed_letters):
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    return display_word.strip()

# Добавление игроков

players = []
num_players = int(input("Введите количество игроков: "))
for i in range(num_players):
    name = input(f"Введите имя игрока {i+1}: ")
    players.append({"name": name, "score": 0})


while True:
    current_player = players[current_player_index]
    print(f"\nХод игрока: {current_player['name']}")
    print("Текущее слово: " + display_progress(secret_word, guessed_letters))
    print(f"Баллы: {current_player['score']}")

    guess = input("Введите букву или слово целиком").lower()


    if len(guess) == 1:
        # Попытка угадать букву
        if guess in guessed_letters:
            print("Эту букву уже называли.")
        elif guess in secret_word:
            print("Верно! Вы угадали букву.")
            guessed_letters.add(guess)
            # Начисление очков за угаданную букву
            current_player['score'] += 10
            # Проверка, завершена ли игра
            if correct_letters.issubset(guessed_letters):
                print(f"Поздравляем! Игрок {current_player['name']} выиграл!")
                print(f"Общий счет:\n" + "\n".join([f"{player['name']}: {player['score']}" for player in players]))
                break
        else:
            print("Неверно. Такой буквы нет.")
            # Передача хода
            current_player_index = (current_player_index + 1) % num_players
    elif len(guess) == len(secret_word):
        # Попытка угадать слово целиком
        if guess == secret_word:
            print(f"Поздравляем! {current_player['name']} угадал слово и выигрывает!")
            current_player['score'] += 50  # бонус за угадывание слова
            print(f"Общий счет:\n" + "\n".join([f"{player['name']}: {player['score']}" for player in players]))
            break
        else:
            print("Неверное слово.")
            # Передача хода