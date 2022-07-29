def stop_words(words: list):
    def wrapper(func):
        def check_stop_words(*args, **kwargs):
            result = func(*args, **kwargs).split(' ')
            new_list = []
            for i in result:
                if i in words:
                    new_list.append('*')
                    continue
                new_list.append(i)
            
            messages = ' '.join(new_list)
            return messages
        return check_stop_words
    return wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW !"

print(create_slogan("Steve"))

assert create_slogan("Steve") == "Steve drinks * in his brand new * !"


