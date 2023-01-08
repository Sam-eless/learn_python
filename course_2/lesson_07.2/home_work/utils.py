import json


def load_students(filename):
    """Загружает список студентов из файла"""
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data


def load_professions(filename):
    """ Загружает список профессий из файла"""
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data


def get_student_by_pk(students, pk):
    """Получает словарь с данными студента по его pk"""
    for student in students:
        if student["pk"] == pk:
            return student


def get_profession_by_title(professions, title):
    """Получает словарь с инфо о профессии по названию"""
    for profession in professions:
        if profession["title"] == title:
            return profession


def check_fitness(student, profession):
    """Возвращает словарь:какиие навыки есть, каких нет, на сколько процентов подходит студент"""
    student_skill = set(student["skills"])
    profession_skills = set(profession["skills"])

    skills = {
        "has": student_skill.intersection(profession_skills),
        "laks": profession_skills.difference(student_skill),
        "fit_percent": len(student_skill.intersection(profession_skills)) / len(profession_skills) * 100
    }
    return skills
