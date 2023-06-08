import streamlit as st

def main():
    st.title("Quiz de Lean Management")

    categories = ['Catégorie 1', 'Catégorie 2', 'Catégorie 3', 'Catégorie 4', 'Catégorie 5']

    for category in categories:
        st.header(category)

        if category == 'Catégorie 1':
            # Questions pour la Catégorie 1
            st.markdown("Question 1 :")
            # Votre question 1
            # Réponse(s) possible(s) pour la question 1

            st.markdown("Question 2 :")
            # Votre question 2
            # Réponse(s) possible(s) pour la question 2

        elif category == 'Catégorie 2':
            # Questions pour la Catégorie 2
            st.markdown("Question 1 :")
            # Votre question 1
            # Réponse(s) possible(s) pour la question 1

            st.markdown("Question 2 :")
            # Votre question 2
            # Réponse(s) possible(s) pour la question 2

        elif category == 'Catégorie 3':
            # Questions pour la Catégorie 3
            st.markdown("Question 1 :")
            # Votre question 1
            # Réponse(s) possible(s) pour la question 1

            st.markdown("Question 2 :")
            # Votre question 2
            # Réponse(s) possible(s) pour la question 2

        elif category == 'Catégorie 4':
            # Questions pour la Catégorie 4
            st.markdown("Question 1 :")
            # Votre question 1
            # Réponse(s) possible(s) pour la question 1

            st.markdown("Question 2 :")
            # Votre question 2
            # Réponse(s) possible(s) pour la question 2

        elif category == 'Catégorie 5':
            # Questions pour la Catégorie 5
            st.markdown("Question 1 :")
            # Votre question 1
            # Réponse(s) possible(s) pour la question 1

            st.markdown("Question 2 :")
            # Votre question 2
            # Réponse(s) possible(s) pour la question 2

if __name__ == "__main__":
    main()
