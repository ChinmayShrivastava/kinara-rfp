# from langchain.chains import create_extraction_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

class ExtractionChain:

    def __init__(
        self,
        prompt: ChatPromptTemplate,
        model: ChatOpenAI = ChatOpenAI(model="gpt-3.5-turbo"),
        output_parser: StrOutputParser = StrOutputParser(),
    ):
        self.chain = (
            {"text": RunnablePassthrough()} 
            | prompt
            | model
            | output_parser
        )

    def invoke(self, text: str) -> str:
        return self.chain.invoke(text)