import logging
import tqdm

class PDFParser:

    def __init__(
            self,
            pdf_path,
            verbose: bool = True,
            ):
        self.verbose = verbose
        if self.verbose:
            self.logger = logging.getLogger()
        else:
            self.logger = logging.getLogger()
            self.logger.disabled = True
        self.pdf_path = pdf_path
        self.file_name = self.pdf_path.split('/')[-1]
        self._chunks = None
        self.nodes = None
        self.splitter = None
        self.reader = None
        self.documents = None
        # log
        self.logger.info(f"PDFParser for {self.pdf_path}")

    def __str__(self) -> str:
        _str = f"PDFParser for {self.pdf_path}"
        return _str
    
    def _get_chunks(
            self,
            chunk_size: int = 512,
            paragraph_separator: str = '\n\n',
            chunk_overlap: int = 0,
            ):
        from llama_index.core import SimpleDirectoryReader
        from llama_index.core.node_parser import SentenceSplitter
        self.reader = SimpleDirectoryReader(input_files=[self.pdf_path])
        self.documents = self.reader.load_data()
        self.splitter = SentenceSplitter(chunk_size=chunk_size, paragraph_separator=paragraph_separator, chunk_overlap=chunk_overlap)
        self.nodes = self.splitter.get_nodes_from_documents(self.documents)
        # self.chunks = [x.text for x in nodes]
        self._chunks = [
            {
                "text": x.text,
                "metadata": {
                    "page_no": x.metadata["page_label"],
                    "file_type": x.metadata["file_type"],
                    "chunk_no": i,
                }
            } for i, x in enumerate(self.nodes)
        ]
        # log
        self.logger.info(f"Got {len(self._chunks)} chunks")
        return self._chunks
    
    def chunks(self):
        if not self._chunks:
            self._get_chunks()
        return self._chunks