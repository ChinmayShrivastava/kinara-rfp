import re

def _contains_date(text):
    # Check if the document contains a date
    # date can be in the format of 01/01/2021 or January 1, 2021 or 01-01-2021 or 01.01.2021 or 01 01 2021 or 1 Jan 2021
    # or 1 January 2021 or 1st January 2021 or 1st Jan 2021 or 1st Jan, 2021 or 1st January, 2021
    re_pattern = r'(\d{1,2}[-/\. ]\d{1,2}[-/\. ]\d{2,4})|((\d{1,2}(st|nd|rd|th)?\s)?(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{2,4})'
    return re.search(re_pattern, text)

def _contains_currency(text):
    # Check if the document contains a currency
    # Currency can be in the format of $1,000,000 or $1M or $1 million
    re_pattern = r'\$\d{1,3}(,\d{3})*(\.\d{1,2})?(\s?[Mm]illion)?'
    return re.search(re_pattern, text)

def _contains_time(text):
    # Check if the document contains a time
    # Time can be in the format of 12:00 AM or 12:00 PM or 12:00:00 AM or 12:00:00 PM
    re_pattern = r'(\d{1,2}:\d{2}(:\d{2})?\s?[AaPp][Mm])'
    return re.search(re_pattern, text)

def _contains_email(text):
    # Check if the document contains an email
    re_pattern = r'[\w\.-]+@[\w\.-]+'
    return re.search(re_pattern, text)

def _contains_url(text):
    # Check if the document contains a URL
    re_pattern = r'https?://\S+'
    return re.search(re_pattern, text)

def _contains_phone_number(text):
    # Check if the document contains a phone number
    re_pattern = r'(\d{3}-\d{3}-\d{4})|(\(\d{3}\)\s?\d{3}-\d{4})'
    return re.search(re_pattern, text)

reannotations = {
    "contains_date": _contains_date,
    "contains_currency": _contains_currency,
    "contains_time": _contains_time,
    "contains_email": _contains_email,
    "contains_url": _contains_url,
    "contains_phone_number": _contains_phone_number
}