list= ['@','05']


























# def list_replace(words[],str()):
#     for i in range(len(words)):
#         func=func.replace(words[i],'*')
#         return 
# words=["pepsi","BMW"]
# stroka="Maxim drinks pepsi in his brand new BMW!"
# stroka_list=stroka.split()
# new=[]
# for i in stroka_list:
#     if i in words:
#         new.append('*')
#         continue
#     new.append(i)
   


# print(stroka_list,type(stroka_list),stroka_list[1])
# print(words,type(words), words[1])
# print(new)

# def stop_words(words: list):
#     def helper(func):
#         def check_stop_words(*args, **kwargs):
#             res = func(*args, **kwargs).split(' ')
#             new = []
#             for i in res:
#                 if i in words:
#                     new.append('*')
#                     continue
#                 new.append(i)
            
#             messages = ' '.join(new)
#             return messages
#         return check_stop_words
#     return helper