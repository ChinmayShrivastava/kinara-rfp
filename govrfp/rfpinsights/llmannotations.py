from .prompts import PROMPT_ANNOTATE
import ast

_llmannotations = [
    "contains_evaluation_criteria",
    "contains_relevant_dates",
    "contains_communication_info",
]

text_representation = "\n".join(_llmannotations)

def llmannotations(text, llm):
    response = llm.complete(PROMPT_ANNOTATE.format(text=text, labels=text_representation)).text
    # use ast to parse the string into a list
    _list = ast.literal_eval(response)
    return {
        v: v in _list for v in _llmannotations
    }