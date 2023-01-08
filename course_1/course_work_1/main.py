import random

# создаем переменные
words_eng = ['existentiality', 'snake', 'computer', 'airplane', 'fury']
answers = []

# словарь Азбуки Морзе
morse_cod = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}


def morse_encode(word):
    """
    Переводит заданное слово в Азбуку Морзе
    """
    morse_word_list = []
    morse_word = []

    for letter in word:
        morse_word_list.append(morse_cod[letter])
        morse_word = " ".join(morse_word_list)
    return morse_word


def get_word(words):
    """
    Получает случайное слово из заданного списка слов и удаляет его из списка
    """
    local_words_eng = words
    random.shuffle(local_words_eng)
    any_word = local_words_eng[0]
    del local_words_eng[0]

    return any_word


def print_statistics(answers_):
    """
    Выводит статистику правильным и неправильных овтетов
    """
    print(f'Всего задачек: {len(answers_)}')
    print(f'Отвечено верно: {answers_.count(True)}')
    print(f'Отвечено неверно: {answers_.count(False)}')


# приветствие и ожидание старта от пользователя
user_input = input(f'Сегодня мы потренируемся расшифровывать морзянку.\n'
                   f'Нажмите Enter и начнем')

# запускаем цикл вопросов
if user_input in ["", "го", "поехали", "начнем", "летсго"]:
    for i in range(len(words_eng)):
        random_word = get_word(words_eng)
        user_answer = input(f'Слово {i + 1} - '
                            f'{morse_encode(random_word)} ').lower()

        if user_answer == random_word:
            answers.append(True)
            print(f'Верно, {random_word}!\n')
        else:
            answers.append(False)
            print(f'Неверно, {random_word}!\n')

# выводим статистику ответов
print_statistics(answers)
