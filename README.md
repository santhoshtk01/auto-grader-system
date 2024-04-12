# auto-grader-system

## Module: InputProcessor
The main goal of the input processor is to validate the input given by the user to prevent unstructured
or invalid data feed to the LLM. This could potentially reduces the performance of the system. As of now
just simple validation whether the given input is string or not. Moving further can add more filtering
process before feeding the input to LLM's.

## Module: grader
This is the heart of the system which is responsible for creating the instances of the LLM's and 
the `prompt`.