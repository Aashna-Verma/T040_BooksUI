# T040 - 07/12/2021 Version 1.0
# Liana Cabalit 101233041, Alvin Muguluma 101219375, Koralie Mokam 101221527, Aashna Verma 101225434

import os
from T040_P3_sorting import *
from P5_T040_load_dataset import *
from T040_P2_search_modify_dataset import *

ENTER_T = 'Enter title: '
ENTER_C = 'Enter category: '
ENTER_A = 'Enter author: '
ENTER_R = 'Enter rate: '
NSC = 'No such command'

def userIn_A() -> tuple:
    """ Returns a tuple of book data inputed by user

        >>> userIn_A()
        Enter title: a
        Enter author: a
        Enter rate: a
        Enter publisher: a
        Enter page count: a
        Enter category: a
        Enter language: a

        returns tuple -> (a,a,a,a,a,a,a)
    """
    title = input(ENTER_T)
    author = input(ENTER_A)
    rating = input(ENTER_R)
    publisher = input('Enter publisher: ')
    page_count = input('Enter page count: ')
    generes = input(ENTER_C)
    language = input('Enter language: ')

    return (title, author, rating, publisher, page_count, generes, language)

command =  {'L' : ['Enter csv filename: ', load_dataset],
            'A' : [userIn_A , add_book],
            'R' : [ENTER_T, ENTER_C, remove_book],
            'F' : [ENTER_T, find_books_by_title],
            'NC': [ENTER_C, print_dictionary_category],
            'CA': [ENTER_A, get_author_categories],
            'CB': [ENTER_T, all_categories_for_book_title],
            
            'G' :  ['Enter what you want to get: ',
                   {'R' : [ENTER_R, get_books_by_rate], 
                    'A' : [ENTER_A, get_books_by_author], 
                    'P' : ['Enter publisher: ',get_books_by_publisher], 
                    'C' : [ENTER_C, get_books_by_category], 
                    'CT': [ENTER_C, ENTER_T, check_category_and_title], 
                    'CR': [ENTER_C, ENTER_R, get_book_by_category_and_rate]
                    }],

            'S' :  ['Enter what you want to sort by: ',
                   {'T' : sort_books_title, 
                    'R' : ['Sort by A)scending rate or D)escending rate: ', 
                        {'A': sort_books_descending_rate, 
                         'D': sort_books_ascending_rate}],
                    'P' : sort_books_publisher, 
                    'C' : sort_books_category, 
                    'PA': sort_books_pageCount
                    }],

            'Q' : False
            }

def prompt() -> str :
    """ Returns a string depending on the input given

        >>> all_commands()
        1- Command Line L)oad file
        2- Command Line A)dd book
        3- Command Line R)emove book
        4- Command Line F)ind book by title
        5- Command Line NC) Number of books in a category
        6- Command Line CA) Categories for an author
        7- Command Line CB) Categories for a book title
        8- Command Line G)et book
                R)ate A)uthor P)ublisher C)ategory
                CT) Category and Title CR) Category and Rate
        9- Command Line S)ort book
                T)itle R)ate P)ublisher C)ategory PA)ageCount
        10-Command line Q)uit
        : <user input>

        returns string -> '<user input>'
    """
    commands = '\n 1- Command Line L)oad file\
                \n 2- Command Line A)dd book\
                \n 3- Command Line R)emove book\
                \n 4- Command Line F)ind book by title\
                \n 5- Command Line NC) Number of books in a category\
                \n 6- Command Line CA) Categories for an author\
                \n 7- Command Line CB) Categories for a book title\
                \n 8- Command Line G)et book\
                \n\t R)ate A)uthor P)ublisher C)ategory\
                \n\t CT) Category and Title CR) Category and Rate\
                \n 9- Command Line S)ort book\
                \n\t T)itle R)ate P)ublisher C)ategory PA)ageCount\
                \n 10- Command line Q)uit\
                \n : '

    return input(commands)

#-------------------- MAIN LOOP ---------------------#

book_dictionary = ''

running = True
while running == True:

    userIn = prompt().upper()
    
    if userIn not in command:
        print(NSC)
    
    # Command 10 - Aashna Verma 101225434
    elif userIn == 'Q':
        running = command['Q'] 
    
    else:
        c = command[userIn]

        # Command 1 - Liana Cabalit 101233041
        if userIn == 'L':
                filename = input(c[0])
                if os.path.isfile(filename) == False:       # imported function that determines whether the file exists
                    print('No file loaded')
                else:
                    book_dictionary = c[1](filename)
                    print(filename, 'has been loaded :)')
        
        elif book_dictionary == '':
            print('No file loaded')

        # Command 2 - Liana Cabalit 101233041
        elif userIn == 'A':
                c[1](book_dictionary, c[0]())

        # Command 3 - Liana Cabalit 101233041
        elif userIn == 'R':
                c[2](book_dictionary, input(c[0]), input(c[1]))

        # Command 8 - Alvin Muguluma 101219375
        elif userIn == 'G':
            
            userIn2 = input(c[0]).upper()               
            
            if userIn2 not in c[1]:                    
                print(NSC)
            
            elif userIn2 in ['CT','CR']:                
                d = c[1][userIn2]
                i1 = input(d[0])                        
                i2 = input(d[1])             
                
                if userIn2 == 'CR' and i2.isdigit():    
                    i2 = int(i2)
                
                d[2](book_dictionary,i1,i2)

            else:                                    
                d = c[1][userIn2]                             
                i1 = input(d[0])                        

                if userIn2 == 'R' and i1.isdigit():     
                    i1 = int(i1)
                
                d[1](book_dictionary,i1)           

        # Commands 9 - Koralie Mokam 101221527
        elif userIn == 'S':
            
            userIn2 = input(c[0]).upper()                             
            
            if userIn2 not in c[1]:               
                print(NSC)
        
            else:                       
                d = c[1][userIn2]

                if userIn2 == 'R':
                    userIn3 = input(d[0]).upper()

                    if userIn3 in d[1]:
                        d[1][userIn3](book_dictionary)
                    else:
                        print(NSC)
                        
                else: 
                    d(book_dictionary)

        # Commands 4, 5, 6, 7 - Liana Cabalit 101233041 and Aashna Verma 101225434
        else:
            c[1](book_dictionary, input(c[0]))

print('Thank you! See you soon!\n')