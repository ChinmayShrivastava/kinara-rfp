from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "Attached is a text from an RFP document."
    "Extract all the relevant compliances as a list from the following text, don't repeat, and be exhaustive. A compliance is a"
    "requirement that can fit into the sentence, \"The applicant is required to...\""
    "or contain strong words like 'must' or 'shall': \n\n"
    "{text}",
)