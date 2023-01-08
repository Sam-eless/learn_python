import random
import requests
from basic_word import BasicWord


def load_random_word():
    """Возвращает экземпляр класса BasicWord, от случайного слова из списка"""

    # Загружаем список слов
    response = requests.request("GET", "https://www.jsonkeeper.com/b/DK0A").json()

    # Перемешиваем список и создаем экземпляр класса по индексу [0]
    random.shuffle(response)
    basic_word = BasicWord(response[0]["word"], response[0]["subwords"])

    return basic_word
