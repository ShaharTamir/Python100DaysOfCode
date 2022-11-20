class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_question = None
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"

    def check_answer(self, user_answer):
        if self.current_question.verify_answer(user_answer):
            self.score += 1
            return True
        else:
            return False

    def score_string(self):
        return f"Score: {self.score}"
