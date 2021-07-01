from book_sale import BookShop,Author,Book
def runner():

    shop_obj=BookShop()
    author_obj=Author("K R Meera","thaiii","kr@gmail.com",78888888,"addressssssssss")  
    author_obj.print_person()     

    book_obj=Book("alchemist","Poulooo","12233488hdjhed")
    book_obj2=Book("water","kkk","12233488")
    
    book_obj.print_books()

    author_obj.add_book(book_obj)

    add_book=shop_obj.add_books(book_obj)
    add_book2=shop_obj.add_books(book_obj2)
    print("Book ",add_book)
    print("Book2 ",add_book2)

    search_book=shop_obj.search("alchemist","Poulooo")
    print("serched  ",search_book)

    sell_book=shop_obj.sell(book_obj)
    print(" ",sell_book) 
    

    sales_details=shop_obj.sales("Poulooo")
    print(sales_details)
    

runner()