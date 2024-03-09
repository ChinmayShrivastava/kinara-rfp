from .PDFParser import PDFParser

class RFPParser(PDFParser):
    def __init__(self, rfp):
        self.rfp = rfp
        self.rfp_text = self