
class Person:
    def __init__(self,first_name, last_name, email, phone_number, address):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.phone_number=phone_number
        self.address=address

    def print_person(self):
        print("from personn classs:  ",self.first_name)

class Author(Person):
    def __init__(self, first_name, last_name, email, phone_number, address,book_list=[]):
        super().__init__(first_name, last_name, email, phone_number, address)
        self.book_list=book_list

    def add_book(self,book):               
        self.book_list.append(book)        
        print(book.title)

class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def print_books(self):
        print("from bookm class:  ",self.title,"   authorrrr :",self.author,"  isbn   :",self.isbn)

class BookShop:

    def __init__(self,inventory=[]):
        self.inventory=inventory
        #self.sold_book=sold_book

    def add_books(self,book):
        self.inventory.append(book) 
        print("from bookshop book: ",book.title)     

    def search(self,title, author_name):
       pass
    
    def sell(book):    
        pass
    
    
    def sales(author):
        pass


shop_obj=BookShop()
author_obj=Author("K R Meera","thaiii","kr@gmail.com",78888888,"addressssssssss")  
author_obj.print_person()     

book_obj=Book("alchemist","Poulooo","12233488hdjhed")
book_obj.print_books()
author_obj.add_book(book_obj)
shop_obj.add_books(book_obj)


        
        