import sqlite3
from sqlite3 import Error
import streamlit as st
import time

global profile_name_global
profile_name_global = "Aucun profil sélectionné"

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('lean_management_quiz.db') # create a database connection
        return conn
    except Error as e:
        print(e)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor() # create a Cursor object and call its execute() method to perform SQL commands
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def get_profiles():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM profiles")
    return cur.fetchall()

def profile_exists(conn, profile_name):
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM profiles WHERE name=?", (profile_name,))
    return cur.fetchone() is not None

def create_profile(conn, profile_name):
    cur = conn.cursor()
    if not profile_exists(conn, profile_name):
        cur.execute("INSERT INTO profiles (name, created_at) VALUES (?, datetime('now'))", (profile_name,))
        conn.commit()
        st.success("Profil créé avec succès!")
        time.sleep(2)
        st.experimental_rerun()
    else:
        st.warning("Ce profil existe déjà.")

def page_select_profile():
    st.title("Sélectionnez votre profil")
    conn = create_connection()
    profiles = get_profiles()
    if profiles:
        profile_names = [profile[1] for profile in profiles]
        profile_name = st.selectbox("Sélectionnez votre profil", profile_names)
        if st.button("Sélectionner"):
            st.session_state.profile_name_global = profile_name
            print(profile_name)
            return profile_name

    new_profile_name = st.text_input("Nom du profil")
    if st.button("Créer un nouveau profil"):
        if new_profile_name:  # ensure the name is not empty
            create_profile(conn, new_profile_name)
            profiles = get_profiles()  # update the profiles list
        else:
            st.warning("Veuillez entrer un nom de profil avant de cliquer sur 'Créer un nouveau profil'.")

def insert_question(conn, question_text, correct_answer, options, category_id):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO questions (question_text, correct_answer, option_1, option_2, option_3, option_4, category_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (question_text, correct_answer, *options, category_id))
    conn.commit()

def insert_result(conn, profile_id, correct_answers, category_id):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO results (profile_id, correct_answers_count, answer_category, created_at) 
        VALUES (?, ?, ?, datetime('now'))
    """, (profile_id, correct_answers, category_id))
    print(cur.execute)
    conn.commit()

def get_profile_id(conn):
    print("Dans la fonction get profile")
    print(st.session_state.profile_name_global)
    cur = conn.cursor()
    cur.execute("SELECT id FROM profiles WHERE name=?", (st.session_state.profile_name_global,))
    row = cur.fetchone()
    if row is not None:
        profile_id = row[0]
        print(f"Profile ID for {st.session_state.profile_name_global}: {profile_id}")  # debug print
        return profile_id
    else:
        return None

def insert_question_form():
    with st.form(key='insert_question_form'):
        st.title("Ajouter une question")

        question_text = st.text_input("Question")
        correct_answer = st.text_input("Bonne réponse")
        options = [st.text_input(f"Option {i+1}") for i in range(4)]
        
        categories = ['1 - Specify value', '2 - Identify the value stream', '3 - Make value flow continuously', '4 - Let customers pull value', '5 - Pursue perfection']
        category_id = st.selectbox("Catégorie", categories)

        submit_button = st.form_submit_button(label='Valider la question')
        if submit_button:
            conn = create_connection()
            insert_question(conn, question_text, correct_answer, options, categories.index(category_id) + 1)
            st.success("Question ajoutée avec succès!")


def page_quiz():
    st.title("Quiz sur le Lean Management")
    categories = ['Specify value', 'Identify the value stream', 'Make value flow continuously', 'Let customers pull value', 'Pursue perfection']
    category = st.sidebar.selectbox("Sélectionnez une catégorie", categories)
    if category:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM questions WHERE category_id = ?", (categories.index(category) + 1,))
        questions = cur.fetchall()
        answers = []
        for question in questions:
            st.header(question[1])  # question text
            options = question[3:7]  # option 1 to 4
            answer = st.radio("Sélectionnez la bonne réponse", options)
            answers.append(answer)  # Ajoute la réponse de l'utilisateur à la liste
        global profile_name_global
        if st.button("Soumettre votre formulaire"):
            print(f"Réponses de l'utilisateur : {answers}")
            profile_id = get_profile_id(conn)  # get the current profile id
            print(profile_id)
            correct_answers = sum(1 for question, answer in zip(questions, answers) if question[2] == answer)
            insert_result(conn, profile_id, correct_answers, categories.index(category) + 1)
            st.success(f"Vous avez {correct_answers} bonne(s) réponse(s) sur {len(questions)} questions.")


def main():
    try:
        database = r"lean_management_quiz.db"

        sql_create_profiles_table = """CREATE TABLE IF NOT EXISTS profiles (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            created_at text NOT NULL
                                        );"""

        sql_create_questions_table = """CREATE TABLE IF NOT EXISTS questions (
                                            id integer PRIMARY KEY,
                                            question_text text NOT NULL,
                                            correct_answer text NOT NULL,
                                            option_1 text NOT NULL,
                                            option_2 text NOT NULL,
                                            option_3 text NOT NULL,
                                            option_4 text NOT NULL,
                                            category_id integer NOT NULL
                                        );"""

        sql_create_results_table = """CREATE TABLE IF NOT EXISTS results (
                                    id integer PRIMARY KEY,
                                    profile_id integer NOT NULL,
                                    answer_category integer NOT NULL,
                                    correct_answers_count integer NOT NULL,
                                    created_at text NOT NULL,
                                    FOREIGN KEY (profile_id) REFERENCES profiles (id),
                                    FOREIGN KEY (answer_category) REFERENCES questions (category_id)
                                );"""

        conn = create_connection()
        if conn is not None:
            # create profiles table
            create_table(conn, sql_create_profiles_table)
            
            # create questions table
            create_table(conn, sql_create_questions_table)

            # create results table
            create_table(conn, sql_create_results_table)
        else:
            print("Error! cannot create the database connection.")
    except Exception as e:
        print(f"An error occurred in def main database: {e}")

    try:
        page = st.sidebar.selectbox("Sélectionnez une page", ["Sélection de profil", "Ajouter une question", "Quiz"])
        if page == "Sélection de profil":
            page_select_profile()
            print("ok profile")
        elif page == "Ajouter une question":
            insert_question_form()
            print("ok add question")
        elif page == "Quiz":
            page_quiz()
            print("ok quizz")
    
    except Exception as e:
        print(f"An error occurred in main select pages: {e}")

if __name__ == '__main__':
    main()
