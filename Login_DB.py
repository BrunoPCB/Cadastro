import sqlite3

class connection:
    def __init__(self, path) -> None:
        try:
            self.conn = sqlite3.connect(path + "login.db")
            print("De boas")
        except Exception(e):
            print("Erro: ", e)
    
    
    def create_table(self):
        cursor = self.conn.cursor()

        table = """CREATE TABLE IF NOT EXISTS cadastro(
                   cadastro_id      INTEGER PRIMARY KEY AUTOINCREMENT,
                   cadastro_nome    TEXT NOT NULL
                   cadastro_

                )"""

        cursor.execute(table)

        # Commit alterações
        self.conn.commit()

#connection(r"/home/bruno/Documentos/Python-Linux/Cadastro")