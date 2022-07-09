import string
string.punctuation
dictionary=dict()
stroka="Ukraine  kiev, ?odessa, kiev ukraine ... lviv: odessa kiev, dnepr, &Donetsk"
#Переводим всё в нижний регистр
stroka=stroka.lower()
#Находим знаки Пунктуации в тексте и заменяем их пробел
for p in string.punctuation:
    if p in stroka:
        stroka=stroka.replace(p, '')
#Разбиваем текст на слова
for ch in stroka:
    words = stroka.split ()
#Повторяющийся слова считаем
for word in words:
    if word in dictionary:
        dictionary[word]+=1
    else:
        dictionary[word]=1
print("Your string:  ",stroka)
print(dictionary)