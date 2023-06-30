from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    #print(question)
    d_text = question["text"]
    d_answer = question["answer"]
    ques = Question(d_text, d_answer)
    ##print(d_text)
    question_bank.append(ques)

quiz = QuizBrain(question_bank)
# Each element in question bank list is an object
while quiz.still_has_questions() :
    quiz.next_question()

print("You reached end of the quiz")
print(f"Your score is {quiz.score}/{quiz.question_number}")


