class bancodedados():

    def criando_tabela(self,coluna,campo,valor):

        import sqlite3
        conn = sqlite3.connect(':memory:')
        c = conn.cursor()
        with open('criando_tabela.sql', 'r') as content_file:
            content = content_file.read()
            c.execute(content)
        
        with open('copiando_tabela.sql', 'r') as content_file:
            content = content_file.read()
            c.execute(content)

        c.execute('SELECT * teste WHERE name = '+coluna)
        for row in c.fetchall():
           notnull = row[3]
           pk = row[5]

        conn.commit()
        conn.close()

        if campo == "pk":
            print (pk == valor)
            return pk == valor
        elif campo == "notnull":
            print (notnull == valor)
            return notnull == valor