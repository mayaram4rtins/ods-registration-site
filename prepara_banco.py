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
      `telefone` bigint NOT NULL,
      `data_cadastro` date NOT NULL,
      `status_projeto` varchar(10) NOT NULL,
      `tag` varchar (15) NOT NULL,
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


# inserindo usuarios
usuario_sql = 'INSERT INTO cadastro_usuario (nome, email, senha, telefone) VALUES (%s, %s, %s, %s)'
usuarios = [
      ("João Profano", "jojopo@hotmail.com", "jojofofo33", "5511987634590"),
      ("Telconir", "teteco_surf@gmali.com", "surfevida54", "5511929387429"),
      ("Yasuo Shigeru", "shigeru_yasuo@yahoo.com.br", "3297yat", "5511912968164")
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from ods-registration-site.cadastro_usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo projetos
projetos_sql = 'INSERT INTO jogos (nome_projeto, id_user, descricao, telefone, data_cadastro, status_projeto, tag) VALUES (%s, %s, %s, %s, %s, %s)'
projetos = [
      ('Irrigamento Autosuficiente', 
      'Modelo de irrigamento de plantas onde não há dispersão de água no processo por meio de uma estrutura metálica resistente á corrosão.',
      '11998124683','2023-05-23 00:00:00', 'Em andamento', 'Sustentabilidade'),

      ('Restringir acesso ás áraeas de mananceais', 
      'Incentivo á criação de uma coleção de leis que detenham o acesso á pessoas não autorizadas ás areás atigindas.',
      '1191698431','2023-05-24 00:00:00', 'Não iniciado', 'Sustentabilidade'),
      
      ('Detecção de possíveis áreas atigindas por deslizamento', 
      'Criar aplicação que possibilite aos usuários reportarem áreas que estam em risco.',
      '11998271974','2023-05-22 00:00:00', 'Não iniciado', 'Deslizamento'),
]
cursor.executemany(projetos_sql, projetos)

cursor.execute('select * from ods-registration-site.cadastro_projetos')
print(' -------------  Projetos:  -------------')
for projeto in cursor.fetchall():
    print(projeto[1])


# commitando se não nada tem efeito

conn.commit()

cursor.close()
conn.close()