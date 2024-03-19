PROMPT_ANNOTATE = """For the given text below, please return a list of labels from teh available labels below.
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