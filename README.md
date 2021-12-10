# T040_BooksUI
*ECOR 1042 Fall 2021 README for [**BooksUI**](https://github.com/AASH800/T040_BooksUI) - Project Version 1.0 - 8/12/2021*  
*Copyright 2021 Aashna Verma, Liana Cabalit, Koralie Mokam and Alvin Muguluma*

## Contact information
Name: Aashna Verma  
Voice: (613)-875-8144  
Email: aashnaverma@cmail.carleton.ca

## Description
This project contains a program that takes a csv file wich
contains a dataset of books. The program then retrieves, removes 
or sorts the books based on the user input and prints statement 
for whichever function the user called.

The project contains 4 python scripts:
>P5_T040_load_dataset.py 
>T040_P2_search_modify_dataset.py 
>T040_P3_sorting.py 
>T040_P2_booksUI.py

## Installation
Python 3.7.4 or later must be installed.
Built-in modules _csv_ and _os_ are used.  
The user-defined modules required can be downloaded [here.](https://github.com/AASH800/T040_BooksUI/archive/refs/heads/main.zip)  
The program must run with the csv file in the same directory. 

## Usage
The module T040_P4_BooksUI.py must be executed in shell in order to utilize the program.
>python T040_P4_BooksUI.py

When prompted with the list of commands below (L, A, R, F, NC, CA, CB, G, S, Q), enter the command of choice.   

**Note:** The first command _must_ be L for to load a file.   
The filename prompted to be entered _must_ be the name of a comma delimited file type saved in the same directory, followed by .csv (e.g. Google_Books_Dataset.csv).  

Follow the program's instructions to complete the analysis.   
After an analysis is completed the prompts below will be redisplayed on the shell.   
Repeat the same steps to excute another analysis or quit the program using the Q command.  
```
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
 10- Command line Q)uit
 : 
```

## Credits
### Aashna Verma  
>print_dictionary_category, find_books_by_title, all_categories_for_book_title, sort_books_title, sort_books_pageCount

### Liana Cabalit  
>add_book, get_books_by_author, get_books_by_category, sort_books_publisher

### Alvin Muguluma  
>get_books_by_rate, check_category_and_title, get_author_categories, sort_books_ascending_rate, sort_books_descending_rate 

### Koralie Mokam  
>remove_book, get_books_by_publisher, get_book_by_category_and_rate, sort_books_category
