class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def verify_answer(self, user_answer):
        return self.answer.lower() == user_answer.lower()
