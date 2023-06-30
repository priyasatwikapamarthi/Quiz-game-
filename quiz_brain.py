    def still_has_questions(self):
        if len(self.question_list) > self.question_number :
            return True
        else :
            return False

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower() :
            print("You got it Right!")
            self.score += 1

        else :
            print("You are wrong")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}.")


