from abc import ABC
from autoGraderExceptions import NotValidQuestion, NotValidAnswer


class ProcessInput(ABC):
    """
    Abstract to process the input got from the user.

    Reason including the two methods for validation.
    We should make sure that the input to the Large
    Language Model(LLM) is not invalid.
    """

    def validateQuestion(self):
        pass

    def validateAnswer(self):
        pass


class GetInput(ProcessInput):

    def __init__(self, question: str, userAnswer: str, actualAnswer: str):
        """
        Needs to pass the three parameters.
        :param question: The question of string format.
        :param userAnswer: The answer of the question in string format.
        :param actualAnswer: The actual answer of the question. (Answer Key).
        """
        self.question = question
        self.userAnswer = userAnswer
        self.actualAnswer = actualAnswer

        # Calling the validation methods.
        self.validateQuestion()
        self.validateAnswer()

    def validateQuestion(self):
        """
        Validate whether the `question` type is string or not.
        :exception NotValidQuestion
        """
        if not isinstance(self.question, str):
            raise NotValidQuestion(f"{str(self.question)[:50]}...")

    def validateAnswer(self):
        """
        Validate the both `userAnswer` and `acutalAnswer` whether they are string or not.
        :exception NotValidAnswer
        """
        if not isinstance(self.userAnswer, str):
            raise NotValidAnswer(f"{str(self.userAnswer)[:50]}...")

        if not isinstance(self.actualAnswer, str):
            raise NotValidAnswer(f"{str(self.actualAnswer)[:50]}...")


if __name__ == "__main__":
    pass
