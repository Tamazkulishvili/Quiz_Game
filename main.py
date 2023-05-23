from question_model import question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for question in question_bank:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Youre final score was: {quiz.score}/{quiz.question_number}")