import pandas as pd
from autoGrader import AutoGraderSystem
from sklearn.metrics import accuracy_score
from utils import find_score

__doc__ = """
This file is dedicated to get the output from the LLM of the ASAP dataset.
    var: output - contains the score got from the LLM.
    var: skipped - contains the index positions of the skipped essays.
"""

# Processing essay set 1
output = pd.read_excel("/home/santhoshtk/Pictures/AutoGrader/TestData/set1.xlsx")

essays = output["essay"]
originalScores = output["Score"]

question = """
While some argue that computers contribute to social isolation and 
health problems, can technology also be a tool for promoting positive 
social interaction, exercise, and connection with the natural world? 
Discuss both the potential benefits and drawbacks of computer use in 
modern society.
"""

# Creating the instance of the AGS
ags = AutoGraderSystem()
output = []
skipped = []
index = 0

for essay in essays:
    score = find_score(ags.getResult(question, essay))

    if score:
        output.append(score)
    else:
        skipped.append(index)

    index += 1

# TODO: Store the output in an appropriate file format to process the data further.
print(output)
print(skipped)
