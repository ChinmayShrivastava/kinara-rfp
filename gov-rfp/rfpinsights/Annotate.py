from llama_index.llms.openai import OpenAI
from reannotations import reannotations

class Annotate:
    def __init__(
            self,
            llm: OpenAI = OpenAI(model="gpt-3.5-turbo"),
            ):
        self.model = llm

    def _annotate(self, text: str):
        _annotations = {}
        for key, value in reannotations.items():
            _annotations[key] = value(text)
        return _annotations
    
    def __call__(self, text: str):
        return self._annotate(text)