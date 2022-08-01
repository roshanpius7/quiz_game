class QuizBrain:
     def __init__(self,q_bank):
        self.question_number=0
        self.score=0
        self.q_list=q_bank

     def any_more_ques(self):
        return self.question_number<len(self.q_list)
     def next_question(self):
        current_ques=self.q_list[self.question_number]
        self.question_number+=1
        user_choice=input(f"Q.{self.question_number} {current_ques.text} True/False :")
        self.check_answer(user_choice,current_ques)



     def check_answer(self,user_choice,current_ques):
        if user_choice==current_ques.answer:
            print("you are right!")
            self.score+=1
        else:
            print("you are wrong")
        print(f"your score is {self.score}/{self.question_number}")