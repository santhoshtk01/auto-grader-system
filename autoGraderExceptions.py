class NotValidQuestion(Exception):

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f"NotValidQuestion: {self.message}"


class NotValidAnswer(Exception):

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f"NotValidAnswer: {self.message}"
