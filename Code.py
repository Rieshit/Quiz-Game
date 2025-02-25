import time

# List of questions and options
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "choices": ["A. Shakespeare", "B. Dickens", "C. Hemingway", "D. Austen"],
        "answer": "A"
    },
    {
        "question": "What is the square root of 64?",
        "choices": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "What is 5 + 3?",
        "choices": ["A. 7", "B. 8", "C. 9", "D. 10"],
        "answer": "B"
    }
]

# Function to ask questions and track score
def ask_questions():
    score = 0
    for q in questions:
        print(q["question"])
        for choice in q["choices"]:
            print(choice)
        
        answer = input("Your answer (A/B/C/D): ").upper()
        
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}\n")
        
        time.sleep(1)  # Adding a short delay before the next question

    print(f"Your final score is {score}/{len(questions)}")

# Start the quiz
ask_questions()
