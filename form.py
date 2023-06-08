import streamlit as st

def main():
    st.title("Quiz de Lean Management")
    questions = []

    def add_question():
        question_type = st.radio("Type de question :", ["Choix multiple", "Zone de texte"])
        question_text = st.text_input("Question :")
        if question_type == "Choix multiple":
            num_options = st.number_input("Nombre d'options :", min_value=2, step=1, value=2)
            options = []
            for i in range(num_options):
                option = st.text_input(f"Option {i+1} :")
                options.append(option)
            correct_option = st.number_input("Numéro de la ou des bonnes options :", min_value=1, step=1)
            questions.append({"type": "choix_multiple", "question": question_text, "options": options, "correct_option": correct_option})
        else:
            questions.append({"type": "texte", "question": question_text})

    def remove_question(index):
        if index < len(questions):
            del questions[index]

    add_question_button = st.button("Ajouter une question")
    if add_question_button:
        add_question()

    for i, question in enumerate(questions):
        st.markdown(f"Question {i+1} : {question['question']}")
        remove_button = st.button(f"Supprimer la question {i+1}")
        if remove_button:
            remove_question(i)
        if question['type'] == 'choix_multiple':
            options = question['options']
            correct_option = question['correct_option']
            selected_option = st.radio("", options)
            if selected_option == options[correct_option-1]:
                st.markdown("Bonne réponse !")
            else:
                st.markdown("Mauvaise réponse.")
        else:
            response = st.text_input("Réponse :")
            st.markdown("Votre réponse : " + response)

if __name__ == "__main__":
    main()
