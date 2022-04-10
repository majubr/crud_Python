import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute ('CREATE TABLE IF NOT EXISTS clientes ('
                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'nome TEXT,'
                'peso REAL'
                ')')

#cursor.execute('INSERT INTO clientes (nome,peso) VALUES ("Marcelo Juliano", 100)')
#cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#               {'id': None, 'nome':'Ana','peso': 35})

#cursor.execute ('UPDATE clientes SET nome= :nome WHERE id=:id',
#                {'nome':'Joana','id':2})

cursor.execute ('DELETE  FROM clientes WHERE id=:id',
                {'nome': 'Joana','id':2}
                )
conexao.commit()

cursor.execute ('SELECT * FROM clientes')

cursor.execute ('SELECT nome, peso FROM clientes WHERE peso >:peso',
                {'peso': 24}
                )

for linha in cursor.fetchall():
    nome, peso = linha
    print(nome, peso)




cursor.close()
conexao.close()



