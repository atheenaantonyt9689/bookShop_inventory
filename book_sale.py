
from typing import Counter


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

    def __init__(self,inventory=[],sold_book=[]):
        self.inventory=inventory
        self.sold_book=sold_book

    def add_books(self,book):
        self.inventory.append(book) 
        
        return book.title
            

    def search(self,title,author):        
        for book in self.inventory:
            
            
            if book.title==title and book.author==author:
                #print("kkkkkk",Counter(self.inventory))
                #print("number of copies ",no_of_book)

                #print(book.title,book.author,book.isbn)
                #n=int(input(" enter the number of copy required: "))
                
                return book.title

            else:
               return False
        
       
    def sell(self,book):
            print("length",len(self.inventory))
            self.sold_book.append(self.inventory.pop(self.inventory.index( book ) ) )    
            print("afterrrr",len(self.inventory))
           
            return book.title         
        
        
            
        
    
    def sales(self,author): 
         #print(author)     
         for i in self.sold_book:
            print("qqqq",i.title)
            if i.author == author:
                #todo
                
                
                return True
            else:
                return False
    


     
        
        # find sales of books for a author
         # will be rquired to calculate author royalty
       

