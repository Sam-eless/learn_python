import random
from utils import load_questions, create_instances, output_statistics

# загрузка списка вопросов
list_question = load_questions("questions.json")

# создание списка экземпляров класса по списку вопросов
questions = create_instances(list_question)

print("Игра начинается")

# создание копии списка вопросов и перемешивание его
questions_random = questions.copy()
random.shuffle(questions_random)

# старт цикла вопросов
for question in questions_random:

    user_answer = input(question.build_question())
    question.user_answer = user_answer
    print(question.build_feedback(user_answer))

# вывод статистики
print(output_statistics(questions_random))
