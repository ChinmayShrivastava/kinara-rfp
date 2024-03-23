from typing import Callable, Dict, List

from llmchains.extractionchain import ExtractionChain
from llmchains.prompts import (COMPLIANCE_PROMPT, EVAL_CRITERIA_PROMPT,
                               IMPORTANT_DATES_PROMPT, RFP_INFO_PROMPT)
from pdf_page_annotator import PDFAnnotator
from python_state_manager import StateManager
from state.rfpstate import Callbacks, statemetadatas, statevalues


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

    def initializing(self):
        print("Initializing")

    def get_relevant_chunks(self, key: str) -> List[str]:
        query_dispatch = {
            "rfp_info": "Any and all information that can be used to identify the RFP, such as the title, the issuing organization, the issuing date, the deadline, etc.",
            "important_dates": "Any and all information that can be used to identify important dates, such as the deadline, the date of the announcement, etc.",
            "eligibility": "Any and all information that can be used to identify eligibility criteria",
            "submission": "Any and all information that can be used to identify submission requirements",
            "evaluation": "Any and all information that can be used to identify evaluation criteria",
            "compliances": "Any and all information that can be used to identify compliances",
        }
        query = query_dispatch[key]
        chunks = self.annotator.get_relevant_chunks(query)
        # each chunk is a whole page
        return chunks

    def page_annotation(self):
        self.annotator.run_extraction_pipeline()
        currentstate = self.state_manager.get_current_state()
        currentstate.metadata["pages_used"] = self.annotator.annotation_state["toc_pages"]
        currentstate.metadata["annotations"] = self.annotator.contents

    def rfp_info(self):
        chunks = self.get_relevant_chunks('rfp_info')
        info = []
        e = ExtractionChain(
            prompt=RFP_INFO_PROMPT,
        )
        for chunk in chunks:
            info.extend(e.invoke(chunk))
        current_state = self.state_manager.get_current_state()
        current_state.metadata["rfp_info"] = info

    def important_dates(self):
        chunks = self.get_relevant_chunks('important_dates')
        dates = []
        e = ExtractionChain(
            prompt=IMPORTANT_DATES_PROMPT,
        )
        for chunk in chunks:
            dates.extend(e.invoke(chunk))
        current_state = self.state_manager.get_current_state()
        current_state.metadata["important_dates"] = dates

    def eligibility(self):
        print("Extracting eligibility info")

    def submission(self):
        print("Extracting submission info")

    def evaluation(self):
        print("Extracting evaluation info")

    def compliances(self):
        print("Extracting compliances")

    def classification(self):
        print("Extracting classification info")