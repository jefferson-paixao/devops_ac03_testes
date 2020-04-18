class bancodedados():

    def criando_tabela(self):

        import sqlite3
        conn = sqlite3.connect(':memory:')
        c = conn.cursor()
        with open('criando_tabela.sql', 'r') as content_file:
            content = content_file.read()
            c.execute(content)

        c.execute("INSERT INTO ac3 VALUES (1, 'Jefferson', 'jeffersonwilliam12@hotmail.com')")

        c.execute('''SELECT * FROM ac3''')

        for row in c.fetchall():
            print(row)

        conn.commit()
        conn.close()

        return 1