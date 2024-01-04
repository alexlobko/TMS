import random


class Mistery:
    """
     Class representing a mystery quiz with a question, answer, and choices.
     """
    def __init__(self, question, answer, choices):
        """
        Initialize the Mistery class.

        Args:
            question (str): The question for the quiz.
            answer (str): The correct answer to the question.
            choices (dict): A dictionary of answer choices with their respective point values.
        """
        self.question = question
        self.answer = {answer: 3}
        self.choices = choices

    def quiz(self):
        """
        Conduct the quiz.

        Returns:
            int: The number of points earned by the user.
        """
        print(self.question)
        answers = list(self.answer) + list(set(self.choices.keys()))[:3]
        random.shuffle(answers)
        print(*[f'{i}. {j}' for i, j in enumerate(answers)], sep='\n')
        user_choice = input('choose answer: ')
        if user_choice == '' or not user_choice.isdigit() or int(user_choice) not in range(len(answers)):
            print('You got 0 points')
            return 0
        elif answers[int(user_choice)] in self.answer:
            print('Right answer! You got 3 points')
            return 3
        else:
            points = self.choices[answers[int(user_choice)]]
            print(f'Wrong answer! You got {points} points')
            return points


q1 = Mistery(question='2x2=', answer='4', choices={'1': -3, '2': -1, '3': 2, '5': 2, '6': -1, '7': -3})
q1.quiz()
