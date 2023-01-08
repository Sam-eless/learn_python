from utils import load_students, load_professions, get_student_by_pk, get_profession_by_title, check_fitness

# подгружаем списки студентов и профессий
students = load_students('students.json')
professions = load_professions('professions.json')

input_student_pk = int(input('Введите номер студента '))

student = get_student_by_pk(students, input_student_pk)

# вывод информации о студенте
if student:
    print(f'Студент {student["full_name"]}\n'
          f'Знает {", ".join(student["skills"])}')
else:
    print('У нас нет такого студента')
    quit()

input_profession = input('Выберите специальность для оценки студента').title()

profession = get_profession_by_title(professions, input_profession)


if not profession:
    print('У нас нет такой специальности')
    quit()
else:
    # вывод результата соответствия студента указанной профессии
    check_dict = check_fitness(student, profession)
    print(f'Пригодность {round(check_dict["fit_percent"])}%')

    # если студент совсем не подходит, не выводим информацию со имеющимися скилами
    if check_dict["fit_percent"] != 0:
        print(f'{student["full_name"]} знает {", ".join(check_dict["has"])}')

    # если студент не подходит на 100%, выводим информацию с отсутствующими скилами
    if check_dict["fit_percent"] != 100:
        print(f'{student["full_name"]} не знает {", ".join(check_dict["laks"])}')
