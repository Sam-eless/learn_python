from utils import load_random_word
from player import Player


user_name = input("Введите имя игрока ")
player = Player(user_name)

print(f"Привет, {user_name}!")

# загружаем случайное слово из списка
random_word = load_random_word()

print(f"Составьте {random_word.count_subwords()} слов из слова: {random_word.word}\n"
      f"Слова должны быть не короче 3 букв\n"
      f"Чтобы закончить игру, угадайте все слова или напишите \"stop\"\n"
      f"Поехали, ваше первое слово?")

# запускаем цикл вопросов, пока не будут отгаданы все подслова
while player.count_used_words() < random_word.count_subwords():
    user_answer = input().lower()

    if len(user_answer) < 3:
        print("слишком короткое слово")

    # завершаем цикл, переходим к выводу статистики
    elif user_answer in ["stop", "стоп"]:
        break

    elif not random_word.check_word(user_answer):
        print("неверно")

    elif player.is_usage_before(user_answer):
        print("уже использовано")
    else:
        print(f"Верно, {user_answer}")
        player.add_to_used(user_answer)

print(f"Игра завершена, вы угадали {player.count_used_words()} слов!")
