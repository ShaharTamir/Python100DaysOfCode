from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

questions_bank = []
for i in question_data:
    questions_bank.append(Question(i["question"], i["correct_answer"]))

quiz = QuizBrain(questions_bank)
quiz_interface = QuizInterface(quiz)


