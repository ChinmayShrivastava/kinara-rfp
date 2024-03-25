import logging
from typing import Callable, Dict, List

from langchain_core.prompts import ChatPromptTemplate
from pdf_page_annotator import PDFAnnotator
from python_state_manager import StateManager
from rfpextractor.llmchains.extractionchain import ExtractionChain
from rfpextractor.llmchains.prompts import (COMPLIANCE_PROMPT,
                                            ELIGIBILITY_PROMPT,
                                            EVAL_CRITERIA_PROMPT,
                                            IMPORTANT_DATES_PROMPT,
                                            RFP_INFO_PROMPT, 
                                            SUBMISSION_PROMPT)
from rfpextractor.state.rfpstate import Callbacks, statemetadatas, statevalues

# ChatPromptTemplate.from_template

class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'

class RFPActions:

    def __init__(
        self,
        pdf_path: str,
        verbose: bool = False
    ):
        self.pdf_path = pdf_path
        self.annotator = PDFAnnotator(pdf_path, verbose=verbose)
        self.reader = self.annotator.reader
        self.verbose = verbose
        self.state_manager = StateManager(
            stateids=statevalues,
            statevalues=statevalues,
            metadatas=[a for _, a in statemetadatas.items()],
            currentstateid='init'
        )
        self.complete = False
        if self.verbose:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.INFO)

    def initializing(self):
        self.logger.info("Initializing")

    def get_relevant_chunks(self, key: str) -> List[str]:
        query_dispatch = {
            "rfp_info": "Any and all information that can be used to identify the RFP, such as the title, the issuing organization, the issuing date, the deadline, etc.",
            "important_dates": "Important dates",
            "eligibility": "Any and all information that can be used to identify eligibility criteria",
            "submission": "Any and all instructions relating to submissions and document format",
            "evaluation": "Any and all information that can be used to identify evaluation criteria",
            "compliances": "Any and all information that can be used to identify compliances",
        }
        query = query_dispatch[key]
        chunks = self.annotator.get_relevant_pages(query)
        # each chunk is a whole page
        return chunks['texts']

    def page_annotation(self):
        self.annotator.run_extraction_pipeline()
        currentstate = self.state_manager.get_current_state()
        currentstate.metadata["pages_used"] = self.annotator.annotation_state["toc_pages"]
        self.logger.info(f"Pages used: {currentstate.metadata['pages_used']}")
        currentstate.metadata["annotations"] = self.annotator.contents
        self.logger.info(f"Annotations: {currentstate.metadata['annotations']}")

    def rfp_info(self):
        self.logger.info("Extracting RFP info")
        chunks = self.get_relevant_chunks('rfp_info')
        rfp_info_schema = {
            "title": "None",
            "issuing_organization": "None",
            "unique_id": "None",
            "url": "None",
        }
        prompt = RFP_INFO_PROMPT.format_map(
            SafeDict(schema="\n".join([f"{k}: {v}" for k, v in rfp_info_schema.items()]))
        )
        prompt = ChatPromptTemplate.from_template(prompt)
        info = []
        e = ExtractionChain(
            prompt=prompt,
        )
        for chunk in chunks:
            info.extend([e.invoke(chunk)])
        current_state = self.state_manager.get_current_state()
        current_state.metadata["rfp_info"] = info
        self.logger.info(f"RFP info updated")

    def important_dates(self):
        self.logger.info("Extracting important dates")
        chunks = self.get_relevant_chunks('important_dates')
        important_dates_schema = {
            "deadline": "None",
            "announcement_date": "None",
            "submission_start_date": "None",
            "submission_end_date": "None",
        }
        prompt = IMPORTANT_DATES_PROMPT.format_map(
            SafeDict(schema="\n".join([f"{k}: {v}" for k, v in important_dates_schema.items()]))
        )
        prompt = ChatPromptTemplate.from_template(prompt)
        dates = []
        e = ExtractionChain(
            prompt=prompt,
        )
        for chunk in chunks:
            dates.extend([e.invoke(chunk)])
        current_state = self.state_manager.get_current_state()
        current_state.metadata["important_dates"] = dates

    def eligibility(self):
        self.logger.info("Extracting eligibility criteria")
        chunks = self.get_relevant_chunks('eligibility')
        eligibility_data = []
        prompt = ChatPromptTemplate.from_template(
            ELIGIBILITY_PROMPT
        )
        e = ExtractionChain(
            prompt=prompt,
        )
        for chunk in chunks:
            eligibility_data.extend([e.invoke(chunk)])
        current_state = self.state_manager.get_current_state()
        current_state.metadata["eligibility"] = eligibility_data

    def submission(self):
        self.logger.info("Extracting submission info")
        chunks = self.get_relevant_chunks('submission')
        submission_data = []
        prompt = ChatPromptTemplate.from_template(
            SUBMISSION_PROMPT
        )
        e = ExtractionChain(
            prompt=prompt,
        )
        for chunk in chunks:
            submission_data.extend([e.invoke(chunk)])
        current_state = self.state_manager.get_current_state()
        current_state.metadata["submission"] = submission_data

    def evaluation(self):
        self.logger.info("Extracting evaluation criteria")
        chunks = self.get_relevant_chunks('evaluation')
        evaluation_data = []
        prompt = ChatPromptTemplate.from_template(
            EVAL_CRITERIA_PROMPT
        )
        e = ExtractionChain(
            prompt=prompt,
        )
        for chunk in chunks:
            evaluation_data.extend([e.invoke(chunk)])
        current_state = self.state_manager.get_current_state()
        current_state.metadata["evaluation"] = evaluation_data

    def compliances(self):
        self.logger.info("Extracting compliances")
        chunks = self.get_relevant_chunks('compliances')
        compliance_data = []
        prompt = ChatPromptTemplate.from_template(
            COMPLIANCE_PROMPT
        )
        e = ExtractionChain(
            prompt=prompt,
        )
        for chunk in chunks:
            compliance_data.extend([e.invoke(chunk)])
        current_state = self.state_manager.get_current_state()
        current_state.metadata["compliances"] = compliance_data

    def classification(self):
        print("Extracting classification info")

# if __name__ == '__main__':
#     print(RFP_INFO_PROMPT.format_map(SafeDict(schema="schema")))