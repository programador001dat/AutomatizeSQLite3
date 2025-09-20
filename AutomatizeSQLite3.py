# encoding: utf-8

import sqlite3

''' automatizando um SQLite3 '''

# Funcões: Create, Insert.

def __Insert__():

   print("(?) Vamos inserir QUERYs dentro da tabela myTable, caso essa tabela não exista ocorreŕa erros.\n")
   conn = sqlite3.connect('myTable.db')
   cursor = conn.cursor()

   produto = str(input("[+] nome do produto: "))
   data_da_venda = str(input("[+] data da venda, [ exemplo '2025-09-01']: "))
   categoria = str(input("[+] categoria: "))
   valor_da_venda = int(input("[+] valor da venda, [ exemplo 1500.00]: "))

   query = """
      INSERT INTO myTable(produto, data_da_venda, categoria, valor_da_venda)
      VALUES (?, ?, ?, ?)
   """
   cursor.execute(query, (produto, data_da_venda, categoria, valor_da_venda))
   conn.commit()
   conn.close()

   print("(C) dados inserido com sucesso no Bando de Dado -> myTable.db")

def __Column__():

   print("(?) vamos criar colunas dentro da tabela myTable, caso essa tabela não exista ocorrerá erros.\n")
   conn = sqlite3.connect('myTable.db')
   cursor = conn.cursor()

   try:
      produto = str(input("-> Quer uma coluna [produto] sim\\nao: "))
      data_da_venda = str(input("-> Quer uma coluna [data_da_venda] sim\\nao: "))
      categoria = str(input("-> Quer uma coluna [categoria] sim\\nao: "))
      valor_da_venda = str(input("-> Quer uma coluna [valor_da_venda] sim\\nao: "))

      # verificar se a coluna já existe
      cursor.execute("PRAGMA table_info(myTable)") # obtém as informações das colunas da tabela
      existing_columns = [column[1] for column in cursor.fetchall()] # lista de colunas existentes

      if produto.lower() == "sim" and 'produto' not in existing_columns:
         cursor.execute("ALTER TABLE myTable ADD COLUMN produtos TEXT")

      if data_da_venda.lower() == "sim" and 'data_da_venda' not in existing_columns:
         cursor.execute("ALTER TABLE myTable ADD COLUMN data_da_venda DATE")

      if categoria.lower() == "sim" and 'categoria' not in existing_columns:
         cursor.execute("ALTER TABLE myTable ADD COLUMN categoria TEXT")

      if valor_da_venda.lower() == "sim" and 'valor_da_venda' not in existing_columns:
         cursor.execute("ALTER TABLE myTable ADD COLUMN valor_da_venda REAL")

      conn.commit() # aplica as mudança no banco de dados.
      conn.close()

   except Exception as error:
      print("(X) escreva em minusculo!\n")

   print("(C) colunas adicionadas com sucesso!\n")

def __Table__():

   try:

      conn = sqlite3.connect('myTable.db')
      cursor = conn.cursor()
      print("(C) conexão com sucesso com SQLite3\n\n")

      if conn:
         print("(?) lembre-se o nome padrão para criar a tabela é myTable, diferente disso ocorrerá erro no sistema\n")
         createTable = str(input("-> digite o nome para sua tabela, sem espaços [myTable]: "))
         cursor.execute(f'''
            CREATE TABLE {createTable}(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               data_de_venda DATE,
               produto TEXT,
               categoria TEXT,
               valor_da_venda REAL
            )
         ''')
         print("(C) tabela criada com sucesso em seu diretorio raiz.\n")
         conn.commit()
         conn.close()

   except Exception as error:
      print("(?) está tabela foi reconstruida do zero\n")

   finally:
      pass


def main():

   while True:

      print("oOo...... Automatizando SQLite3 ......oOo\n\n")
      print("[0]\tCriar a tabela")
      print("[1]\tCriar colunas da tabela")
      print("[2]\tInserir QUERYs no banco de dados.\n")
      print("oOo................................oOo")

      user = str(input("#:"))
      if user == "0":
         __Table__()

      elif user == "1":
         __Column__()

      elif user == "2":
         __Insert__()

      else:
         print("\n\n\n\n\noOo...... Fechando programa ......oOo\n\n\n\n\n")
         break

if __name__ == "__main__":
   main()


