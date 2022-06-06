import random

students_list = []
count_less_ten, count_ten_fifteen, count_fifteen_plus = 0, 0, 0

for _ in range(random.randint(1, 50)):
    students_list.append(random.randint(1, 30))

for i in range(len(students_list)):
    if students_list[i] < 10:
        count_less_ten += 1
    elif students_list[i] >= 10 and students_list[i] <= 15:
        count_ten_fifteen += 1
    else:
        count_fifteen_plus += 1

print(f'A percentagem dos estudantes que entraram menos de 10 vezes no refeitório da universidade é: {round((count_less_ten * 100) / len(students_list), 2)}%;\
  \nA percentagem dos estudantes que entraram de [10 à 15] vezes no refeitório da universidade é: {round((count_ten_fifteen * 100) / len(students_list), 2)}%;\
  \nA percentagem dos estudantes que entraram mais de 15 vezes no refeitório da universidade é: {round((count_fifteen_plus * 100) / len(students_list), 2)}%.')