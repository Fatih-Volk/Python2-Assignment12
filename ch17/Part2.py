#### Part 2 of Assignment 12 File
#### Mig. M.
#### 12/11/2021
#### Assignment 12
#### Short summary:  Part 2 of 3
def part2():
    import sqlite3

    connection = sqlite3.connect('books.db')

    import pandas as pd

    pd.options.display.max_columns = 10

    pd.read_sql('SELECT * FROM authors', connection, index_col=['id'])

    pd.read_sql('SELECT * FROM titles', connection)

    df = pd.read_sql('SELECT * FROM author_ISBN', connection)

    df.head()

    #### 17.2.2 down here

    pd.read_sql('SELECT first, last FROM authors', connection)

    #### 17.2.3 down here

    pd.read_sql("""SELECT title, edition, copyright FROM titles WHERE copyright > '2016'""", connection)

    pd.read_sql("""SELECT id, first, last FROM authors WHERE last LIKE 'D%'""", connection, index_col=['id'])

    pd.read_sql("""SELECT id, first, last FROM authors WHERE first LIKE '_b%'""", connection, index_col=['id'])

    pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)

    pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last, first""", connection, index_col=['id'])

    pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last DESC, first ASC""", connection, index_col=['id'])

    pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY title""", connection)

    #### start of 17.2.5

    pd.read_sql("""SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER BY last, first""", connection).head()

    #### start of 17.2.6

    cursor = connection.cursor()

    cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Sue', 'Red')""")

    pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])

    #### start of 17.2.7

    cursor = cursor.execute("""UPDATE authors SET last='Black' WHERE last='Red' AND first='Sue'""")

    cursor.rowcount

    pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])

    ### start of 17.2.8

    cursor = cursor.execute('DELETE FROM authors WHERE id=6')

    cursor.rowcount

    pd.read_sql('SELECT id,first,last FROM authors', connection, index_col=['id'])

    #### end, self check for section 17.2

    pd.read_sql("""SELECT title, edition FROM titles ORDER BY edition DESC""", connection).head(3)

    pd.read_sql("""SELECT * FROM authors WHERE first LIKE 'A%'""", connection)

    pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title NOT LIKE '%How to Program' ORDER BY title""", connection)

    #### END of 17.2
def part3():
    import sqlite3

    connection = sqlite3.connect('books.db')

    import pandas as pd

    pd.options.display.max_columns = 10

    pd.read_sql('SELECT first, last FROM authors', connection)  #### part A

    pd.read_sql('SELECT last, first FROM titles', connection)   #### part B

    pd.read_sql("""SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER BY last, first""", connection) #### part C???

    cursor = connection.cursor()
    
    cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Sue', 'Red')""")  #### Part D

    cursor = cursor.execute("""INSERT INTO titles WHERE last='Red' AND first='Sue'""")  #### PART #


#part2()
#part3()