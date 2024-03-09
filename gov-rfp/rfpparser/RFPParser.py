from PDFParser import PDFParser

class RFPParser(PDFParser):
    def __init__(
            self,
            pdf_path,
            verbose: bool = True,
            ):
        super().__init__(pdf_path, verbose=verbose)

    def __str__(self) -> str:
        _str = f"RFPParser for {self.pdf_path}"
        return _str