import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('lean_management_quiz.db') # create a database connection to a SQLite database 
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
        'question_text': 'What are the fundamental principles of lean management?',
        'correct_answer': 'a) Specify value, identify waste, and pursue perfection.',
        'options': [
            'a) Specify value, identify waste, and pursue perfection.',
            'b) Reduce costs, improve efficiency, and eliminate bottlenecks.',
            'c) Enhance customer satisfaction, increase productivity, and optimize resources.',
            'd) Streamline processes, minimize waste, and achieve continuous improvement.'
        ]
    },
    {
        'question_text': 'Explain step 1 in lean management: specifying value and identifying the 8 types of waste.',
        'correct_answer': 'c) Step 1 includes identifying waste and eliminating non-value-added activities.',
        'options': [
            'a) Step 1 involves defining customer requirements and identifying potential areas of improvement.',
            'b) Step 1 focuses on setting goals and objectives for lean implementation.',
            'c) Step 1 includes identifying waste and eliminating non-value-added activities.',
            'd) Step 1 involves analyzing process flows and optimizing resource utilization.'
        ]
    },
    {
        'question_text': 'How would you define a process?',
        'correct_answer': 'a) A process is a systematic sequence of steps to achieve a specific goal or outcome.',
        'options': [
            'a) A process is a systematic sequence of steps to achieve a specific goal or outcome.',
            'b) A process is a set of tools and technologies used to automate tasks.',
            'c) A process is a collection of resources and materials used in production.',
            'd) A process is a framework for managing customer relationships.'
        ]
    },
    {
        'question_text': 'Who are the different types of customers in a process?',
        'correct_answer': 'a) Internal customers and external customers.',
        'options': [
            'a) Internal customers and external customers.',
            'b) Primary customers and secondary customers.',
            'c) Active customers and passive customers.',
            'd) End-users and stakeholders.'
        ]
    },
    {
        'question_text': 'Why is it important to identify the customer in a process?',
        'correct_answer': 'b) Understanding the customer\'s needs and expectations improves process design.',
        'options': [
            'a) Identifying the customer helps allocate resources effectively.',
            'b) Understanding the customer\'s needs and expectations improves process design.',
            'c) Customer identification is essential for marketing and sales purposes.',
            'd) Identifying the customer streamlines communication within the organization.'
        ]
    },
    {
        'question_text': 'What is a process map, and why is it useful?',
        'correct_answer': 'a) A process map is a visual representation of a process, showing the sequence of steps and interactions.',
        'options': [
            'a) A process map is a visual representation of a process, showing the sequence of steps and interactions.',
            'b) A process map is a tool used to track inventory levels in manufacturing.',
            'c) A process map is a document that outlines the roles and responsibilities of team members.',
            'd) A process map is a diagram that illustrates the flow of information within an organization.'
        ]
    }
    ]


    for question in questions:
            insert_question(conn, question['question_text'], question['correct_answer'], *question['options'], 1)

if __name__ == "__main__":
    main()
