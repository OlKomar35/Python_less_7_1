# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не
# настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в
# порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

def count_letters(word):
    count = 0
    for letters in word:
        if letters in vowels:
            count += 1
    return count

text = "пара-ра-рам рам-пам-папам па-ра-па-да"
text_list = text.split()
vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}

count_vowels = list()

for index_word in range(len(text_list)):
    count_vowels.append( count_letters(text_list[index_word]))

flag = True
for i in range(1, len(count_vowels)):
    if count_vowels[i] != count_vowels[i - 1]:
        flag = False
        print("Пам парам")
        break
if flag:
    print('Парам пам-пам')



# решение через лямбда и функции высшего порядка

count_vowels = list(map(lambda word: sum(1 for letter in word if letter in vowels), text_list))

if all(map(lambda x: x == count_vowels[0], count_vowels)):
    print('Парам пам-пам')
else:
    print('Пам парам')