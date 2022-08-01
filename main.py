from question_bank import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank=[]
for question in question_data:
    text=question["text"]
    answer=question["answer"]
    current_question=Question(text,answer)
    question_bank.append(current_question)
quiz=QuizBrain(question_bank)
while quiz.any_more_ques():
    quiz.next_question()
print("the game is over")
print(f"your final score is {quiz.score}/{quiz.question_number}")