from typing import List, Dict
from .FEW_SHOT_EXAMPLES import FEW_SHOT_EXAMPLES, FINAL_PROMPT_TEMPLATE, FORMAT_TEMPLATE_FOR_NEW_CHUNK, FS_EXAMPLE_TEMPLATE
from govrfp.rfpinsights._chromadb import return_collection, add_entries_to_collection

class Selector:
    """
    This takes in a a list of few shot examples at initiation.

    At query, it first matches the chunk with the few shot examples and then returns a final prompt to be used for text generation.
    """
    def __init__(
        self,
        few_shot_examples: List[Dict] = FEW_SHOT_EXAMPLES,
        force_update_collection: bool = False
    ):
        self.few_shot_examples = few_shot_examples
        self.fscollection = return_collection(path="./fsdata", collection_name="fewshot")
        if self.fscollection.count() == 0 or force_update_collection:
            self.fscollection = add_entries_to_collection(
                docs=[i['text'] for i in few_shot_examples],
                metadata=[{"id": str(i)} for i in few_shot_examples],
                ids=[str(i['id']) for i in few_shot_examples],
                collection=self.fscollection
            )

    def query(self, chunk: str, page_number) -> str:
        """
        This takes in a chunk and returns a final prompt to be used for text generation.
        """
        match = self.fscollection.query(
            query_texts=[chunk],
            n_results=2
        )
        ids = [int(i) for i in match['ids'][0]]
        _fs = {}
        for _chunk in self.few_shot_examples:
            if _chunk['id'] in ids:
                _fs[_chunk['id']] = _chunk
        fs_examples = [FS_EXAMPLE_TEMPLATE.format(chunk = _fs[i]['text'], output = _fs[i]['output']) for i in ids]
        new_chunk = FORMAT_TEMPLATE_FOR_NEW_CHUNK.format(chunk=chunk, page_number=page_number)
        return FINAL_PROMPT_TEMPLATE.format(fs1=fs_examples[0], fs2=fs_examples[1], current_chunk=new_chunk)