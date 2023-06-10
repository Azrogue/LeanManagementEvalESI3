import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('lean_management_quiz.db')  # create a database connection to a SQLite database 
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def insert_question(conn, question_text, correct_answer, option_1, option_2, option_3, option_4, category_id):
    cur = conn.cursor()
    cur.execute("INSERT INTO questions(question_text, correct_answer, option_1, option_2, option_3, option_4, category_id) VALUES(?, ?, ?, ?, ?, ?, ?)", 
    (question_text, correct_answer, option_1, option_2, option_3, option_4, category_id))
    conn.commit()

def main():
    database = r"lean_management_quiz.db"
    conn = create_connection()
    questions = [
    {
        'question_text': 'What is step 3 in lean management, and what is the significance of flow and value stream mapping?',
        'correct_answer': 'b) Step 3 in lean management is to implement a pull system to control the flow of materials and information. Flow and value stream mapping reduce waste and lead time.',
        'options': [
            'a) Step 3 in lean management is to establish standardized work processes. Flow and value stream mapping ensure smooth operations.',
            'b) Step 3 in lean management is to implement a pull system to control the flow of materials and information. Flow and value stream mapping reduce waste and lead time.',
            'c) Step 3 in lean management is to optimize resource utilization. Flow and value stream mapping improve efficiency.',
            'd) Step 3 in lean management is to implement automation and technology. Flow and value stream mapping increase productivity.'
        ]
    },
    {
        'question_text': 'Why is understanding and improving processes important?',
        'correct_answer': 'b) Understanding and improving processes enhance customer satisfaction.',
        'options': [
            'a) Understanding and improving processes lead to cost reduction.',
            'b) Understanding and improving processes enhance customer satisfaction.',
            'c) Understanding and improving processes increase employee morale.',
            'd) Understanding and improving processes streamline decision-making.'
        ]
    },
    {
        'question_text': 'How can organizational boundaries hinder the flow of value?',
        'correct_answer': 'a) Organizational boundaries create silos and hinder effective communication and collaboration.',
        'options': [
            'a) Organizational boundaries create silos and hinder effective communication and collaboration.',
            'b) Organizational boundaries result in excessive bureaucracy and slow decision-making.',
            'c) Organizational boundaries lead to a lack of accountability and responsibility.',
            'd) Organizational boundaries increase lead time and waste in the process.'
        ]
    },
    {
        'question_text': 'Explain in a few words how eliminating bottlenecks and reducing buffers can improve the process.',
        'correct_answer': 'a) By eliminating bottlenecks, the flow of work becomes smoother and faster. Reducing buffers minimizes waiting time and improves overall efficiency.',
        'options': [
            'a) By eliminating bottlenecks, the flow of work becomes smoother and faster. Reducing buffers minimizes waiting time and improves overall efficiency.',
            'b) Eliminating bottlenecks and reducing buffers have no impact on the process.',
            'c) Eliminating bottlenecks and reducing buffers increase the complexity of the process.',
            'd) Eliminating bottlenecks and reducing buffers only apply to manufacturing processes, not services.'
        ]
    }
]



    for question in questions:
            insert_question(conn, question['question_text'], question['correct_answer'], *question['options'], 3)

if __name__ == "__main__":
    main()
