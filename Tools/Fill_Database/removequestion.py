import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('lean_management_quiz.db')
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def delete_question(conn, question_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM questions WHERE id = ?", (question_id,))
    conn.commit()

# Demander l'ID de la question à supprimer
question_id = input("Entrez l'ID de la question à supprimer : ")

# Créer la connexion à la base de données
conn = create_connection()

# Supprimer la question
delete_question(conn, question_id)

# Fermer la connexion à la base de données
conn.close()
