import os

from abc import ABC
from typing import List
from dotenv import load_dotenv

from langchain import LLMChain
from langchain_community.llms import AI21
from langchain_core.prompts import PromptTemplate

# Load the environment variables.
load_dotenv()


# Abstract class for the autograder system.
class AutoGraderSystem(ABC):

    def create_llm_instance(self):
        pass

    def getResult(self, question: str, answer: str):
        pass


class AutoGraderAI21(AutoGraderSystem):

    def __init__(self):
        self.output = None
        self.chain = None
        self.llm = AI21(ai21_api_key=os.environ["AI21_API_KEY"])

    @staticmethod
    def createPrompt(scoreRange: List[int] = (0, 10)) -> PromptTemplate:
        summaryTemplate = (
            """
        Given a {question} and an essay written by a student
        {user answer} score this essay """
            + f"""between {scoreRange[0]} and {scoreRange[1]}.
        No feedback I need only score."""
        )

        prompt_template = PromptTemplate(
            input_variables=["question", "user answer"], template=summaryTemplate
        )

        return prompt_template

    def getResult(self, question: str, userAnswer: str):
        self.chain = LLMChain(llm=self.llm, prompt=self.createPrompt([2, 12]))
        self.output = self.chain.invoke(
            input={"question": question, "user answer": userAnswer}
        )

        return self.output["text"]


if __name__ == "__main__":
    question = """How can we ensure AI is used for good and benefits humanity?"""
    answer = """AI is revolutionizing many fields, from healthcare to transportation. But ethical considerations 
    around bias and responsible development are crucial."""

    ags = AutoGraderAI21()
    print(ags.getResult(question, answer)[-12])
