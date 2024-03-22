from langchain_core.prompts import ChatPromptTemplate

COMPLIANCE_PROMPT = ChatPromptTemplate.from_template(
    "Attached is a text from an RFP document.\n"
    "Extract all the relevant compliances as a list from the following text, don't repeat, and be exhaustive. A compliance is a "
    "requirement that can fit into the sentence, \"The applicant is required to...\""
    "or contain strong words like 'must' or 'shall': \n\n"
    "{text}",
)

EVAL_CRITERIA_PROMPT = ChatPromptTemplate.from_template(
    "Attached is a text from an RFP document, suspected to contain the evaluation criteria and the rubric.\n"
    "Extract all the evaluation criteria and the rubric as a list from the following text, don't repeat, and be exhaustive. An evaluation criterion is a"
    "requirement that can fit into the sentence, \"The applicant will be evaluated based on...\": \n\n"
    "{text}",
)

IMPORTANT_DATES_PROMPT = ChatPromptTemplate.from_template(
    "Attached is a text from an RFP document, suspected to contain important dates.\n"
    "Based on the given schema, extract all that you can.\n"
    "The schema is as follows:\n"
    "{schema}\n"
    "The text is as follows:\n"
    "{text}",
)

RFP_INFO_PROMPT = ChatPromptTemplate.from_template(
    "Attached is a text from an RFP document.\n"
    "Based on the given schema, extract all that you can.\n"
    "The schema is as follows:\n"
    "{schema}\n"
    "The text is as follows:\n"
    "{text}",
)