PROMPT_ANNOTATE = """For the given compliance from an RFP below, please return a list of labels from the available labels below.
--------------------
Available labels:
{labels}
--------------------
Example 1:
Text:
Documents must be in English and formatted to fit on 8.5" x 11" paper with one-inch margins on all sides
Labels:
['is_formating_compliance']
--------------------
Example 2:
Text:
Include a summary table identifying all rounds of financing, purchase dates, investors for each round, and governance and information rights obtained by investors
['is_finance_compliance']
--------------------
Text:
{text}
Labels:"""

_PROMPT_ANNOTATE = """For the given text below, please return a list of labels from teh available labels below.
If the given text is an absolute requirement and affects the submission of the RFP, use applies_directly_to_the_rfp_submission.
If the given text doesn't affect the submission of the RFP, even though it is important, use doesn’t_apply_to_the_rfp_submission.
If the given text is a mandatory requirement, use is_mandatory.
--------------------
Available labels:
{labels}
--------------------
Example 1:
Text:
The proposals shall be prepared using the following format: 
  Use 8.5”x11” size paper, single spaced; 
  Use 1” margins all around; 
  Text shall be no smaller than 12-point font; 
Labels:
['is_mandatory', 'applies_directly_to_the_rfp_submission']
--------------------
Example 2:
Text:
The proposal will be evaluated based on the following criteria:
1. Technical Approach
2. Management Approach
3. Past Performance
Labels:
['doesn’t_apply_to_the_rfp_submission']
--------------------
Text:
{text}
Labels:"""