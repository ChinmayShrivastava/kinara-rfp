PROMPT_ANNOTATE = """For the given text below, please return a list of labels from teh available labels below.
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
['contains_page_formatting_instructions']
--------------------
Example 2:
Text:
The proposal will be evaluated based on the following criteria:
1. Technical Approach
2. Management Approach
3. Past Performance
Labels:
['contains_evaluation_criteria']
--------------------
Text:
{text}
Labels:"""