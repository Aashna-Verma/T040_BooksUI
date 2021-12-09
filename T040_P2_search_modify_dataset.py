# T040 - 07/12/2021 Version 1.0
# Liana Cabalit 101233041, Alvin Muguluma 101219375, Koralie Mokam 101221527, Aashna Verma 101225434

# By Liana Cabalit 101233041, Alvin Muguluma 101219375, Koralie Mokam 101221527, Aashna Verma 101225434
def dictionary_organizer(dictionary: dict, header: str) -> dict[str, list[dict]]:
    """ Returns a dictionary of a header with a list books containing the same headers and their specifications
        based on a dictionary

        >>> dictionary_organizer(book_data_dictionary, 'author')
        {'Barbara Allan': [
            {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 
            'author': 'Barbara Allan', 
            'rating': 3.3, 
            'publisher': 'Kensington Publishing Corp.', 
            'page_count': 288, 
            'language': 'English', 
            'generes': 'Fiction'},
            etc ... 
            ], 
        'Peter V. Brett': [
            {'title': 'The Painted Man (The Demon Cycle, Book 1)', 
            'author': 'Peter V. Brett', 
            'rating': 4.5, 
            'publisher': 'HarperCollins UK', 
            'page_count': 544, 
            'language': 'English', 
            'generes': 'Fiction'},
            etc ...
            ],
        etc ...
        }

        >>>  dictionary_organizer(book_data_dictionary, 'generes')
        {'Fiction': [
            {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 
            'author': 'Barbara Allan', 
            'rating': 3.3, 
            'publisher': 'Kensington Publishing Corp.', 
            'page_count': 288,
            'language': 'English'
            'generes' : 'Fiction',},
            etc ...
            ],
         'Comics': [
            {'title': 'Deadpool Kills the Marvel Universe', 
            'author': 'Cullen Bunn', 
            'rating': 4.2, 
            'publisher': 'Marvel Entertainment', 
            'page_count': 96, 
            'language': 'English',
            'generes' : 'Comics'},
            etc ...
            ],
        etc ... 
        }
    """
    book_dictionary = {}                                                # initiates an empty dictionary to contain books seperated by header
    books = []                                                          # initiates an empty dictionary to contain a list of all the books    
    
    for genere in dictionary:                                           
        for book in dictionary.get(genere):                             
            book.update({'generes':genere})                             # adds a key called 'generes' in every book and assignes it the genere that it was origionally a part of
            books.append(book)                                          # adds the book to the list books

    for row in books:                                                   
        if row.get(header) not in list(book_dictionary.keys()):         # if the key header in a row is not in key in the dictionary book_dictionary ...
            same_headers = []                                           # an empty header is created to store books that have the same header
            for row2 in books:                                          
                if row.get(header) == row2.get(header):                 # if the value of header from row1 is the same as the one in row2
                    same_headers.append(row2)                           # add all of row2 to the list same_headers
            book_dictionary.update({row.get(header):same_headers})      # update book_dictionary with the value of the header from row2 annd assign it to the list same_headers

    return book_dictionary

# Function 1 - Aashna Verma 101225434
def print_dictionary_category(dictionary: dict, genere: str) -> int:
    """ Returns the number of items with the same genere in a dictionary
        Prints how many books are in a category and provides the details of each book

        >>> print_dictionary_category(book_data_dictionary, 'Fiction')
        The genere Fiction has 39 books. This is the list of books in the genere Fiction:
        Book #1
                title: Antiques Roadkill: A Trash 'n' Treasures Mystery
                author: Barbara Allan
                rating: 3.3
                publisher: Kensington Publishing Corp.
                page_count: 288
                language: English
        Book #2
        etc...
        return int -> 39

        >>> print_dictionary_category(book_data_dictionary, 'Comics')
        The genere Comics has 7 books. This is the list of books in the genere Comics:
        Book #1
                title: Deadpool Kills the Marvel Universe
                author: Cullen Bunn
                rating: 4.2
                publisher: Marvel Entertainment
                page_count: 96
                language: English
        Book #2
        etc ...
        return int -> 7

        >>> print_dictionary_category(book_data_dictionary, 'Comic')
        The genere Comic was not found
        returns None
    """

    if genere not in dictionary:
        print("The genere " + genere + " was not found")
    
    else:
        amount = len(dictionary.get(genere))
        print("The genere {0} has {1} books. This is the list of books in the genere {0}:".format(genere,amount))
        number = 1
        for book in dictionary.get(genere):
            print("Book #" + str(number))
            for b in book:
                print('\t' , b , ": " , book.get(b), sep = '')
            number += 1   
        return amount

# Function 2 - Liana Cabalit 101233041
def add_book(dictionary: str, values: tuple) -> dict:
    """ Returns the updated dictionary with the new book, given a dictionary and a tuple (values) containing seven values in the 
        order of: (title, author, rating, publisher, page_count, generes, language) 
        Prints a message stating whether or not the book was successfully added to the dictionary.
        
        >>> add_book(load_dataset('Google_Books_Dataset.csv'), ("The Cruel Prince", "Holly Black","4","Little Brown","370","Fantasy","English"))
        The book has been added correctly!
        ... Returns the dictionary organized by category, updated with the new book.
        >>> add_book(load_dataset('Google_Books_Dataset.csv'), ("Little Women", "Louisa May Alcott","4","Penguin","464","Classics","English"))
        The book has been added correctly!
        ... Returns the dictionary organized by category, updated with the new book.
        >>> add_book(load_dataset('Google_Books_Dataset.csv'), ("The Boy in the Striped Pajamas", "John Boyne",4,"Ember",216,"Historical Fiction","English"))
        The book has been added correctly!
        ... Returns the dictionary organized by category, updated with the new genere and book.
    """   
    (title, author, rating, publisher, page_count, generes, language) = values                          # assigns each value in the tuple a variable name

    partition = rating.partition('.')

    if (partition[0].isdigit() or partition[0] == '') and (partition[1] == '.' or partition[1] == '') and (partition[2].isdigit() or partition[2] == '') and page_count.isdigit():
        new_book = {'title':title, 'author':author, 'rating':float(rating), 'publisher':publisher,      # creates a dict with the new book's information
                    'page_count':int(page_count), 'language':language} 

        if generes not in dictionary.keys():                                                            # if the book is of a new genere adds another key in the dictionary
            dictionary[generes] = []  

        dictionary[generes].append(new_book)                                                            # adds the new book's info as a the key's value
                                                                       
        print("The book has been added correctly!")
    else:
        print("There was an error adding the book!")  

    return dictionary

# Function 3 - Koralie Mokam 101221527
def remove_book(dictionary: dict, title: str, category: str) -> dict:
    """ Returns an updated dictionary that removes the book that has the title and category given in the indicated dictionary
        Prints a message stating if the book has been removed or not
    
        >>>remove_book(load_dataset('Google_Books_Dataset.csv'), "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'Fiction')
        The book has been removed correctly
        {'Fiction': [{'title': 'The Painted Man (The Demon Cycle, Book 1)',
        'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK',
        'page_count': 544, 'language': 'English'}, 
        {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson',
        'rating': 4.8, 'publisher': 'Tor Books', 'page_count': 226, 'language': 'English'},
        {another book}
        ...etc]}
        
        >>>remove_book(load_dataset('Google_Books_Dataset.csv'), "Deadpool Kills the Marvel Universe", 'Fiction')
        There was an error removing the book. Book not found.
        ...Returns the exact same dictionnary from load_dataset('Google_Books_Dataset.csv')
        
        >>>remove_book(load_dataset('Google_Books_Dataset.csv'), "The Painted Man (The Demon Cycle, Book 1), 'Fiction'")
        The book has been removed correctly
        {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288, 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'page_count': 226, 'language': 'English'},...etc]}     
    """

    if category not in dictionary.keys():
        print('There was an error removing the book. Category not found.')
    else:
        books = dictionary.get(category)   
        for book in books: 
            if book.get('title')== title:
                books.remove(book)
                print('The book has been removed correctly')
                return dictionary
        print('There was an error removing the book. Book not found.')  
    return dictionary

# Function 4 - Alvin Muguluma 101219375
def get_books_by_rate(dictionary:dict, rate:int) -> dict[str, list[dict]]:
    """ Returns a dictionary of the retrieved books in a range of a given rate 
        Prints the details of the books in the range

        >>>get_books_by_rate(4,'Google_Books_Dataset.csv')
        Book # 1
        title: The Painted Man (The Demon Cycle, Book 1)
        author: Peter V. Brett
        rating: 4.5
        publisher: HarperCollins UK
        page_count: 544
        generes: Fiction
        language: English
            
        ....etc
        {'value':[
        {'title': 'The Painted Man (The Demon Cycle, Book 1)', 
        'author': 'Peter V. Brett', 
        'rating': 4.5, 
        'publisher': 'HarperCollins UK', 
        'page_count': 544, 
        'generes': 'Fiction', 
        'language': 'English'},etc...
            ]
        }
        
        >>>get_books_by_rate(5,'Google_Books_Dataset.csv')
        Book # 1
        title: Final Option: 'The best one yet'
        author: Clive Cussler
        rating: 5.0
        publisher: Penguin UK
        page_count: 400
        generes: Fiction
        language: English
            
        ....etc
        {'value': [
        {'title': "Final Option: 'The best one yet'", 
        'author': 'Clive Cussler', 
        'rating': 5.0, 
        'publisher': 'Penguin UK',
        'page_count': 400, 
        'generes': 'Fiction', 
        'language': 'English'},etc..
      ]
    }
    """
    if str(rate).isdigit() == False:
        print('Rate should be an integer')
    else:   
        num = 1
        books = []
        for genere in dictionary.keys():                    
            for book in dictionary.get(genere):                                     
                rating = book.get('rating') 
                book.update({'generes':genere}) 
                if rating != None and (rating < (rate+1)//1) and (rating >= (rate//1)): 
                    books.append(book)
                    print('Book #', num)    
                    num += 1
                    for i in book:                                  
                        print('\t'+ i + ': ' + str(book.get(i)))    
            
        return_dict = {'value':books}
        return return_dict
  
# Function 5 - Aashna Verma 101225434
def find_books_by_title(dictionary: dict, title: str) -> bool:
    """ Returns if a book is in a dictionary based on it's title
        Prints if the books has been found or not

        >>> find_books_by_title(book_data_dictionary, 'The Mysterious Affair at Styles')
        The book has been found :)
        returns boolean -> True
        
        >>> find_books_by_title(book_data_dictionary, 'The Mysterious')
        The book has NOT been found :(
        returns boolean -> False
    """
    for genere in dictionary.values():  
        for book in genere:
            if book.get('title') == title:
                print("The book has been found :)")
                return True

    print("The book has NOT been found :(")
    return False

# Function 6 - Liana Cabalit 101233041
def get_books_by_author(dictionary:dict, author: str) -> list:
    """ Returns a list containing the author's book titles given a dictionary and author
        Prints out each title in a numbered order.
        
        >>> get_books_by_author(load_dataset('Google_Books_Dataset.csv'), 'Agatha Christie')
        The author "Agatha Christie" has published the following books:
        1 - The Red Signal: An Agatha Christie Short Story
        2 - And Then There Were None
        3 - The Mysterious Affair at Styles
        ... Returns: ['And Then There Were None', 'The Red Signal: An Agatha Christie Short Story', 'The Mysterious Affair at Styles']
        
        >>> get_books_by_author(load_dataset('Google_Books_Dataset.csv'), 'Barbara Allan')
        The author "Barbara Allan" has published the following books:
        1 - Antiques Roadkill: A Trash 'n' Treasures Mystery
        2 - Antiques Con
        3 - Antiques Chop
        4 - Antiques Knock-Off
        ... Returns: ["Antiques Roadkill: A Trash 'n' Treasures Mystery", 'Antiques Knock-Off', 'Antiques Chop', 'Antiques Con']
        
        >>> get_books_by_author(load_dataset('Google_Books_Dataset.csv'), 'Madeline Miller')
        Author "Madeline Miller" not found.
        ... Returns: [None]
    
    """
    dictionary = dictionary_organizer(dictionary, 'author')
    if author not in dictionary.keys():
        print('Author "' + author + '" not found.')
        titles = [None]
    else: 
        print('The author "' + author + '" has published the following books:')                 
        books = dictionary.get(author)                                                  
        titles = []                                                                     
        for book in books:                                                              
            title = book.get('title')                                                  
            if title not in titles:                                                     
                titles += [title]                                               
        number = 1                                                                      
        for name in titles:
            print (str(number) + " - " + name)
            number += 1 

    return titles

# Function 7 - Koralie Mokam 101221527  
def get_books_by_publisher(dictionary: dict, publisher:str)-> list:
    """ Returns a list of book titles for the given publisher’s name
        Prints the books publishedd
    
        >>> get_books_by_publisher(load_dataset('Google_Books_Dataset.csv'), 'AMACOM')
        The publisher "AMACOM" has published the following books:
        1- Personal Success (The Brian Tracy Success Library)
        2- Management (The Brian Tracy Success Library)
        3- Marketing (The Brian Tracy Success Library)
        4- The Essentials of Finance and Accounting for Nonfinancial Managers
        5- Business Strategy (The Brian Tracy Success Library)
        ['Personal Success (The Brian Tracy Success Library)', 'Management (The Brian Tracy Success Library)', 'Marketing (The Brian Tracy Success Library)', 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'Business Strategy (The Brian Tracy Success Library)']
        
        >>> get_books_by_publisher(load_dataset('Google_Books_Dataset.csv'), 'Tor Books')
        The publisher "Tor Books" has published the following books:
        1- Mistborn Trilogy: The Final Empire, The Well of Ascension, The Hero of Ages
        2- Edgedancer: From the Stormlight Archive
        ['Mistborn Trilogy: The Final Empire, The Well of Ascension, The Hero of Ages', 'Edgedancer: From the Stormlight Archive']
        
        >>>get_books_by_publisher('DC', 'Google_Books_Dataset.csv')
        The publisher "DC" has published the following books:
        1- Young Justice Vol. 1
        2- The Joker
        ['Young Justice Vol. 1', 'The Joker']
    """
    dictionary = dictionary_organizer(dictionary, 'publisher') 
    
    if publisher not in dictionary.keys():
        print('Publisher "' + publisher + '" not found.')
        titles = [None]  
    else:
        print('The publisher "' + publisher + '" has published the following books:')
        books = dictionary.get(publisher) 
        titles = []
        for book in books:                             
            title = book.get('title')
            if title not in titles:
                titles += [title]                      
        counter = 1                                     
        for title in titles:                           
            print (str(counter) + "- " + title)          
            counter += 1                                  
    
    return titles
                     
# Function 8 - Alvin Muguluma 101219375
def check_category_and_title(dictionary:dict, category:str, title:str,) -> bool:
    """ Returns if the title is in a given category from a dictionary
        Prints if a category has the title
   
    >>>check_category_and_title('Thrillers','Bring M Back','Google_Books_Dataset.csv')
    The category Thrillers does not have the book title Bring M Back
    False
    
    >>>check_category_and_title('Thrillers','Bring Me Back','Google_Books_Dataset.csv')
    The category Thrillers has the book title Bring Me Back
    True
    
    """ 
    if category not in dictionary.keys():
        print(category, 'not found')
    else:
        book_category = dictionary.get(category)                
        a = 0                                                   
        for book in book_category:                              
            title_1 = book.get('title')
            if title_1 == title:                                
                print("The category",category,"has the book title",title) 
                a = 1                                           
                return True                                     
        if a != 1:                                              
            print("The category",category,"does not have the book title",title) 
            return False                                        
  
# Function 9 - Aashna Verma 101225434
def all_categories_for_book_title(dictionary: dict, title: str) -> list:
    """ Returns a list of generes for given title in given dictionary
        Prints all the categories of a book

        >>> all_categories_for_book_title(csvreader, "A Feast for Crows (A Song of Ice and Fire, Book 4)")
        The book title A Feast for Crows (A Song of Ice and Fire, Book 4) has the following genere(s):
                1 - Fiction
                2 - Fantasy
                3 - Adventure
                4 - Epic
        returns list -> ['Fiction', 'Fantasy', 'Adventure', 'Epic']

        >>> all_categories_for_book_title(book_data_dictionary, "Little Girl Lost: A Lucy Black Thriller")
        The book title Little Girl Lost: A Lucy Black Thriller has the following genere(s):
                1 - Fiction
                2 - Thrillers
                3 - Mystery
        returns list -> ['Fiction', 'Thrillers', 'Mystery']

        >>> all_categories_for_book_title(book_data_dictionary, "A (A Song of Ice and Fire, Book 4)")
        There is no book found with the title A Feast for Crows (A Song of Ice an Fire, Book 4)
        returns list -> None
    """

    generes = [] 
    num = 1

    for genere in dictionary:
        for book in dictionary.get(genere):                        
            if book.get('title') == title:                      
                if num == 1:
                    print("The book title " + title + " has the following genere(s):")
                generes.append(genere)  
                print( "\t" + str(num) , genere, sep= ' - ')
                num += 1

    if num == 1:                                                    
        print("There is no book found with the title " + title)
        return None

    return generes
 
# Function 10 - Liana Cabalit 101233041
def get_books_by_category(dictionary:dict, category: str) -> list:
    """ Returns a list containing the book titles from a given dictionary and category, 
        Prints out each title in a numbered order.
    
        >>> get_books_by_category(load_dataset('Google_Books_Dataset.csv'), 'Adventure')
        The category "Adventure" has  the following books:
        1 - Sword of Destiny: Witcher 2: Tales of the Witcher
        2 - A Feast for Crows (A Song of Ice and Fire, Book 4)
        3 - After Anna
        4 - The Way Of Shadows: Book 1 of the Night Angel
        5 - A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
        6 - Edgedancer: From the Stormlight Archive
        7 - The Malady and Other Stories: An Andrzej Sapkowski Sampler
        ... Returns: ['Sword of Destiny: Witcher 2: Tales of the Witcher', 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'After Anna', 'The Way Of Shadows: Book 1 of the Night Angel', 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'Edgedancer: From the Stormlight Archive', 'The Malady and Other Stories: An Andrzej Sapkowski Sampler']
        
        >>> get_books_by_category(load_dataset('Google_Books_Dataset.csv'), 'Comics')
        The category "Comics" has  the following books:
        1 - Deadpool Kills the Marvel Universe
        2 - Young Justice Vol. 1
        3 - Ultimate Spider-Man Vol. 11: Carnage
        4 - Immortal Hulk Vol. 1: Or Is He Both?
        5 - Watchmen (2019 Edition)
        6 - The Joker
        7 - Venomized
        ... Returns: ['Deadpool Kills the Marvel Universe', 'Young Justice Vol. 1', 'Ultimate Spider-Man Vol. 11: Carnage', 'Immortal Hulk Vol. 1: Or Is He Both?', 'Watchmen (2019 Edition)', 'The Joker', 'Venomized']
        
        >>> get_books_by_category(load_dataset('Google_Books_Dataset.csv'), 'Romance')
        "Romance" category not found.
        ... Returns: [None]
    """
    
    if category not in dictionary.keys():                                              
        print('"' + category + '" category not found.')                                 
        booktitles = [None]                                                           
    else:
        print('The category "' + category + '" has  the following books:')
        books = dictionary.get(category)                                                
        number = 1                                                                      
        booktitles = []                                                                 
        for book in books:                                                              
            print (str(number) + " - " + book.get('title'))                                 
            booktitles += [book.get('title')]                                           
            number += 1                                                                 
            
    return booktitles 
     
# Function 11 - Koralie Mokam 101221527
def get_book_by_category_and_rate(dictionary: dict, category:str, rate: int)-> list:
    """ Returns a list of book titles in a dictionary for the given category and rate interval
        Prints out each book title in a numbered order.
    
        >>> get_book_by_category_and_rate(load_dataset('Google_Books_Dataset.csv'), "Aventure", 4)
        The category “Adventure” and rate 4 has the following books:
        1- Sword of Destiny: Witcher 2: Tales of the Witcher
        2- A Feast for Crows (A Song of Ice and Fire, Book 4)
        3- After Anna
        4- The Way Of Shadows: Book 1 of the Night Angel
        5- A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, 
        A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
        6- Edgedancer: From the Stormlight Archive
        7- The Malady and Other Stories: An Andrzej Sapkowski Sampler
        ['Sword of Destiny: Witcher 2: Tales of the Witcher', 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'After Anna', 'The Way Of Shadows: Book 1 of the Night Angel', 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'Edgedancer: From the Stormlight Archive', 'The Malady and Other Stories: An Andrzej Sapkowski Sampler']
        
        >>> get_book_by_category_and_rate(load_dataset('Google_Books_Dataset.csv'), "Fiction", 1)
        The category "Fiction" and rate 1 has the following books:
        []
        
        >>> get_book_by_category_and_rate(load_dataset('Google_Books_Dataset.csv'), "Mystery", 3)
        The category "Mystery" and rate 3 has the following books:
        1 - Antiques Roadkill: A Trash 'n' Treasures Mystery
        ["Antiques Roadkill: A Trash 'n' Treasures Mystery"]
    """

    if str(rate).isdigit() == False:
        print('Rate should be an integer')
    else:
        if category not in dictionary.keys():
            print(category, 'not found')
        else:
            print('The category "' + category + '" and rate ' + str(rate) + ' has the following books:')    
            counter = 1                                                                                     
            titles = []                                                                                     
            for book in dictionary.get(category):                                                           
                if type(book.get('rating')) == float and int(book.get('rating')) == rate:
                    print (str(counter) + " - " + book.get('title'))                             
                    titles += [book.get('title')]              
                    counter += 1 
            return titles    

# Function 12 - Alvin Muguluma 101219375
def get_author_categories(dictionary:dict, author:str) -> list:
    """ Returns a list of categories for the given author
        Prints the categories in numbered order

        >>>get_author_categories('Barbara Allan','Google_Books_Dataset.csv')
        The author Barbara Allan has published books under the following categories:
        1 - Mystery
        2 - Fiction
        3 - Detective
        ['Mystery', 'Fiction', 'Detective']
    
        >>>get_author_categories('Agatha Christie','Google_Books_Dataset.csv')
        The author Agatha Christie has published books under the following categories:
        1 - Horror
        2 - Traditional
        3 - Thrillers
        4 - Detective
        5 - Mystery
        6 - Classics
        7 - Fiction
        ['Horror', 'Traditional', 'Thrillers', 'Detective', 'Mystery', 'Classics', 'Fiction']
    """ 
    author_list = []                                
    for genere in dictionary.keys():                
        for book in dictionary.get(genere):         
            author_1 = book.get('author')           
            if author == author_1:                 
                author_list.append(genere)          
    author_list = set(author_list)                  
    author_list = list(author_list)                 
    
    if len(author_list) == 0:
        print('The author', author, 'was not found.')
    else:
        print ('The author',author,'has published books under the following categories:')   
        for i in range(len(author_list)):                         
            print('\t', (i+1), '-', author_list[i], sep = '')     
        return author_list 