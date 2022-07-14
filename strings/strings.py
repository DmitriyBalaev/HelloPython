#Конкатенация
print('hello ' + 'friend')
print("hello " + "friend")

#Интерполяция
first_name = 'Dmitry'
greething = 'Hello'
print(f'{greething}, {first_name}!')

#Извлечение символов из строки
first_name = 'Dmitry'
print(first_name[0]) # получение символа по индексу
print(first_name[-2])#обратный отсчет по индексу

#срезы строки
value = '17-04-1991'
value2 = 'akira'
print(value[0:2])
print(value2[3:]) # С открытыми границами
print(value2[:4])
print(value2[1:5:2]) # 3 параметр шаг
print(value2[::-1]) # переворачиваем строку

#Multi-line
text = '''например
вот
так'''
print(text)


