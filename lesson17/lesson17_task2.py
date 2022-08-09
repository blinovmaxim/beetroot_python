class Author:
     def __init__(self,name,country,birthday,books=[]):
        self.name=name
        self.country=country
        self.birthday=birthday
        self.books=books

class Book:
     def __init__(self,name,year,author:Author):
        self.name=name
        self.books=year
        self.author=author
        all_books=0
        


class Library:
    def __init__(self,name,books=[],authors=[]):
        self.name=name
        self.books=books
        self.authors=authors
        self.books=[]    
        
    def new_book(self,name: str, year: int, author: Author,book):
        b=Book
        book_add=[name,year,author]
        self.books.append(book_add)
        return b


    # def group_by_author(author: Author):
    
    # def group_by_year(year: int):

Lib=Library("Harry",2034,"Potter")

Lib.new_book()