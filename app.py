import sqlite3
from sqlite3 import Error
import streamlit as st

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

def page_select_profile():
    st.title("Sélectionnez votre profil")
    profiles = get_profiles()
    if profiles:
        profile_name = st.selectbox("Sélectionnez votre profil", profiles)
        if st.button("Sélectionner"):
            return profile_name
    else:
        if st.button("Créer un nouveau profil"):
            st.text_input("Nom du profil")
            if st.button("Créer"):
                st.success("Profil créé avec succès!")

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

    sql_create_results_table = """CREATE TABLE IF NOT EXISTS results (
                                    id integer PRIMARY KEY,
                                    profile_id integer NOT NULL,
                                    category text NOT NULL,
                                    answers text NOT NULL,
                                    created_at text NOT NULL,
                                    FOREIGN KEY (profile_id) REFERENCES profiles (id)
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
