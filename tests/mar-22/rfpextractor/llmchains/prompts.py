COMPLIANCE_PROMPT = (
    "Attached is a text from an RFP document.\n"
    "Extract all the relevant compliances as a list from the following text, don't repeat, and be exhaustive. "
    "A compliance is a requirement that can fit into the sentence, \"The applicant is required to...\""
    "or contain strong words like 'must' or 'shall': \n\n"
    "{text}\n"
    "List of compliances starting with '-'\n:"
)

EVAL_CRITERIA_PROMPT = (
    "Attached is a text from an RFP document, suspected to contain the evaluation criteria and the rubric.\n"
    "Extract all the evaluation criteria and the rubric as a list from the following text, don't repeat, and "
    "be exhaustive. An evaluation criterion is a requirement that can fit into the sentence, \"The applicant "
    "will be evaluated based on...\": \n\n"
    "{text}\n"
    "List of evaluation criteria starting with '-'\n:"
)

IMPORTANT_DATES_PROMPT = (
    "Attached is a text from an RFP document, suspected to contain important dates.\n"
    "Based on the given schema, extract all that you can.\n"
    "The schema is as follows:\n"
    "{schema}\n"
    "The text is as follows:\n"
    "{text}\n"
)

RFP_INFO_PROMPT = (
    "Attached is a text from an RFP document.\n"
    "Based on the given schema, if the information isn't already extracted and stored, extract all that you "
    "can.\n"
    "The schema is as follows:\n"
    "{schema}\n"
    "The text is as follows:\n"
    "{text}\n"
)

ELIGIBILITY_PROMPT = (
    "Attached is a text from an RFP document, suspected to contain eligibility criteria.\n"
    "Extract all the eligibility criteria as a list from the following text, don't repeat, and be exhaustive. "
    "An eligibility criterion is a  requirement that can fit into the sentence, \"The applicant must be...\": "
    "\n\n"
    "{text}\n"
    "List of eligibility criteria starting with '-'\n:"
)

SUBMISSION_PROMPT = (
    "Attached is a text from an RFP document, suspected to contain submission information.\n"
    "Extract all the submission information as a list from the following text, don't repeat, and be "
    "exhaustive. A submission requirement is a requirement that can fit into the sentence, \"The "
    "applicant must submit...\": \n\n"
    "{text}\n"
    "List of submission requirements starting with '-'\n:"
)