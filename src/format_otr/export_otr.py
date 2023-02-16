from format_otr.utils import get_json_from_file, parse_html, get_all_timestamps
from pathlib import Path


def get_text_between(start, end):
    text = ""
    tag = start.next_element.next_element
    while tag != end:
        if tag.name is None:
            text += tag.text
        tag = tag.next_element
    return text


def get_text_till_end(start):
    text = ""
    tag = start.next_element.next_element
    while tag:
        if tag.name is None:
            text += tag.text
        tag = tag.next_element
    return text


def get_txt(file_path_to_otr):
    otr_file = Path(file_path_to_otr)
    json_otr = get_json_from_file(otr_file)
    soup = parse_html(json_otr["text"])
    timestamps = get_all_timestamps(soup)
    txt = ""
    for start, end in zip(timestamps, timestamps[1:]):
        txt += f"{start.string} {get_text_between(start, end).strip()}\n"
    txt += f"{timestamps[-1].string} {get_text_till_end(timestamps[-1]).strip()}"
    # \xa0 is non-breaking space. Replace it with space.
    txt = txt.replace("\xa0", " ")
    return txt
