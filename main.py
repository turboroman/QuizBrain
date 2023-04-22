from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_question():
#     quiz.next_question()

print("That's all")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")