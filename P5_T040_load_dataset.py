# T040 - 07/12/2021 Version 1.0
# Liana Cabalit 101233041, Alvin Muguluma 101219375, Koralie Mokam 101221527, Aashna Verma 101225434

import csv

def load_dataset(filename: str) -> dict[str, list[dict]]:
    """ Returns a dictionary of generes with a list books containing the same genere and their specifications
        based on the csv filename

        >>>  book_category_dictionary_list('Google_Books_Dataset.csv')
        {'Fiction': [
            {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 
            'author': 'Barbara Allan', 
            'rating': 3.3, 
            'publisher': 'Kensington Publishing Corp.', 
            'page_count': 288, 
            'language': 'English'},
            etc ...
            ],
         'Comics': [
            {'title': 'Deadpool Kills the Marvel Universe', 
            'author': 'Cullen Bunn', 
            'rating': 4.2, 
            'publisher': 'Marvel Entertainment', 
            'page_count': 96, 
            'language': 'English'},
            etc ...
            ],
            etc ... 
        }

        >>>  book_category_dictionary_list('Library_Dataset.csv')
        {'Superhero': [
            {'title': "Renegades", 
            'author': 'Marissa Meyer', 
            'rating': 4.1, 
            'publisher': 'Feiwel & Friends', 
            'page_count': 592, 
            'language': 'English'},
            etc ...
            ],
         'Comics': [
            {'title': 'Thea Stilton and the Mystery in Paris', 
            'author': 'Tea Stilton', 
            'rating': 4.4, 
            'publisher': 'Scholastic Inc', 
            'page_count': 96, 
            'language': 'English'},
            etc ...
            ],
            etc ... 
        }
    """
    infile = open(filename, 'r')
    csvreader = csv.DictReader(infile)                          # opens filename and reads it as a dictionary

    book_dictionary = {}                                        # intiates an empty dictionary to contain books seperated by genere
    books = []                                                  # intiates an ampty list to contain books

    for row in csvreader:                                       # iterates through every row in csvreader
        del row['']                                             # gets rid of the empty keys
        row.update({"page_count":int(row.get("page_count"))})   # turns page_count in every row into a integer
        if row.get("rating") == '':
            row.update({"rating":0.0})                            # if rating is empty then turn rating into 0
        else:
            row.update({"rating":float(row.get("rating"))})     # else turns rating into a float

        books.append(row)                                       # adds the rows to the list books 
        book_dictionary.update({row.get('generes'):[]})         # updates book_dictionary to the value of genere from row to an empty list

    infile.close()
    
    for genere in list(book_dictionary.keys()):                 # for evey genere in book_dictionary
        same_generes = []                                       # initiates and empty list to contain all teh books with the same generes
        for book in books:                                      # goes through every book in books            
            if genere == book.get('generes'):                   # if the genere is the same as the the key 'genere' in the book
                del book['generes']                             # delete the key 'generes' from the book
                if book not in same_generes:
                    same_generes.append(book)                   # add the book to same_generes
        book_dictionary.update({genere:same_generes})           # update the key genere in the book_dictionary to a list of the same generes

    return book_dictionary

load_dataset('Google_Books_Dataset.csv')

