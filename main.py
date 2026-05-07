import tkinter as tk

# window
root = tk.Tk()
root.title("Python Quiz App")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# questions
questions = [
    {"q": "What is Python?", "options": ["Language", "Snake", "Game", "OS"], "ans": "Language",
     "exp": "Python is a programming language."},
    {"q": "Who created Python?", "options": ["Dennis", "Guido", "James", "Linus"], "ans": "Guido",
     "exp": "Guido van Rossum created Python."},
    {"q": "Keyword for function?", "options": ["fun", "def", "function", "define"], "ans": "def",
     "exp": "Functions are defined using 'def' keyword."},
    {"q": "File extension?", "options": [".py", ".txt", ".java", ".cpp"], "ans": ".py",
     "exp": "Python files use .py extension."},
    {"q": "Text datatype?", "options": ["int", "str", "bool", "float"], "ans": "str",
     "exp": "String (str) is used for text."},
    {"q": "Comment symbol?", "options": ["#", "//", "/*", "--"], "ans": "#",
     "exp": "# is used for comments in Python."},
    {"q": "Output of 2+3?", "options": ["5", "6", "23", "Error"], "ans": "5",
     "exp": "2+3 = 5."},
    {"q": "Input function?", "options": ["get()", "input()", "read()", "scan()"], "ans": "input()",
     "exp": "input() is used to get user input."},
    {"q": "Conditional keyword?", "options": ["if", "loop", "case", "switch"], "ans": "if",
     "exp": "if is used for condition checking."},
    {"q": "Boolean datatype?", "options": ["int", "bool", "str", "float"], "ans": "bool",
     "exp": "bool represents True/False."}
]

q_index = 0
score = 0
wrong_answers = []

# functions
def start_quiz():
    global q_index, score, wrong_answers
    q_index = 0
    score = 0
    wrong_answers = []

    title_label.pack_forget()
    start_button.pack_forget()
    show_question()

def show_question():
    global q_index

    if q_index >= len(questions):
        show_result()
        return

    q = questions[q_index]

    # 👉 Progress added here
    question_label.config(text=f"Question {q_index+1}/{len(questions)}:\n{q['q']}")
    question_label.pack(pady=20)

    for i in range(4):
        option_buttons[i].config(text=q["options"][i])
        option_buttons[i].pack(pady=5)

    result_label.config(text="")

def check_answer(selected):
    global q_index, score

    correct = questions[q_index]["ans"]
    explanation = questions[q_index]["exp"]

    if selected == correct:
        result_label.config(text=f"Correct ✅\n{explanation}", fg="green")
        score += 1
    else:
        result_label.config(text=f"Wrong ❌\nCorrect: {correct}\n{explanation}", fg="red")
        wrong_answers.append(questions[q_index])

    q_index += 1
    root.after(1500, show_question)

def show_result():
    question_label.config(text=f"Your Score: {score}/{len(questions)}")

    for btn in option_buttons:
        btn.pack_forget()

    # 👉 Final message based on score
    if score >= 8:
        msg = "Excellent 🎉"
    elif score >= 5:
        msg = "Good 👍"
    else:
        msg = "Keep Practicing 💪"

    result_label.config(text=msg)
    review_btn.pack(pady=10)

def show_review():
    review_window = tk.Toplevel(root)
    review_window.title("Review Mistakes")
    review_window.geometry("400x400")

    if not wrong_answers:
        tk.Label(review_window, text="No mistakes! 🎉").pack()
    else:
        for q in wrong_answers:
            tk.Label(review_window, text=f"Q: {q['q']}").pack(anchor="w")
            tk.Label(review_window, text=f"Correct: {q['ans']}").pack(anchor="w")
            tk.Label(review_window, text=f"Explanation: {q['exp']}").pack(anchor="w")
            tk.Label(review_window, text="------------------").pack()

# UI
title_label = tk.Label(root, text="Python Quiz App", font=("Arial", 18), bg="#f0f0f0")
title_label.pack(pady=40)

start_button = tk.Button(root, text="Start Quiz ▶", command=start_quiz, width=15)
start_button.pack()

question_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")

option_buttons = []
for i in range(4):
    btn = tk.Button(root, width=25,
        command=lambda i=i: check_answer(option_buttons[i].cget("text")))
    option_buttons.append(btn)

result_label = tk.Label(root, text="", bg="#f0f0f0")
result_label.pack(pady=10)

review_btn = tk.Button(root, text="Review Mistakes 📖", command=show_review)

root.mainloop()