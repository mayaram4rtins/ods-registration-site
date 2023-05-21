import mysql.connector
from mysql.connector import errorcode

print("Conectando ao MySQL...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `ods-registration-site`;")

cursor.execute("CREATE DATABASE `ods-registration-site`;")

cursor.execute("USE `ods-registration-site`;")

# criando tabelas
TABLES = {}
TABLES['Users'] = ('''
      CREATE TABLE `cadastro_usuario` (
      `id_user` int(10) NOT NULL AUTO_INCREMENT,
      `nome` varchar(100) NOT NULL,
      `email` varchar(50) NOT NULL,
      `senha` varchar(14) NOT NULL,
      `telefone` bigint NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Projetos'] = ('''
      CREATE TABLE `cadastro_projetos` (
      `id_proj` int(10) NOT NULL AUTO_INCREMENT,
      `nome_projeto` varchar(100) NOT NULL,
      `id_user` int(10) NOT NULL,
      `descricao` varchar(100) NOT NULL,
      `ods` varchar(14) NOT NULL,
      `telefone` bigint NOT NULL,
      `data_cadastro` date NOT NULL,
      `status_projeto` varchar(10) NOT NULL,
      `tag` varchart (15) NOT NULL,
      PRIMARY KEY (`id_proj`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

cursor.execute("alter table `cadastro_projetos` add foreign key (id_user) references User(id_user)")

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('Ok, tabela criada!')

'''
# inserindo usuarios
usuario_sql = 'INSERT INTO usuario (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
      ("Bruno Divino", "BD", "alohomora"),
      ("Camila Ferreira", "Mila", "paozinho"),
      ("Guilherme Louro", "Cake", "python_eh_vida")
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from jogoteca.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)'
jogos = [
      ('Tetris', 'Puzzle', 'Atari'),
      ('God of War', 'Hack n Slash', 'PS2'),
      ('Mortal Kombat', 'Luta', 'PS2'),
      ('Valorant', 'FPS', 'PC'),
      ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
      ('Need for Speed', 'Corrida', 'PS2'),
]
cursor.executemany(jogos_sql, jogos)

cursor.execute('select * from jogoteca.jogos')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])
'''

# commitando se não nada tem efeito

conn.commit()

cursor.close()
conn.close()