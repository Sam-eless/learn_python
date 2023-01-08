import json


class Question:

    def __init__(self, question, difficulty, answer):
        self.question = question
        self.difficulty = difficulty
        self.answer = answer
        self.points = self.difficulty * 10
        self.asked_question = False
        self.user_answer = None

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов"""
        return self.points

    def is_correct(self, user_answer):
        """Возвращает True, если ответ пользователя совпадает
          с верным ответом иначе False."""
        if user_answer == self.answer:
            self.asked_question = True
            return True
        else:
            return False

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5"""
        return f"Вопрос: {self.question}\nСложность {self.difficulty}/5\n"

    def build_feedback(self, user_answer):
        """Возвращает:
        Ответ верный, получено __ баллов
        или
        Ответ неверный, верный ответ __"""
        if self.is_correct(user_answer):
            return f"Ответ верный, получено {self.points} баллов"
        else:
            return f"Ответ неверный, верный ответ {self.answer}"


def load_questions(filename):
    """Загрузка списка вопросов из файла"""
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data


def create_instances(list_questions):
    """Создание списка экземпляров класса по списку вопросов"""
    questions = [Question(i["q"], int(i["d"]), i["a"]) for i in list_questions]
    return questions


def output_statistics(questions):
    """Возвращает:
    Отвечено __ вопроса из __
    Набрано баллов: __"""
    correct_answers, total_answers, score = 0, 0, 0

    for question in questions:
        total_answers += 1
        if question.asked_question:
            correct_answers += 1
            score += question.points

    return f"Вот и всё! \n" \
           f"Отвечено {correct_answers} вопроса из {total_answers}\n" \
           f"Набрано баллов: {score}"
