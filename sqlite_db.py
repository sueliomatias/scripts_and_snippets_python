import sqlite3

# conecta ao banco de dados (cria o banco de dados se não existir)
conn = sqlite3.connect('example.db')

# cria uma tabela no banco de dados
conn.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY,
             name TEXT,
             email TEXT)''')

# inserir dados na tabela
conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('John Doe', 'john@example.com'))
conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Jane Smith', 'jane@example.com'))

# confirma as alterações
conn.commit()

# consulta os dados da tabela
cursor = conn.execute("SELECT * FROM users")
print(cursor)
for row in cursor:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

# fecha a conexão com o banco de dados
conn.close()