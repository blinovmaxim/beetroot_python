#Создаём список с днями недели
spisok_day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print("Lists with days of the week: ",spisok_day)

#Создаём словарь , где 1 - Ключи, А Monday- значение и т.д
dictionary={}
for index,value in enumerate(spisok_day):
    dictionary[index+1]=value
print("Your dictionary with days of the week: ",dictionary)

#Создаём обратный словарь, где Monday - это ключ , а 1 это значение
dictionary_inverse={}
for key,val in dictionary.items():
    dictionary_inverse[val]=key
    
print("Your reverse dictionary with days of the week: ", dictionary_inverse)
