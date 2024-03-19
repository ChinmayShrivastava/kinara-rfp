from .prompts import PROMPT_ANNOTATE
import ast

# 1.⁠ ⁠Evaluation Criteria - Ex: Technical Approach, Management Background, Commercialization, etc.
# 2.⁠ ⁠Logistics - Contact Info, Payment Info, Date and Time of Submission, Formatting, etc.
# 3.⁠ ⁠Certifications 
# 4.⁠ ⁠Statement of Work / Scope of Work / PWS etc.
# 5.⁠ ⁠Supporting Documents (Similar to Certification)
# Logistics / Submission / Technial Volume : Type of File, Page Limits, Page number, etc.

_llmannotations = [
    # "contains_evaluation_criteria",
    # "contains_performance_metrics",
    # "contains_required_certifications",
    # "contains_logistical_information",
    # "contains_logistical_requirements_for_submission",
    # "contains_statement_of_work",
    # "contains_supporting_documents_requirements",
    # "contains_scope_of_work",
    # "contains_technical_volume_requirements",
    # "contains_performance_work_statement",
    # "contains_pricing_requirements",
    # "is_good_to_have",
    "applies_directly_to_the_rfp_submission",
    "doesn’t_apply_to_the_rfp_submission",
    "is_mandatory",
    "other"
]

text_representation = "\n".join(_llmannotations)

def llmannotations(text, llm):
    response = llm.complete(PROMPT_ANNOTATE.format(text=text, labels=text_representation)).text
    # use ast to parse the string into a list
    _list = ast.literal_eval(response)
    return {
        v: v in _list for v in _llmannotations
    }