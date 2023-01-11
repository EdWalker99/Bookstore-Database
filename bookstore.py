import sqlite3

db = sqlite3.connect('bookstore_db')
cursor = db.cursor()

#Create function to seach for a specific book in stock
def search_book():

    id_lookup = int(input("Please enter the ID of the book you would like to view: "))
    cursor.execute('''
                   SELECT * FROM bookstore WHERE ID=?
                   ''', (id_lookup,))

    search = cursor.fetchone()
    print(search)

#create function to add a book entry to the database
def add_book():

    i_d = int(input("Please enter the ID of this book entry: "))
    title = input("Please enter the title of this book entry: ")
    author = input("Please enter the author of this book: ")
    qty = int(input("Please enter the quantity of books in stock: "))
    
    cursor.execute('''INSERT INTO bookstore VALUES(?,?,?,?)''',(i_d, title, author, qty))
    print("Entry added!")
    db.commit()

#create function to update an entry within the database
def update_book():

#display all books in database
    cursor.execute('''
                   SELECT * FROM bookstore
                   ''')
    books = cursor.fetchall()
    print(books)

#request user to specify which book they would like to edit
    id_edit = int(input("Please enter the ID of the book you would like to edit: "))
    edit_column = input("What aspect would you like to edit? (ID,Title,Author,Qty): ").lower()

#edit specific column based on user choice 
    if edit_column == 'id':
        new_id = int(input("Please enter the new ID of the book: "))
        cursor.execute('''
                       UPDATE bookstore SET ID=? WHERE ID=?''',(new_id,id_edit,))
        print("Entry Updated.")
        db.commit()

    elif edit_column == 'title':
        new_title = input("Please enter the new title of the book: ")
        cursor.execute('''
                       UPDATE bookstore SET Title=? WHERE ID=?''',(new_title,id_edit,))
        print("Entry Updated.")
        db.commit()

    elif edit_column == 'author':
        new_author = input("Please enter the new author of the book: ")
        cursor.execute('''
                       UPDATE bookstore SET Author=? WHERE ID=?''',(new_author,id_edit,))
        print("Entry Updated.")
        db.commit()

    elif edit_column == 'qty':
        new_qty = int(input("Please enter the new quantity of the book: "))
        cursor.execute('''
                       UPDATE bookstore SET Quantity=? WHERE ID=?''',(new_qty,id_edit,))
        print("Entry Updated.")
        db.commit()
#print error message if user inputs invaled entry
    else:
        print("Invalid Entry.")

#create function to delete book from database
def delete_book():

#display all books in database 
    cursor.execute('''
                   SELECT * FROM bookstore
                   ''')
    books = cursor.fetchall()
    print(books)

#request specific book choice from user
    id_delete = int(input("Please enter the ID of the book you would like to delete: "))

#remove that book from database
    cursor.execute(''' 
                   DELETE FROM bookstore WHERE ID=?''', (id_delete,))
    print("Entry Removed!")
    db.commit()

#create table called bookstore with columns ID, Title, Author and Quantity 
cursor.execute('''
               CREATE TABLE IF NOT EXISTS bookstore(
               ID INTEGER PRIMARY KEY NOT NULL UNIQUE,
               Title TEXT NOT NULL,
               Author TEXT NOT NULL,
               Quantity INTEGER NOT NULL)
               ''')

print("Database Created!")
db.commit()

#Populate the table with entries to begin with

id1 = 3001
title1 = 'A Tale Of Two Cities'
author1 = 'Charles Dickens'
qty1 = 30

id2 = 3002
title2 = 'Harry Potter and the Philosopher\'s Stone'
author2 = 'J.K. Rowling'
qty2 = 40

id3 = 3003
title3 = 'The Lion, The Witch and The Wardrobe'
author3 = 'C.S. Lewis'
qty3 = 25

id4 = 3004
title4 = 'The Lord of The Rings'
author4 = 'J.R. Tolkien'
qty4 = 37


id5 = 3005
title5 = 'Alice in Wonderland'
author5 = 'Lewis Carroll'
qty5 = 12

books_ = [(id1,title1,author1,qty1),(id2,title2,author2,qty2),(id3,title3,author3,qty3),(id4,title4,author4,qty4),(id5,title5,author5,qty5)]
#add entries to table
#this will be commented out so we don't end up adding repeat entries 
cursor.executemany(''' INSERT INTO bookstore VALUES(?,?,?,?)''',(books_))
print("Entries Added!")
db.commit()

user_choice = ""

### MAIN PROGRAM ### 
while user_choice != 'quit':
    print("----------------------------")
    user_choice = input("What would you like to do - search/edit/add/delete/quit? : ").lower()

    if user_choice == 'search':
        print("----------------------------")
        search_book()
    
    elif user_choice == 'edit':
        print("----------------------------")
        update_book()
    
    elif user_choice == 'add':
        print("----------------------------")
        add_book()

    elif user_choice == 'delete':
        print("----------------------------")
        delete_book()

    elif user_choice == "quit":
        print("----------------------------")
        print("Goodbye")
    else:
        print("Oops - incorrect input")

