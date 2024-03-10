from rfpparser.RFPParser import RFPParser
import chromadb
from llama_index.core import StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.legacy.retrievers import BM25Retriever
from llama_index.core.retrievers import QueryFusionRetriever

class RFPRetriever(RFPParser):
    def __init__(
            self,
            pdf_path: str = None,
            verbose: bool = False
    ):
        super().__init__(pdf_path, verbose)
        self.verbose = verbose
        # self.chroma_client = chromadb.EphemeralClient()
        # self.chroma_collection = self.chroma_client.create_collection(self.file_name.replace('.pdf', '').replace(' ', '_'))
        # # log
        # self.logger.info(f'RFPRetriever initialized for {self.file_name} with chroma_collection count: {self.chroma_collection.count()}')
        # self.chroma_store = ChromaVectorStore(chroma_collection=self.chroma_collection)
        # self.chroma_storage_context = StorageContext.from_defaults(vector_store=self.chroma_store)
        if not self.nodes:
            self.chunks()
        self.chroma_index = VectorStoreIndex.from_documents(
            self.documents,
            transformations=[self.splitter]
        )
        self.chroma_retriever = self.chroma_index.as_retriever()
        print(self.chroma_index.docstore.__dict__['_kvstore'].__dict__)
        self.bm25_retriever = BM25Retriever.from_defaults(
            nodes=self.nodes, similarity_top_k=10
        )
        self.retriever = QueryFusionRetriever(
            [self.chroma_retriever],
            retriever_weights=[1],
            similarity_top_k=10,
            num_queries=3,  # set this to 1 to disable query generation
            mode="relative_score",
            use_async=False,
            verbose=True,
        )

    def retrieve(self, query: str):
        return self.retriever.retrieve(query)