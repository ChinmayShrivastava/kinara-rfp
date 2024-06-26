from python_state_manager import StateManager
from rfpextractor.actions.rfpactions import RFPActions
from rfpextractor.state.rfpstate import Callbacks, statemetadatas, statevalues


class DocExtraction(RFPActions):

    def __init__(
        self,
        pdf_path: str,
        verbose: bool = False
    ):
        super().__init__(pdf_path, verbose=verbose)
        self.callbacks = Callbacks()

    def run(self):
        self._run_extraction_pipeline()

    def _run_extraction_pipeline(self):
        while not self.complete:
            try:
                currentstateid = self.state_manager.get_current_state().stateid
                ### Perform actions here ###
                self.callbacks(self, currentstateid, "entry")
                ######
                # complete stage
                self.state_manager.complete_state()
            except:
                self.complete = self.state_manager.is_finished()
                if self.complete:
                    print("Extraction complete")
                    break

    async def run_async(self):
        self._run_extraction_pipeline_async()

    async def _run_extraction_pipeline_async(self):
        while not self.complete:
            try:
                currentstateid = self.state_manager.get_current_state().stateid
                ### Perform actions here ###
                await self.callbacks(self, currentstateid, "entry")
                ######
                # complete stage
                self.state_manager.complete_state()
            except:
                self.complete = self.state_manager.is_finished()
                if self.complete:
                    print("Extraction complete")
                    break

if __name__ == "__main__":
    pdf_path = "egsearch.pdf"
    # pdf_annotator = PDFAnnotator(pdf_path)
    rfp_extraction = DocExtraction(pdf_path, verbose=True)
    rfp_extraction.run()