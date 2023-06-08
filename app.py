import sqlite3
from sqlite3 import Error
import streamlit as st
import time

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
            return profile_name

    new_profile_name = st.text_input("Nom du profil")
    if st.button("Créer un nouveau profil"):
        if new_profile_name:  # ensure the name is not empty
            create_profile(conn, new_profile_name)
            profiles = get_profiles()  # update the profiles list
        else:
            st.warning("Veuillez entrer un nom de profil avant de cliquer sur 'Créer un nouveau profil'.")



def page_quiz():
    st.title("Quiz sur le Lean Management")
    categories = ['Catégorie 1', 'Catégorie 2', 'Catégorie 3', 'Catégorie 4', 'Catégorie 5']
    category = st.sidebar.selectbox("Sélectionnez une catégorie", categories)
    if category:
        st.header(category)
        st.subheader("Question")
        answer = st.radio("Sélectionnez la bonne réponse", ["Option 1", "Option 2", "Option 3"])
        if st.button("Soumettre"):
            if answer == "Option 1":
                st.success("Bonne réponse!")
            else:
                st.error("Mauvaise réponse.")

def main():
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
        create_table(conn, sql_create_profiles_table)
        create_table(conn, sql_create_results_table)
    else:
        print("Error! cannot create the database connection.")

    page = st.sidebar.selectbox("Sélectionnez une page", ["Sélection de profil", "Quiz"])
    if page == "Sélection de profil":
        page_select_profile()
    elif page == "Quiz":
        page_quiz()

if __name__ == '__main__':
    main()
