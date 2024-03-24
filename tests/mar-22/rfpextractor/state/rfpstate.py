from typing import Callable, Dict, List

statevalues = [
    "init",
    "page annotation",
    "rfp info",
    "important dates",
    "eligibility",
    "submission",
    "evaluation",
    "compliances",
    "classification",
]

statemetadatas = {
    "init": {"init state": "init state"},
    "page annotation": {
        "pages_used": [],
        "annotations": [],
    },
    "rfp info": {
        "rfp_name": "",
        "rfp_description": "",
        "rfp_id": "",
        "rfp_url": "",
    },
    "important dates": {
        "submission_deadline": "",
    },
    "eligibility": {
        "eligibility_criteria": "",
        "eligibility_documents": "",
        "eligibility_conditions": "",
    },
    "submission": {
        "submission_method": "",
        "submission_documents": "",
        "submission_conditions": "",
    },
    "evaluation": {
        "evaluation_criteria": "",
        "evaluation_documents": "",
        "evaluation_conditions": "",
        "rubric": "",
    },
    "compliances": {
        "compliances": "",
    },
    "classification": {
        "classification": "",
    },
}

def callback_dispatcher(obj, stateid, entryorexit) -> Dict[str, List[Callable]]:

    entry_callbacks = {
        "init": [obj.initializing],
        "page annotation": [obj.page_annotation],
        "rfp info": [obj.rfp_info],
        "important dates": [obj.important_dates],
        "eligibility": [obj.eligibility],
        "submission": [obj.submission],
        "evaluation": [obj.evaluation],
        "compliances": [obj.compliances],
        "classification": [obj.classification],
    }

    exit_callbacks = {
        "init": [],
        "page annotation": [],
        "rfp info": [],
        "important dates": [],
        "eligibility": [],
        "submission": [],
        "evaluation": [],
        "compliances": [],
        "classification": [],
    }

    if entryorexit == "entry":
        return entry_callbacks[stateid]
    elif entryorexit == "exit":
        return exit_callbacks[stateid]

class Callbacks:

    def __call__(self, obj, stateid, entryorexit):
        if entryorexit == "entry":
            for callback in callback_dispatcher(obj, stateid, entryorexit):
                callback()
        elif entryorexit == "exit":
            for callback in callback_dispatcher(obj, stateid, entryorexit):
                callback()