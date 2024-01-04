import random


class Mistery:
    def __init__(self, question, answer, choices):
        self.question = question
        self.answer = answer
        self.choices = choices

    def quiz(self):
        print(self.question)
        random.shuffle(self.choices)
        answers = [self.answer] + self.choices[:3]
        random.shuffle(answers)
        print(*[f'{i}. {j}' for i, j in enumerate(answers)], sep='\n')
        user_choice = input('choose answer: ')
        if answers[int(user_choice)] == self.answer:
            print(True)
            return True
        else:
            print('wrong answer')
            return False

q1 = Mistery(question='2x2=', answer='4', choices=['1', '2', '3', '5', '6'])
q1.quiz()