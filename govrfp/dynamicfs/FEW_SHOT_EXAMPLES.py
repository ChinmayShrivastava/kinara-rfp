FINAL_PROMPT_TEMPLATE = """For the given chunk from an RFP document and it's scope, generate any critical and informative information present.
------------------------------------------------
Example 1
{fs1}
------------------------------------------------
Example 2
{fs2}
------------------------------------------------
Example 3
{current_chunk}
"""

FORMAT_TEMPLATE_FOR_NEW_CHUNK = """RFP DOC Scope: The Contractor shall provide a virtual coaching platform that includes scheduling, coach 
matching, assessments, a resource portal, and on-demand specialty coaching available for 
each coaching participant. The Executive Coaching shall take place virtually, consisting of 
individualized, one-on-one sessions.
Doc Page Number: {page_number}
Chunk:
{chunk}
Output:
"""

FS_EXAMPLE_TEMPLATE = """{chunk}
Output:
{output}"""

FEW_SHOT_EXAMPLES = [
    {
        "id": 1,
        "text": """RFP DOC Scope: The Contractor shall provide a virtual coaching platform that includes scheduling, coach 
matching, assessments, a resource portal, and on-demand specialty coaching available for 
each coaching participant. The Executive Coaching shall take place virtually, consisting of 
individualized, one-on-one sessions. 
Doc Page Number: 83 and 84
Chunk:
For the purpose of this solicitation, terms are defined below:   
  
A "strength" is an attribute of the Offeror's proposal that exceeds the specified performance or 
capability requirements in a way that is beneficial to the government.  
  
A "weakness" is a flaw in the proposal that increases the risk of unsuccessful contract 
performance.

A “significant weakness” in the proposal is a flaw that appreciably increases the risk of 
unsuccessful contract performance.  
  
A "deficiency" is a material failure of a proposal to meet a Government requirement or a 
combination of significant weaknesses in a proposal that increases the risk of unsuccessful 
contract performance to an unacceptable level. A proposal with a deficiency cannot be found 
eligible for award and is rated “unacceptable”. 
 
Proposals rated that have 1 or more deficiencies for any of the Factors are NOT eligible for 
award and will be excluded from further consideration.""",
        "output": """CRITICAL: If the application has more than one deficiency, it will be excluded from further consideration. Simply, a deficiency is failure to meet a requirement or a combination of significant weaknesses that increases the risk of unsuccessful contract performance to an unacceptable level. A proposal with a deficiency cannot be found eligible for award and is rated “unacceptable”.
        INFORMATIVE: A "strength" is an attribute of the Offeror's proposal that exceeds the specified performance or capability requirements in a way that is beneficial to the government. A "weakness" is a flaw in the proposal that increases the risk of unsuccessful contract performance. A “significant weakness” in the proposal is a flaw that appreciably increases the risk of unsuccessful contract performance.""",
    },
    {
        "id": 2,
        "text": """RFP DOC Scope: The Contractor shall provide a virtual coaching platform that includes scheduling, coach 
matching, assessments, a resource portal, and on-demand specialty coaching available for 
each coaching participant. The Executive Coaching shall take place virtually, consisting of 
individualized, one-on-one sessions. 
Doc Page Number: 84
Chunk:
4.2.1.1 Confidence Ratings for Factor 1 Technical Approach 
  
The Government will assess its confidence in each Offeror by evaluating the Technical 
Approach of the proposal to determine if the Offeror has demonstrated the ability to effectively 
and efficiently perform the work specified in the SOW. The approach should reflect a clear 
understanding of the work under this requirement specifically Section III of the SOW and should 
demonstrate how each task in the SOW will be accomplished.  
 
The ratings that will be utilized to evaluate Factor 1 Technical Approach are as follows:  
 
RATING | DEFINITIONS 
High Confidence | The Government has high confidence that the Offeror understands the 
requirement, proposes a sound approach, and will be successful in 
performing the contract action with little or no Government intervention. 
Some Confidence | The Government has some confidence that the Offeror understands the 
requirement, proposes a sound approach, and will be successful in 
performing the contract with some Government intervention. 
Low Confidence | The Government has low confidence that the Offeror understands the 
requirement, proposes a sound approach, or will be successful in 
performing the contract even with Government intervention. 
 
Proposals rated “unacceptable” for any of the Factors are NOT eligible for award and will be 
excluded from further consideration.""",
        "output": """CRITICAL: Offerer's will be evaluated on their technical approach based on the SOW and will be rated as High Confidence, Some Confidence, or Low Confidence.
        CRITICAL: There are multiple factors that will be evaluated and proposals rated “unacceptable” for any of the Factors are NOT eligible for award and will be excluded from further consideration.
        INFORMATIVE: The technical approach will be evaluated based on the SOW and will be rated as High Confidence, Some Confidence, or Low Confidence. High Confidence means the Government has high confidence that the Offeror understands the requirement, proposes a sound approach, and will be successful in performing the contract action with little or no Government intervention. Some Confidence means the Government has some confidence that the Offeror understands the requirement, proposes a sound approach, and will be successful in performing the contract with some Government intervention. Low Confidence means the Government has low confidence that the Offeror understands the requirement, proposes a sound approach, or will be successful in performing the contract even with Government intervention.""",
    },
    {
        "id": 3,
        "text": """RFP DOC Scope: The Contractor shall provide a virtual coaching platform that includes scheduling, coach 
matching, assessments, a resource portal, and on-demand specialty coaching available for 
each coaching participant. The Executive Coaching shall take place virtually, consisting of 
individualized, one-on-one sessions. 
Doc Page Number: 81
Chunk:
2.6   Page Limits Matrix  
 
Table 3.4 
Proposal 
Volume  Volume Title  Page Limit 
I  Cover Letter   2 pages for Cover  
Letter   
II  Technical Approach  
Volume   5 Pages  
III  Management Approach 
Volume 
3 pages 
IV  Past Performance Volume  
Past Performance  
Reference  
Attachments (3 
pages)  
V  Completed RFP and Price 
Volume   No page limit

2.6.1   Page Limitations  
  
Page limitations shall be treated as maximums.  If exceeded, the excess pages will not be read or 
considered in the evaluation or award decision of the proposal.  Each page shall be counted 
except introductory letter(s), cover pages, table of contents, list of tables or drawings, tabs, and 
glossaries, unless otherwise noted in this provision.""",
        "output": """CRITICAL: The page limits for each volume are as follows: Cover Letter (2 pages), Technical Approach Volume (5 pages), Management Approach Volume (3 pages), Past Performance Volume (3 pages), and Completed RFP and Price Volume (No page limit).
        INFORMATIVE: Page limitations shall be treated as maximums. If exceeded, the excess pages will not be read or considered in the evaluation or award decision of the proposal. Each page shall be counted except introductory letter(s), cover pages, table of contents, list of tables or drawings, tabs, and glossaries, unless otherwise noted in this provision.""",
    },
    {
        "id": 4,
        "text": """RFP DOC Scope: The Contractor shall provide a virtual coaching platform that includes scheduling, coach 
matching, assessments, a resource portal, and on-demand specialty coaching available for 
each coaching participant. The Executive Coaching shall take place virtually, consisting of 
individualized, one-on-one sessions. 
Doc Page Number: 80
Chunk:
2.4.5  Volume V – Complete RFP and Price  
 
2.4.5.1  Completed Copy and Signed RFP (and any Amendments) 
 
One complete copy of the RFP, and/or amendments (NOTE: Offerors shall complete all required 
fill-ins as required.) 
 
Offerors must submit all included “fill-in” Provisions/Clause listed below. Providing a proposal 
without filling in the Provisions/Clauses may result in the offeror receiving an overall evaluated 
score of “Non-Responsive”. Proposals that fail to furnish required representations or information 
or reject the terms and conditions of the solicitation may be excluded from consideration.  
 
These will not be part of your page count. 
 
  FAR 52.203-2 – Certificate of Independent Price Determination (Apr 1985) 
  52.204-5 – Women-Owned Business (Other Than Small Business) (Oct 2014) 
  FAR 52.204-24 - Representation Regarding Certain Telecommunications and Video 
Surveillance Services or Equipment (Nov 2021) 
  FAR 52.212-3 Offeror Representations and Certifications—Commercial Products and 
Commercial Services (Dec 2022)  
  DTAR 1052.209-70 - Notice and Consent to Disclose and Use of Taxpayer Return 
Information (Nov 2017)""",
        "output": """CRITICAL: Offerors must submit all included “fill-in” Provisions/Clause including FAR 52.203-2, 52.204-5, 52.204-24, 52.212-3, and DTAR 1052.209-70. Providing a proposal without filling in the Provisions/Clauses may result in the offeror receiving an overall evaluated score of “Non-Responsive”. Proposals that fail to furnish required representations or information or reject the terms and conditions of the solicitation may be excluded from consideration. These will not be part of your page count.""",
    },
    {
        "id": 5,
        "text": """RFP DOC Scope: The Contractor shall provide a virtual coaching platform that includes scheduling, coach 
matching, assessments, a resource portal, and on-demand specialty coaching available for 
each coaching participant. The Executive Coaching shall take place virtually, consisting of 
individualized, one-on-one sessions. 
Doc Page Number: 76
Chunk:
2.2   RFP Response Package  
 
Phase 1: Demonstration of fully developed COTS On Demand Coaching Platform Resource. 
The Offerors will provide a demonstration of their COTS On Demand Coaching Platform and 
will have the opportunity to voluntarily withdraw from Phase 2 participation if they are not able 
to achieve a high confidence rating. 
  
Phase 2: Full Proposal Submission  
 
The RFP response package shall be organized as follows:  
  
- Volume I – Cover Letter  
- Volume II – Technical Approach 
- Volume III - Management Approach  
- Volume IV – Past Performance  
- Volume V – Cost/Price""",
        "output": """CRITICAL: The RFP response package shall be organized as follows: Volume I – Cover Letter, Volume II – Technical Approach, Volume III - Management Approach, Volume IV – Past Performance, and Volume V – Cost/Price.
        INFORMATIVE: The Offerors will provide a demonstration of their COTS On Demand Coaching Platform and will have the opportunity to voluntarily withdraw from Phase 2 participation if they are not able to achieve a high confidence rating.""",
    },
    {
        "id": 6,
        "text": """RFP DOC Scope: The Contractor shall provide a virtual coaching platform that includes scheduling, coach 
matching, assessments, a resource portal, and on-demand specialty coaching available for 
each coaching participant. The Executive Coaching shall take place virtually, consisting of 
individualized, one-on-one sessions. 
Doc Page Number: 79
Chunk:
2.4.3  Volume III: Management Approach 
  
Order and number Volume III as follows:  
  
1. Table of Contents  
2. Glossary of Abbreviations and Acronyms  
3. Management Approach  
4. Subcontracting Plan 
 
The Offeror shall plan, schedule, initiate, administer, and monitor each task to meet 
requirements, as well as manage the delivery requirements in SOW Section 4. The proposal shall 
describe how the Offeror plans to manage all tasks described in the SOW.   
 
The Offeror shall provide a proposed subcontracting plan compliant with FAR Clause 52.219-9 
demonstrating how small businesses, including small, disadvantaged businesses, women owned 
small businesses, veteran owned small businesses, service-disabled veteran owned small 
businesses, and HUBZone small businesses, will play an active role throughout the life of this 
contract. The plan shall include a list of the legal name, applicable socio-economic categories, 
corporate address, SOW related specialties, and geographic service area(s) of all proposed 
subcontractors at any tier and outline the teaming and subcontracting arrangements proposed for 
performance of work contained in the solicitation. small businesses are not required to submit a 
detailed 52.219-9 subcontracting plan but are still required to state how much work will be 
subcontracted to large and small businesses.""",
        "output": """CRITICAL: Volume III: Management Approach shall include a Table of Contents, Glossary of Abbreviations and Acronyms, Management Approach, and Subcontracting Plan in that order.
        INFORMATIVE: The Offeror shall plan, schedule, initiate, administer, and monitor each task to meet requirements, as well as manage the delivery requirements in SOW Section 4. The proposal shall describe how the Offeror plans to manage all tasks described in the SOW. The Offeror shall provide a proposed subcontracting plan compliant with FAR Clause 52.219-9 demonstrating how small businesses, including small, disadvantaged businesses and others, will play an active role throughout the life of this contract.
        INFORMATIVE: Small businesses are not required to submit a detailed 52.219-9 subcontracting plan but are still required to state how much work will be subcontracted to large and small businesses."""
    },
    {
        "id": 7,
        "text": """RFP DOC Scope: The Contractor shall provide a virtual coaching platform that includes scheduling, coach 
matching, assessments, a resource portal, and on-demand specialty coaching available for 
each coaching participant. The Executive Coaching shall take place virtually, consisting of 
individualized, one-on-one sessions. 
Doc Page Number: 75 and 76
Chunk:
2.1.3 Page Size and Format   
  
The proposals shall be prepared using the following format: 
 
  Use 8.5”x11” size paper, single spaced; 
  Use 1” margins all around; 
  Text shall be no smaller than 12-point font; 
  Font style and size for illustrations, drawings, and tables are at the Offeror’s discretion, 
but all labels and markings must be easily readable. Color may be used at the discretion 
of the Offeror.
Every page, except for the Title Page, shall contain a page number. Blank pages will contain the 
marking “Page Intentionally Left Blank.” Every page will contain the Offeror’s name and the 
RFP number. It is the Offeror’s responsibility to ensure data considered sensitive is marked as 
such. These markings may appear only in the margins. The Offeror shall include the point of 
contact (name, telephone number, e-mail address, and fax number) that can assist the CO with 
questions/problems associated with the Offeror’s quote submission. 
 
*Submissions shall be via email in MS Word, MS Excel, and/or .pdf format.""",
        "output": """CRITICAL: Paper size should be 8.5”x11”, single spaced, with 1” margins all around. Text shall be no smaller than 12-point font. Font style and size for illustrations, drawings, and tables are at the Offeror’s discretion. Everything must be easily readable and accessible. Color may be used at the discretion of the Offeror.
        CRITICAL: Every page should hav a page number, except for the Title Page. Blank pages will contain the marking “Page Intentionally Left Blank.” Every page will contain the Offeror’s name and the RFP number.
        CRITICAL: Submissions shall be via email in MS Word, MS Excel, and/or .pdf format.
        CRITICAL: It is the Offeror’s responsibility to ensure data considered sensitive is marked as such. These markings may appear only in the margins. The Offeror shall include the point of contact (name, telephone number, e-mail address, and fax number) that can assist the CO with questions/problems associated with the Offeror’s quote submission.""",
    },
    {
        "id": 8,
        "text": """RFP DOC Scope: The Contractor shall provide a virtual coaching platform that includes scheduling, coach 
matching, assessments, a resource portal, and on-demand specialty coaching available for 
each coaching participant. The Executive Coaching shall take place virtually, consisting of 
individualized, one-on-one sessions. 
Doc Page Number: 8
Chunk:
BACKGROUND 
 
The U.S. Department of the Treasury (Treasury), Treasury Executive Institute (TEI) is 
seeking a subscription to a web-based application resource that provides a platform for on-
demand professional coaching in areas such as alignment, cognitive agility, and managing 
teams that will equip leaders to more effectively tackle the daily demands associated with 
their roles for the Treasury’s Departmental Offices. Specifically, TEI would like to utilize 
professional coaching to help its clients develop Executive Core Qualifications (ECQs), (1) 
learn and practice coaching skills, (2) improve the ability to give and receive feedback, and 
(3) become more effective leaders for their teams.  
 
2.  SCOPE 
 
The Contractor shall provide a virtual coaching platform that includes scheduling, coach 
matching, assessments, a resource portal, and on-demand specialty coaching available for 
each coaching participant. The Executive Coaching shall take place virtually, consisting of 
# individualized, one-on-one sessions.""",
        "output": """INFORMATIVE: The TEI would like to utilize professional coaching to help its clients develop Executive Core Qualifications (ECQs), learn and practice coaching skills, improve the ability to give and receive feedback, and become more effective leaders for their teams.
        INFORMATIVE: The Contractor shall provide a virtual coaching platform that includes scheduling, coach matching, assessments, a resource portal, and on-demand specialty coaching available for each coaching participant. The Executive Coaching shall take place virtually, consisting of individualized, one-on-one sessions.""",
    },
    {
        "id": 9,
        "text": """RFP DOC Scope: The Contractor shall provide a virtual coaching platform that includes scheduling, coach 
matching, assessments, a resource portal, and on-demand specialty coaching available for 
each coaching participant. The Executive Coaching shall take place virtually, consisting of 
individualized, one-on-one sessions. 
Doc Page Number: 8
Chunk:
3.  TECHNICAL REQUIREMENTS 
 
The Contractor shall provide online subscription services with online access to the digital 
libraries via the website platform, 24 hours a day, 7 days a week, with customer support. 
 
3.1  Executive Coaching: 
 
The Contractor shall provide all services, materials, supplies, equipment, and project 
supervision, as required in connection with this Statement of Work (SOW).  The executive 
coaching engagement shall consist of: 
 
Coaching, assessment & development resources: 
 
  1:1 Coaching by ICF credentialed coaches. 
  On-Demand Coaching with sessions occurring within one business day 
  Learning/Development Resources to support the coachees to gain knowledge and 
develop skills in coaching areas which includes a whole-person approach 
  Assessment to be completed at start and end of engagements 
  Capacity to offer 360 Assessments aligned with Office of Personnel Management’s 
Executive Core Qualifications included in the platform/licensing fee. 
  Platform access for users to serve as single stop for all services/resources and for admins 
to show real time monitoring and usage (dashboard as well as reports). Interested parties 
will be requested to provide a demo of their platform.  
  Demonstration of ability to scale resources is necessary due to nature of the contracting 
mechanism""",
        "output": """CRITICAL: The Contractor shall provide 24/7 online access to the digital libraries via the website platform, with customer support.
        CRITICAL: The executive coaching engagement shall consist of 1:1 Coaching by ICF credentialed coaches, On-Demand Coaching with sessions occurring within one business day, Learning/Development Resources to support the coachees to gain knowledge and develop skills in coaching areas which includes a whole-person approach, Assessment to be completed at start and end of engagements, Capacity to offer 360 Assessments aligned with Office of Personnel Management’s Executive Core Qualifications included in the platform/licensing fee, Platform access for users to serve as single stop for all services/resources and for admins to show real time monitoring and usage (dashboard as well as reports), and Demonstration of ability to scale resources is necessary due to nature of the contracting mechanism.""",
    },
    {
        "id": 10,
        "text": """RFP DOC Scope: The Contractor shall provide a virtual coaching platform that includes scheduling, coach 
matching, assessments, a resource portal, and on-demand specialty coaching available for 
each coaching participant. The Executive Coaching shall take place virtually, consisting of 
individualized, one-on-one sessions. 
Doc Page Number: 10
Chunk:
The Contractor shall provide deliverable(s) in a format mutually agreed upon by TEI and 
the Contractor.  The following deliverables are not expected to change.   
 
 
SOW SECTION  DELIVERABLE  DUE DATE 
4.1  Monthly status report.  Monthly by no later than the 
7th calendar day for the 
previous month’s activities. 
4.1.3  Post Session Survey 
Results 
Monthly by no later than the 
7th calendar day for the 
previous month’s activities 
4.1.4  Behavioral Change Data  Quarterly by no later than the 
15th calendar day for the 
previous quarter’s activities 
4.2  Final Report  Prior to completion of the 
period of performance.""",
        "output": """INFORMATIVE: Deliverables will be as follows - Monthly Status Report (4.1), Post Session Survey Results (4.1.3), Behavioral Change Data (4.1.4), Final Report (4.2)"""
    }
]