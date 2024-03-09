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
            logger = logging.getLogger()
        else:
            logger = logging.getLogger()
            logger.disabled = True
        self.pdf_path = pdf_path
        self.file_name = self.pdf_path.split('/')[-1]
        # log
        logger.info(f"PDFParser for {self.pdf_path}")

    def __str__(self) -> str:
        _str = f"PDFParser for {self.pdf_path}"
        return _str
    
    def _get_chunks(
            self,
            chunk_size: int = 512,
            paragraph_separator: str = '\n\n',
            chunk_overlap: int = 128,
            ):
        from llama_index import SimpleDirectoryReader
        from llama_index.core.node_parser import SentenceSplitter
        reader = SimpleDirectoryReader(input_files=[self.pdf_path])
        documents = reader.load_data()
        splitter = SentenceSplitter(chunk_size=chunk_size, paragraph_separator=paragraph_separator, chunk_overlap=chunk_overlap)
        nodes = splitter.get_nodes_from_documents(documents)
        # self.chunks = [x.text for x in nodes]
        self.chunks = [
            {
                "text": x.text,
                "metadata": {
                    "page_no": x.metadata["page_label"],
                    "file_type": x.metadata["file_type"],
                    "chunk_no": i,
                }
            } for i, x in enumerate(nodes)
        ]
        return self.chunks
    
    def get_chunks(self):
        return self._get_chunks()