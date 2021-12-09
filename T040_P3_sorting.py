# T040 - 07/12/2021 Version 1.0
# Liana Cabalit 101233041, Alvin Muguluma 101219375, Koralie Mokam 101221527, Aashna Verma 101225434

def turn_to_list(dictionary: dict) -> list:
    """ Returns dictionary as a list

        >>> turn_to_list(dictionary)
        [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288, 'language': 'English', 'generes': 'Fiction'},
         {'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 544, 'language': 'English', 'generes': 'Fiction'}, 
         {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'page_count': 226, 'language': 'English', 'generes': 'Fiction'}, 
         {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'page_count': 400, 'language': 'English', 'generes': 'Fiction'},
         etc...]

         >>> turn_to_list(dictionary)
        [{'title': 'The Cruel Prince', 'author': 'Holly Black', 'rating': 4.09, 'publisher': 'Little Brown', 'page_count': 370, 'language': 'English', 'generes': 'Fantasy'}, 
        {'title': 'The Wicked King', 'author': 'Holly Black', 'rating': 2.85, 'publisher': 'Little Brown', 'page_count': 336, 'language': 'English', 'generes': 'Fantasy'}, 
        {'title': 'The Queen of Nothing', 'author': 'Holly Black', 'rating': 4.35, 'publisher': 'Little Brown', 'page_count': 300, 'language': 'English', 'generes': 'Fantasy'},
        etc...]
    """
    books = []                                                      
    for genere in dictionary.keys():
        for book in dictionary.get(genere):
            book['generes'] = genere                                
            books.append(book)                                     
    
    return books

def book_info_print(books: list):
    """ Prints all the info of each book in books

        >>> book_info_print(books):
        Book # 1
            title - A Feast for Crows (A Song of Ice and Fire, Book 4)
            author - George R.R. Martin
            rating - 4.5
            publisher - HarperCollins UK
            page_count - 864
            language - English
            generes - Fiction

        Book # 2
            title - A Feast for Crows (A Song of Ice and Fire, Book 4)
            author - George R.R. Martin
            rating - 4.5
            publisher - HarperCollins UK
            page_count - 864
            language - English
            generes - Fantasy
        
        Book # etc ...
            etc ...

        >>> book_info_print(books2):
        Book # 1
            title - Aviation handbook
            author - Urwor S'nitemr
            rating - 0.2
            publisher - Wannabe Enginerring inc.
            page_count - 200
            language - English
            generes - Suffering
        
        Book # 2
            title - Basic Python: Torture problems edition 
            author - Urwor S'nitemr
            rating - 0.0
            publisher - Wannabe Enginerring inc.
            page_count - 9999
            language - English
            generes - Suffering
        
        Book #etc ...
            etc ...
    """
    num = 0
    for b in books:
        num += 1
        print('\nBook #', num)
        for k in b:
            print('\t', k, '-', b.get(k))

# Function 1 - Aashna Verma 101225434 
def sort_books_title(dictionary: dict) -> list:
    """ Returns a list of books, aplphabetically ordered by title based on a dictionary
        Prints the specifications of every book 

        >>> sort_books_title(load_dataset('Google_Books_Dataset.csv'))
        Book # 1
            title - A Feast for Crows (A Song of Ice and Fire, Book 4)
            author - George R.R. Martin
            rating - 4.5
            publisher - HarperCollins UK
            page_count - 864
            language - English
            generes - Fiction

        Book # 2
            title - A Feast for Crows (A Song of Ice and Fire, Book 4)
            author - George R.R. Martin
            rating - 4.5
            publisher - HarperCollins UK
            page_count - 864
            language - English
            generes - Fantasy

        Book # 3
            title - A Feast for Crows (A Song of Ice and Fire, Book 4)
            author - George R.R. Martin
            rating - 4.5
            publisher - HarperCollins UK
            page_count - 864
            language - English
            generes - Adventure

        Book #etc
            etc...
        
        returns list -> [{'title': 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 864, 'language': 'English', 'generes': 'Fiction'}, 
        {'title': 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 864, 'language': 'English', 'generes': 'Fantasy'}, 
        {'title': 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 864, 'language': 'English', 'generes': 'Adventure'},
        etc ... ]

        >>> sort_books_title(load_dataset('Textbooks.csv'))
        Book # 1
            title - Aviation handbook
            author - Urwor S'nitemr
            rating - 0.2
            publisher - Wannabe Enginerring inc.
            page_count - 200
            language - English
            generes - Suffering
        
        Book # 2
            title - Basic Python: Torture problems edition 
            author - Urwor S'nitemr
            rating - 0.0
            publisher - Wannabe Enginerring inc.
            page_count - 9999
            language - English
            generes - Suffering
        
        Book #etc
            etc...

        returns list -> [{'title': 'Aviation handbook', 'author': 'Urwor S'nitemr', 'rating': 0.2, 'publisher': 'Wannabe Enginerring inc.', 'page_count': 9999, 'language': 'English', 'generes': 'Suffering'}, 
        {'title': 'Basic Python: Torture problems edition ', 'author': 'Urwor S'nitemr', 'rating': 0.0, 'publisher': 'Wannabe Enginerring inc.', 'page_count': 9999, 'language': 'English', 'generes': 'Suffering'}, 
        etc ...]
    """
    books = turn_to_list(dictionary)
    
    n = len(books)                                                 
    for i in range(len(books)):
        for j in range(0, n - i - 1):
            if books[j].get('title').lower() > books[j+1].get('title').lower():
                books[j], books[j+1] = books[j+1], books[j]
    
    book_info_print(books)                                              

    return books

# Function 2 - Alvin Muguluma 101219375
def sort_books_ascending_rate(dictionary:dict) -> list:
    """ Returns a list of book data given the dictionary where the books are sorted by the rate in ascending order
        Prints the specifications of every book 
        
        >>> sort_books_ascending_rate(load_dataset('Google_Books_Dataset.csv'))
        Book # 1
        title: Antiques Roadkill: A Trash 'n' Treasures Mystery
        author: Barbara Allan
        rating: 3.3
        publisher: Kensington Publishing Corp.
        page_count: 288
        language: English
        generes: Fiction
        etc...
        [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 
        'author': 'Barbara Allan', 
        'rating': 3.3, 
        'publisher': 'Kensington Publishing Corp.', 
        'page_count': 288, 
        'language': 'English', 
        'generes': 'Fiction'}, 
        etc...
        ]
        
        >>> sort_books_ascending_rate(load_dataset('T040_Books.csv'))
        Book # 1
        title: The Kite Runner
        author: Khaled Hosseini
        rating: 1.35
        publisher: Riverhead Books
        page_count: 371
        language: English
        generes: Fiction
        etc...
        [{'title': 'The Kite Runner', 
        'author': 'Khaled Hosseini', 
        'rating': 1.35, 
        'publisher': 'Riverhead Books', 
        'page_count': 371, 
        'language': 'English', 
        'generes': 'Fiction'},
        etc...
        ] 
    """
    books = turn_to_list(dictionary)
    
    n =len(books)
    for i in range(n):                                                     
        for j in range(0, n-i-1):                                          
            if books[j].get('rating') > books[j+1].get('rating'):         
                books[j], books[j+1] = books[j+1], books[j]
                
    book_info_print(books)                                                              
                    
    return books

# Function 3 - Alvin Muguluma 101219375    
def sort_books_descending_rate(dictionary:dict) -> list:
    """ Returns a list of book data given the dictionary where the books are sorted by the rate in descending order
        Prints the specifications of every book
        
        >>> sort_books_descending_rate(load_dataset('Google_Books_Dataset.csv'))
        Book # 1
        title: Final Option: 'The best one yet'
        author: Clive Cussler
        rating: 5.0
        publisher: Penguin UK
        page_count: 400
        language: English
        generes: Fiction
        etc...
        [{'title': "Final Option: 'The best one yet'", 
        'author': 'Clive Cussler', 'rating': 5.0,
        'publisher': 'Penguin UK', 
        'page_count': 400, 
        'language': 'English', 
        'generes': 'Fiction'} etc..
        ]
        
        >>> sort_books_descending_rate(load_dataset('T040_Books.csv'))
        Book # 1
        title: The Song of Achilles
        author: Madeline Miller
        rating: 4.41
        publisher: Ecco
        page_count: 378
        language: English
        generes: Historical Fiction
        etc..
        [{'title': 'The Song of Achilles', 
        'author': 'Madeline Miller', 
        'rating': 4.41, 
        'publisher': 'Ecco', 
        'page_count': 378, 
        'language': 'English', 
        'generes': 'Historical Fiction'},
        etc..
        ]
    """
    books = turn_to_list(dictionary)
    
    n =len(books)
    for i in range(n):                                                      
        for j in range(0, n-i-1):                                           
            if books[j].get('rating') < books[j+1].get('rating'):           
                books[j], books[j+1] = books[j+1], books[j]
                
    book_info_print(books)                                                
                    
    return books

# Function 4 - Liana Cabalit 101233041 
def sort_books_publisher(dictionary: dict) -> list:
    """ Returns a list of books given the dictionary, organized alphabetically by publisher 
        Prints out each book and its details.
        Note: Books with the same publisher are in alphabetical order.

        >>> sort_books_publisher(load_dataset('Google_Books_Dataset.csv'))
        Book #1
        title - Business Strategy (The Brian Tracy Success Library)
        author - Brian Tracy
        rating - None
        publisher - AMACOM
        page_count - 112
        language - English
        generes - Economics

        Book #2
        title - Business Strategy (The Brian Tracy Success Library)
        author - Brian Tracy
        rating - None
        publisher - AMACOM
        page_count - 112
        language - English
        generes - Business

        Book #3
        title - Management (The Brian Tracy Success Library)
        author - Brian Tracy
        rating - None
        publisher - AMACOM
        page_count - 112
        language - English
        generes - Economics
        
        Book #etc
            etc...
        ... Returns: [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': None, 'publisher': 'AMACOM', 'page_count': 112, 'language': 'English', 'generes': 'Economics'}, {'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': None, 'publisher': 'AMACOM', 'page_count': 112, 'language': 'English', 'generes': 'Business'}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': None, 'publisher': 'AMACOM', 'page_count': 112, 'language': 'English', 'generes': 'Economics'}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': None, 'publisher': 'AMACOM', 'page_count': 112, 'language': 'English', 'generes': 'Management'}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': None, 'publisher': 'AMACOM', 'page_count': 112, 'language': 'English', 'generes': 'Economics'}, {'title': 'Personal Success (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': None, 'publisher': 'AMACOM', 'page_count': 112, 'language': 'English', 'generes': 'Economics'}, {'title': 'Personal Success (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': None, 'publisher': 'AMACOM', 'page_count': 112, 'language': 'English', 'generes': 'Business'}, {'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields', 'rating': None, 'publisher': 'AMACOM', 'page_count': 320, 'language': 'English', 'generes': 'Economics'}, {'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields', 'rating': None, 'publisher': 'AMACOM', 'page_count': 320, 'language': 'English', 'generes': 'Business'}, ... {next publisher} ... ]

        >>> sort_books_publisher(load_dataset('T040_Books.csv'))
        Book #1
        title - The Book Thief
        author - Markus Zusak
        rating - 4.38
        publisher - Alfred A. Knopf
        page_count - 552
        language - English
        generes - Historical Fiction

        Book #2
        title - It Ends With Us
        author - Colleen Hoover
        rating - 3.62
        publisher - Atria Books
        page_count - 385
        language - English
        generes - Romance

        Book #3
        title - The Immortal Life of Henrietta Lacks
        author - Rebecca Skloot
        rating - 4.07
        publisher - Broadway Books
        page_count - 370
        language - English
        generes - Biography
            
        Book #etc
            etc...
        ... Returns: [{'title': 'The Book Thief', 'author': 'Markus Zusak', 'rating': 4.38, 'publisher': 'Alfred A. Knopf', 'page_count': 552, 'language': 'English', 'generes': 'Historical Fiction'}, {'title': 'It Ends With Us', 'author': 'Colleen Hoover', 'rating': 3.62, 'publisher': 'Atria Books', 'page_count': 385, 'language': 'English', 'generes': 'Romance'}, {'title': 'The Immortal Life of Henrietta Lacks', 'author': 'Rebecca Skloot', 'rating': 4.07, 'publisher': 'Broadway Books', 'page_count': 370, 'language': 'English', 'generes': 'Biography'}, {'title': 'The Silent Patient', 'author': 'Alex Michaelides', 'rating': 3.52, 'publisher': 'Celadon Books', 'page_count': 325, 'language': 'English', 'generes': 'Thriller'}, ... {next publisher...}]
    """
    books = turn_to_list(dictionary)
    
    n = len(books)
    for i in range(n):                                          
        for j in range(0, n - i - 1):
            if books[j].get('publisher') > books[j+1].get('publisher') or (books[j].get('publisher') == books[j + 1].get('publisher') and books[j].get('title') > books[j + 1].get('title')):
                books[j], books[j+1] = books[j+1], books[j]
                
    book_info_print(books) 
        
    return books
   
# Function 5 - Aashna Verma 101225434 
def sort_books_pageCount(dictionary: dict) -> list:
    """ Returns a list of books in ascending ordered of pagecount based on a dictionary.
        Prints the specifications of every book
        Note: Books with the same page count are in alphabetical order.

        >>> sort_books_pageCount(load_dataset('Google_Books_Dataset.csv'))
        Book # 1
            title - Summary: Think and Grow Rich
            author - Nine99 Innovation Lab
            rating - None
            publisher - Nine99 Innovation Lab (OPC) Pvt Ltd
            page_count - 14
            language - English
            generes - Economics
        
        Book # 2
            title - Summary: Think and Grow Rich
            author - Nine99 Innovation Lab
            rating - None
            publisher - Nine99 Innovation Lab (OPC) Pvt Ltd
            page_count - 14
            language - English
            generes - Business

        Book #etc
            etc...
        
        returns list -> [{'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': None, 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'page_count': 14, 'language': 'English', 'generes': 'Economics'}, 
        {'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': None, 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'page_count': 14, 'language': 'English', 'generes': 'Business'}, 
        etc ...]

        >>> sort_books_pageCount(load_dataset('Textbooks.csv'))
        Book # 1
            title - Calc for idiots
            author - Urwor S'nitemr
            rating - 0.0
            publisher - Wannabe Enginerring inc.
            page_count - 999
            language - English
            generes - Suffering
        
        Book # 2
            title - Circuits: How NOT to blow up 
            author - Urwor S'nitemr
            rating - 0.0
            publisher - Wannabe Enginerring inc.
            page_count - 999
            language - English
            generes - Suffering
        
        Book #etc
            etc...

        returns list -> [{'title': 'Calc for idiots', 'author': 'Urwor S'nitemr', 'rating': 0.0, 'publisher': 'Wannabe Enginerring inc.', 'page_count': 999, 'language': 'English', 'generes': 'Suffering'}, 
        {'title': 'Circuits: How NOT to blow up', 'author': 'Urwor S'nitemr', 'rating': 0.0, 'publisher': 'Wannabe Enginerring inc.', 'page_count': 999, 'language': 'English', 'generes': 'Suffering'}, 
        etc ...]
    """
    books = turn_to_list(dictionary)

    for i in range(len(books)):                                                 
        for j in range(len(books) - i - 1):
            if books[j].get('page_count') > books[j + 1].get('page_count') or (books[j].get('page_count') == books[j + 1].get('page_count') and books[j].get('title') > books[j + 1].get('title')):
                books[j], books[j + 1] = books[j + 1], books[j]
        
    book_info_print(books)                                                       
    
    return books

# Function 6 - Koralie Mokam 101221527
def sort_books_category(dictionary:dict) -> list:
    """ Returns a list with the book data given a dictionary where the books are
        sorted alphabetically by category 
        Note: books with the same category are sorted alphabetically by title

        >>> sort_books_category(load_dataset('Google_Books_Dataset.csv'))
        prints... Book # 1
        title - A Feast for Crows (A Song of Ice and Fire, Book 4)
        author - George R.R. Martin
        rating - 4.5
        publisher - HarperCollins UK
        page_count - 864
        generes - Adventure
        language - English...etc {another prints}
        returns...[{'Adventure': [{'title': 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 
        'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'page_count': 400,
        'generes': 'Adventure', 'language': 'English'}, 
        {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings,
        A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 
        'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 
        'page_count': 864, 'generes': 'Adventure', 'language': 'English'}, {next book}...]
        'Biography': [{'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Garrard Conley', 'rating': 4.0, 'publisher': 'Penguin', 'page_count': 352, 'generes': 'Biography', 'language': 'English'},{next book}...]
        'Next category'...etc
        }]
        
        >>> sort_books_category(load_dataset('T040_Books.csv'))
        prints..Book # 1
        title - The Immortal Life of Henrietta Lacks
        author - Rebecca Skloot
        rating - 4.07
        publisher - Broadway Books
        page_count - 370
        generes - Biography
        language - English... etc {another data}
        returns... [{'Biography': [{'title': 'The Immortal Life of Henrietta Lacks', 'author': 'Rebecca Skloot', 'rating': 4.07, 'publisher': 'Broadway Books', 'page_count': 370, 'generes': 'Biography', 'language': 'English'}], 'Classics': [{'title': 'Little Women', 'author': 'Louisa May Alcott', 'rating': 4.11, 'publisher': 'Signet Classics', 'page_count': 449, 'generes': 'Classics', 'language': 'English'}],
        'Next category'...etc
        }]
    """                                                          
    sortlist = turn_to_list(dictionary)
            
    n =len(sortlist)      
    for i in range(n):                                                   
        for j in range(0, n-i-1):
            if sortlist[j].get('generes') > sortlist[j + 1].get('generes') or (sortlist[j].get('generes') == sortlist[j + 1].get('generes') and sortlist[j].get('title') > sortlist[j + 1].get('title')):
                sortlist[j], sortlist[j + 1] = sortlist[j + 1], sortlist[j]           

    book_info_print(sortlist)                                                      
            
    return sortlist                                                            
