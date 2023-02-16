from pathlib import Path


def add_breaks_on_timestamps(text):
    return text.replace("<span", "<p><br /></p> <span")


def remove_all_breaks(text):
    return text.replace("<p><br /></p>", " ")


def get_format_otr(file_path_to_otr):
    otr_file_content = Path(file_path_to_otr).read_text("utf8")
    no_breaks = remove_all_breaks(otr_file_content)
    format_otr = add_breaks_on_timestamps(no_breaks)
    return format_otr.replace("\xa0", " ")
