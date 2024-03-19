from prompt_autotune import TunePrompt

if __name__ == "__main__":

    prompt = '''Given the following compliances, return any compliances that are required while writing an application for the RFP.
    Return None, if no such compliances are found.
    --------------------
    Example 1:
    Given compliances:
    - Deadline: 08/31/2023 1700 ET
    - Offer due date: 08/31/2023 1700 ET
    - Submit invoices to address shown in block 18a
    Response:
    - Deadline is 5:00 PM ET on August 31, 2023
    --------------------
    Example 2:
    Given compliances:
    - Any deviation or delay upon the agreed upon delivery time will be recorded and influence the contractor closing assessment made by the COR
    - Offeror must provide description of service(s) or product(s)
    - Number and Names of Sub-contractors, if any
    Response:
    - None
    --------------------
    Response:'''

    task = """You will be given excerpts from an RFP application. THe excerpts can be a paragraph or multiple paragraphs. You are required to generate a list of exhaustive standalone compliance requirements for the applicant. This list will be used as a checklist while drafting the application proposal. If no such compliances are found, return None.
    Pleae leave out anything that is additional and not a compliance requirement."""

    tuner = TunePrompt(
        task=task,
        prompt=prompt,
    )

    tuner()

    # save tuner.prompt in a file
    with open("tests/mar-19/tuned_prompt.txt", "w") as file:
        file.write(tuner.prompt)

    # save the examples into a file
    with open("tests/mar-19/examples.txt", "w") as file:
        for example in tuner.examples:
            # example.input and example.output
            file.write(f"Input: {example.input}\nOutput: {example.output}\n\n")
    